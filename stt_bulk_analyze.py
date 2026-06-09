import requests
import json
import csv
import time

# 🛠️ 백엔드 실제 고정 API 주소 세팅
API_URL = "http://210.110.250.32:8000"
UTTERANCE_API_URL = f"{API_URL}/utterances"

# 최종 결과 저장 파일명
ANALYSIS_REPORT_CSV = f"stt_bulk_analysis_report_{int(time.time())}.csv"

def run_bulk_analysis():
    target_session_id = 1 
    SESSION_UTTERANCES_URL = f"{API_URL}/sessions/{target_session_id}/utterances"
    
    print(f"📡 [Step 1] {target_session_id}번 세션의 전체 발화 데이터 수집 중... ({SESSION_UTTERANCES_URL})")
    try:
        res = requests.get(SESSION_UTTERANCES_URL, timeout=5)
        if res.status_code != 200:
            print(f"❌ 발화 목록 조회 실패 (Code: {res.status_code})")
            return
        
        # 🚨 [방어 코드 1] 만약 서버 응답이 JSON 텍스트 상태로 오면 딕셔너리로 강제 변환
        raw_data = res.json()
        if isinstance(raw_data, str):
            try:
                utterances = json.loads(raw_data)
            except:
                utterances = [raw_data]
        else:
            utterances = raw_data
            
    except Exception as e:
        print(f"❌ 서버 연결 실패: {e}")
        return

    total_count = len(utterances)
    print(f"✅ 총 {total_count}개의 발화(Utterance) 데이터가 감지되었습니다.")
    
    # 결과 저장용 CSV 파일 생성
    with open(ANALYSIS_REPORT_CSV, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["발화ID", "STT모델구분", "라즈베리파이_STT원본", "서버_AI_최종교정본", "RAG_매칭여부"])

    print("\n🚀 [Step 2] 100회 발화 일괄 분석 실행 및 결과 대조 시작...")
    
    success_analyze = 0
    for idx, utt in enumerate(utterances, 1):
        # 🚨 [방어 코드 2] 에러 추적 파트: utt가 딕셔너리가 아닌 단순 문자열(str)일 경우 예외 처리
        if isinstance(utt, str):
            print(f"⚠️ 경고: 서버가 JSON 객체가 아닌 단순 문자열을 보냈습니다. 가상 매핑을 시도합니다.")
            utt_id = idx  # 임시 가상 ID 부여
            stt_text = utt
            model_group = "simulated_string_data"
        else:
            # 정상적인 딕셔너리 구조일 때
            utt_id = utt.get("id", idx)
            stt_text = utt.get("stt_text", "")
            model_group = utt.get("stt_model", "unknown")
        
        ANALYZE_REQUEST_URL = f"{API_URL}/utterances/{utt_id}/analyze"
        RESULT_GET_URL = f"{API_URL}/utterances/{utt_id}/analysis"
        
        refined_text = "분석실패"
        rag_status = "N/A"
        
        try:
            # ① 분석 POST 요청 보내기 (트리거)
            analyze_res = requests.post(ANALYZE_REQUEST_URL, timeout=5)
            
            if analyze_res.status_code in [200, 201]:
                # ② 분석 결과조회 GET 요청하기
                result_res = requests.get(RESULT_GET_URL, timeout=5)
                if result_res.status_code == 200:
                    analysis_data = result_res.json()
                    
                    if isinstance(analysis_data, list) and len(analysis_data) > 0:
                        target_data = analysis_data[0]
                        refined_text = target_data.get("corrected_text", target_data.get("processed_text", "교정완료"))
                        rag_status = "RAG매칭" if target_data.get("is_rag", True) else "일반LLM교정"
                        success_analyze += 1
                    elif isinstance(analysis_data, dict):
                        refined_text = analysis_data.get("corrected_text", analysis_data.get("processed_text", "교정완료"))
                        rag_status = "RAG매칭" if analysis_data.get("is_rag", True) else "일반LLM교정"
                        success_analyze += 1
        except Exception as e:
            refined_text = f"통신에러: {e}"

        print(f" ⚙️ [{idx}/{total_count}] ID:{utt_id} [{model_group}] -> 라즈베리: {stt_text} ➡️ 서버교정: {refined_text} ({rag_status})")
        
        # CSV 파일에 한 줄씩 기록 저장
        with open(ANALYSIS_REPORT_CSV, mode="a", encoding="utf-8-sig", newline="") as f:
            csv.writer(f).writerow([utt_id, model_group, stt_text, refined_text, rag_status])
            
        time.sleep(0.1)

    print("\n" + "="*60)
    print("🏆 서버 일괄 분석 및 최종 검증 리포트 생성 완료!")
    print(f"📊 총 처리: {total_count}건 | AI 문장 교정 완료: {success_analyze}건")
    print(f"📝 최종 결과 보고서 파일: {ANALYSIS_REPORT_CSV}")
    print("="*60)

if __name__ == "__main__":
    run_bulk_analysis()