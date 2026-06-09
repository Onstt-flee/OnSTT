import requests
import json
import time

# 🛠️ 백엔드 실제 GPU 서버 IP 및 포트 정보 설정
API_BASE_URL = "http://210.110.250.32:8000"
SESSION_ID = 1  # 벤치마크 테스트를 진행했던 세션 ID

def generate_analysis_markdown():
    # 최종 저장될 마크다운 파일명
    output_filename = f"STT_Analysis_Report_{int(time.time())}.md"
    
    print(f"📡 [Step 1] {SESSION_ID}번 세션의 발화 목록을 가져오는 중...")
    try:
        session_res = requests.get(f"{API_BASE_URL}/sessions/{SESSION_ID}/utterances", timeout=5)
        if session_res.status_code != 200:
            print(f"❌ 발화 목록 조회 실패 (Code: {session_res.status_code})")
            return
        
        session_data = session_res.json()
        # 앞서 판명된 실제 서버의 json 키 구조(utterances) 반영
        utterance_list = session_data.get("utterances", [])
        
    except Exception as e:
        print(f"❌ 서버 연결 실패: {e}")
        return

    total_count = len(utterance_list)
    print(f"✅ 총 {total_count}개의 발화 데이터가 확인되었습니다.")
    print("🚀 [Step 2] 각 발화별 /analysis 데이터를 추출하여 마크다운 문서 생성 시작...\n")

    # 마크다운 파일 작성 시작 (상단 타이틀 및 헤더)
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(f"# 📊 일본어 STT 온디바이스 전처리 및 AI 분석 결과 최종 보고서\n\n")
        f.write(f"- **검증 세션 번호:** {SESSION_ID}번 세션\n")
        f.write(f"- **추출 일시:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"- **총 분석 대상 발화 수:** {total_count}건\n")
        f.write(f"- **분석 파이프라인 AI 엔진:** qwen/qwen3-4b-2507 (RAG 하이브리드 엔진)\n\n")
        f.write(f"--- \n\n")

        success_count = 0
        
        for idx, utt in enumerate(utterance_list, 1):
            utt_id = utt.get("utterance_id")
            stt_text = utt.get("stt_text", "")
            
            # 특정 발화의 분석 결과 조회 API 호출
            analysis_url = f"{API_BASE_URL}/utterances/{utt_id}/analysis"
            
            try:
                analysis_res = requests.get(analysis_url, timeout=5)
                if analysis_res.status_code != 200:
                    continue
                
                analysis_data = analysis_res.json()
                if not analysis_data or len(analysis_data) == 0:
                    print(f" ⚠️ [{idx}/{total_count}] ID:{utt_id} -> 아직 AI 분석(Analyze)이 실행되지 않은 발화입니다. 패스합니다.")
                    continue
                
                # 리스트의 첫 번째 실제 데이터 바인딩
                analysis = analysis_data[0]
                success_count += 1
                
                # 📝 마크다운에 발화별 상세 블록 쓰기
                f.write(f"## 📌 발화 샘플 데이터 #{idx} (ID: {utt_id})\n\n")
                
                # 대조 테이블 작성
                f.write(f"| 구분 | 내용 |\n")
                f.write(f"| :--- | :--- |\n")
                f.write(f"| **라즈베리파이 STT 원문** | `{stt_text}` |\n")
                f.write(f"| **서버 AI 최종 교정본** | **{analysis.get('corrected_text', '-')}** |\n")
                f.write(f"| **문장 적합성 여부** | {'✅ 정상 문장 (오류 없음)' if analysis.get('is_correct') else '❌ 교정 필요 문장'} |\n")
                f.write(f"| **심층 분석 수행 여부** | {'True' if analysis.get('needs_deep_analysis') else 'False'} |\n")
                f.write(f"| **AI 모델 확신도** | {analysis.get('confidence', 1) * 100}% |\n\n")

                # 한국어/일본어 총평 피드백
                f.write(f"### 💬 AI 정밀 피드백\n")
                f.write(f"- **한국어 해설:** {analysis.get('feedback_ko', '피드백 없음')}\n")
                f.write(f"- **일본어 해설:** {analysis.get('feedback_ja', '피드백 없음')}\n\n")

                # 매칭된 단어 컨텍스트 (vocab_context) 정리
                if analysis.get('vocab_context'):
                    f.write(f"### 📖 어휘 및 읽기 참고 자료 (Vocab Context)\n")
                    f.write(f"```text\n{analysis.get('vocab_context').strip()}\n```\n\n")

                # 매칭된 문법 컨텍스트 (grammar_context) 정리
                if analysis.get('grammar_context'):
                    f.write(f"### 📐 문법 규칙 매칭 근거 (Grammar Context)\n")
                    f.write(f"```text\n{analysis.get('grammar_context').strip()}\n```\n\n")

                # 탐지된 오류 유형 정보 (error_context) 정리
                if analysis.get('error_context'):
                    f.write(f"### ⚠️ 잠재적 오류 유형 검토 (Error Context)\n")
                    f.write(f"```text\n{analysis.get('error_context').strip()}\n```\n\n")
                
                f.write(f"--- \n\n") # 구분선
                print(f" ⚙️ [{idx}/{total_count}] ID:{utt_id} -> 마크다운 파싱 성공.")
                
            except Exception as e:
                print(f" ❌ [{idx}/{total_count}] ID:{utt_id} 처리 중 예외 에러: {e}")

    print("\n" + "="*60)
    print(f"🏆 마크다운 보고서 파일이 성공적으로 빌드되었습니다!")
    print(f"📊 총 조회 데이터: {total_count}건 | 마크다운 변환 완료: {success_count}건")
    print(f"📝 파일 확인: {output_filename}")
    print("="*60)

if __name__ == "__main__":
    generate_analysis_markdown()