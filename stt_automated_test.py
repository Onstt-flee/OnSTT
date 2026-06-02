import os
import time
import csv
import requests
from faster_whisper import WhisperModel

# 🛠️ 백엔드 실제 API 주소 규격 반영
API_URL = "http://210.110.250.32:8000"
SESSION_API_URL = f"{API_URL}/sessions"
UTTERANCE_API_URL = f"{API_URL}/utterances"

# 테스트 대상 데이터셋 경로 설정
DATASET_DIR = "./test_dataset"
GROUPS = ["low_skilled", "tts_perfect"]

def run_automated_test():
    # 1. Faster-Whisper 최적화 로딩 (정확성 극대화를 위해 민성님 튜닝 파라미터 적용)
    print("🤖 성능 검증용 고정밀 STT 엔진 로딩 중...")
    stt_model = WhisperModel("tiny", device="cpu", compute_type="int8")
    print("✅ STT 엔진 준비 완료.")

    # 2. 결과 저장용 CSV 파일 초기화
    csv_filename = f"stt_test_report_{int(time.time())}.csv"
    with open(csv_filename, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "그룹(숙련도)", "파일명", "STT_인식결과", "서버_전송상태", "소요시간(초)"])

    # 3. 데이터 수집을 위한 백엔드 DB 세션 최초 1회 생성
    target_user_id = 1
    current_session_id = 1
    
    print(f"⏳ 백엔드 서버에 테스트 전용 세션 생성 요청 중...")
    try:
        session_payload = {
            "user_id": target_user_id,
            "topic": "100회 대규모 음성 인식 성능 검증 테스트셋",
            "description": "저숙련자 50회 vs 표준 TTS 50회 비교 분석 데이터"
        }
        res = requests.post(SESSION_API_URL, json=session_payload, timeout=5)
        if res.status_code in [200, 201]:
            current_session_id = int(res.json().get("id", current_session_id))
            print(f"🔗 [성공] 테스트 세션 번호 {current_session_id}번 생성 완료.")
    except Exception as e:
        print(f"⚠️ 세션 생성 실패({e}), 기본 1번 세션으로 강제 연동 테스트 진행.")

    total_count = 0
    success_count = 0

    # 4. 2개 폴더(총 100개 파일) 자동 순회 기동
    for group in GROUPS:
        folder_path = os.path.join(DATASET_DIR, group)
        if not os.path.exists(folder_path):
            print(f"🚨 폴더가 존재하지 않습니다: {folder_path}")
            continue

        file_list = [f for f in os.listdir(folder_path) if f.endswith(".wav")]
        print(f"\n📂 [{group}] 그룹 테스트 시작 - 총 {len(file_list)}개 파일 감지됨")

        for idx, file_name in enumerate(file_list, 1):
            total_count += 1
            file_path = os.path.join(folder_path, file_name)
            
            start_time = time.time()
            
            # 🛠️ 음성 파일 로컬 변환 수행 (정확도 복원 파라미터 튜닝)
            segments, info = stt_model.transcribe(
                file_path,
                language="ja",          # 일본어 모드 고정
                beam_size=5,            # 정밀 탐색
                temperature=0.0,        # 환각 차단
                vad_filter=True,
                suppress_tokens=[]
            )
            
            recognized_text = "".join([segment.text for segment in segments]).strip()
            elapsed_time = round(time.time() - start_time, 2)

            # 🛠️ 백엔드 DB Utterance 테이블 규격에 맞춰 페이로드 구성 후 전송
            server_status = "실패"
            if recognized_text:
                utterance_payload = {
                    "session_id": int(current_session_id),
                    "stt_text": recognized_text,
                    "language": "ja",
                    "stt_model": f"faster-whisper-tiny-[{group}]"
                }
                try:
                    response = requests.post(UTTERANCE_API_URL, json=utterance_payload, timeout=5)
                    if response.status_code in [200, 201]:
                        server_status = "성공"
                        success_count += 1
                except:
                    server_status = "통신에러"

            # 콘솔 실시간 진행 상황 출력
            print(f" [{total_count}/100] [{group}] {file_name} -> 변환 결과: {recognized_text} ({elapsed_time}초) | DB전송: {server_status}")

            # CSV 보고서 파일에 한 줄씩 기록
            with open(csv_filename, mode="a", encoding="utf-8-sig", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([total_count, group, file_name, recognized_text, server_status, elapsed_time])

            # 서버 과부하 방지를 위한 미세한 대기 시간
            time.sleep(0.2)

    print("\n" + "="*60)
    print("🏆 대규모 100회 자동화 STT 벤치마크 테스트 완료!")
    print(f"📊 총 진행: {total_count}회 | DB 최종 저장 성공: {success_count}회")
    print(f"📝 상세 결과 리포트가 성공적으로 저장되었습니다: {csv_filename}")
    print("="*60)

if __name__ == "__main__":
    run_automated_test()