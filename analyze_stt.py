import pandas as pd
import glob
import os
from jiwer import cer

def analyze_stt_results():
    # 1. 가장 최근에 생성된 STT 결과 CSV 파일 찾기
    csv_files = glob.glob("stt_final_report_*.csv")
    if not csv_files:
        print("🚨 분석할 CSV 파일을 찾을 수 없습니다. 파일명을 확인해 주세요.")
        return
    
    latest_csv = max(csv_files, key=os.path.getctime)
    print(f"📊 분석 대상 파일: {latest_csv}\n")
    
    # 2. 데이터 불러오기
    df = pd.read_csv(latest_csv)
    
    # 공백이나 결측치 제거 및 문자열 변환
    df['원본매프텍스트'] = df['원본매프텍스트'].fillna("").astype(str).str.strip()
    df['STT추출값'] = df['STT추출값'].fillna("").astype(str).str.strip()
    
    # 3. 그룹별 데이터 분리
    tts_group = df[df['테스트그룹'] == 'tts_perfect']
    low_group = df[df['테스트그룹'] == 'low_skilled']
    
    # 4. 정확도(CER 기반) 계산 함수 정의
    def calculate_accuracy(group_df):
        total_cer = 0
        count = 0
        for _, row in group_df.iterrows():
            ref = row['원본매프텍스트']
            hyp = row['STT추출값']
            if not ref: continue  # 빈 문장 패스
            
            # CER(오류율) 계산 후 정확도(1 - 오류율) 환산
            error_rate = cer(ref, hyp)
            accuracy = max(0, 1 - error_rate)
            total_cer += accuracy
            count += 1
            
        return (total_cer / count) * 100 if count > 0 else 0

    # 5. 최종 결과 출력
    tts_acc = calculate_accuracy(tts_group)
    low_acc = calculate_accuracy(low_group)
    total_acc = calculate_accuracy(df)
    
    print("=" * 50)
    print("🏆 [제출용] STT 텍스트 정밀도 분석 결과")
    print("=" * 50)
    print(f"① 고숙련 표준 음성 (tts_perfect) 정확도 : {tts_acc:.2f} %")
    print(f"② 저숙련 변칙 음성 (low_skilled) 정확도 : {low_acc:.2f} %")
    print("-" * 50)
    print(f"🔥 전체 시스템 평균 음성 인식 정확도     : {total_acc:.2f} %")
    print("=" * 50)
    
    # 6. 요약 보고서 파일로도 자동 저장
    with open("stt_summary_report.txt", "w", encoding="utf-8") as f:
        f.write("=== STT TEXT PRECISION ANALYSIS REPORT ===\n")
        f.write(f"TTS Perfect Group Accuracy: {tts_acc:.2f}%\n")
        f.write(f"Low Skilled Group Accuracy: {low_acc:.2f}%\n")
        f.write(f"Total Average Accuracy: {total_acc:.2f}%\n")
    print("📝 분석 요약본이 'stt_summary_report.txt'로 저장되었습니다.")

if __name__ == "__main__":
    analyze_stt_results()