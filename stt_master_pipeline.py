import requests
import csv
import time

API_URL = "http://210.110.250.32:8000"
ANALYSIS_REPORT_CSV = f"stt_final_report_{int(time.time())}.csv"

def run_final_analysis():
    session_id = 1
    SESSION_URL = f"{API_URL}/sessions/{session_id}/utterances"
    
    print(f"📡 [Step 1] {session_id}번 세션 데이터 조회 중... ({SESSION_URL})")
    try:
        res = requests.get(SESSION_URL, timeout=5)
        data = res.json()
        
        # 🚨 드디어 찾은 진짜 데이터 리스트 경로!
        utterance_list = data.get("utterances", [])
        
    except Exception as e:
        print(f"❌ 데이터 조회 실패: {e}")
        return

    total_count = len(utterance_list)
    print(f"✅ 총 {total_count}개의 발화 데이터가 완벽하게 인식되었습니다!\n")
    
    # CSV 헤더 생성
    with open(ANALYSIS_REPORT_CSV, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["발화ID", "라즈베리파이_원본텍스트", "서버_최종_교정본", "RAG_매칭여부"])

    print("🚀 [Step 2] 전체 데이터 일괄 AI 분석(Analyze) 및 대조 시작...")
    
    success_count = 0
    # 316개의 데이터를 하나씩 돌면서 분석 시작
    for idx, utt in enumerate(utterance_list, 1):
        # 🚨 정확한 키 이름 매핑
        utt_id = utt.get("utterance_id")
        stt_text = utt.get("stt_text", "")
        
        analyze_url = f"{API_URL}/utterances/{utt_id}/analyze"
        result_url = f"{API_URL}/utterances/{utt_id}/analysis"
        
        refined_text = "분석 실패"
        rag_status = "N/A"
        
        try:
            # ① 분석 실행 트리거 (POST)
            req_analyze = requests.post(analyze_url, timeout=5)
            
            if req_analyze.status_code in [200, 201]:
                # ② 분석 결과 가져오기 (GET)
                req_result = requests.get(result_url, timeout=5)
                
                if req_result.status_code == 200:
                    analysis_data = req_result.json()
                    
                    if isinstance(analysis_data, list) and len(analysis_data) > 0:
                        target = analysis_data[0]
                        refined_text = target.get("corrected_text", target.get("processed_text", "완료"))
                        rag_status = "RAG매칭" if target.get("is_rag", True) else "일반LLM교정"
                        success_count += 1
                    elif isinstance(analysis_data, dict):
                        refined_text = analysis_data.get("corrected_text", analysis_data.get("processed_text", "완료"))
                        rag_status = "RAG매칭" if analysis_data.get("is_rag", True) else "일반LLM교정"
                        success_count += 1
                        
        except Exception as e:
            refined_text = f"에러: {e}"

        print(f" ⚙️ [{idx}/{total_count}] ID:{utt_id} | 원본: {stt_text} ➡️ 교정: {refined_text} ({rag_status})")
        
        # 한 줄씩 CSV 저장
        with open(ANALYSIS_REPORT_CSV, mode="a", encoding="utf-8-sig", newline="") as f:
            csv.writer(f).writerow([utt_id, stt_text, refined_text, rag_status])
            
        time.sleep(0.1) # 서버 과부하 방지

    print("\n" + "="*60)
    print(f"🏆 모든 분석 완료! 총 {total_count}개 중 {success_count}건 성공")
    print(f"📝 최종 결과 파일: {ANALYSIS_REPORT_CSV}")
    print("="*60)

if __name__ == "__main__":
    run_final_analysis()