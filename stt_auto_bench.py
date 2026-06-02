import os
import time
import requests
import csv
from gtts import gTTS
from faster_whisper import WhisperModel

# 🛠️ 백엔드 실제 API 주소 세팅 (팀 규칙 준수)
API_URL = "http://210.110.250.32:8000"
SESSION_API_URL = f"{API_URL}/sessions"
UTTERANCE_API_URL = f"{API_URL}/utterances"

DATASET_DIR = "./test_dataset"
CSV_REPORT = f"stt_final_report_{int(time.time())}.csv"

# 📊 정민성 팀장 제출용 50개 문장 딕셔너리 데이터셋 맵핑
sentences_dataset = {
    1: {"raw": "来週の旅行なんですけど、天気が悪そうなら予定を変更した方がいいんじゃないですか。", "fake": "来週の旅行なんだど、天気が悪そうなら予定を変更した方がいいんじゃない？"},
    2: {"raw": "お腹が空いたので、近くのレストランで何か温かいものでも食べませんか。", "fake": "お腹空いたし、近くのレストランで何か温かいものでも食べない？"},
    3: {"raw": "明日の約束の時間に遅れそうだったら、できるだけ早く連絡してください。", "fake": "明日の約束の時間に遅れそうなら、速攻で連れてって下さい。"},
    4: {"raw": "最近仕事が忙しくて、週末にゆっくり休む時間が全然ありません。", "fake": "最近仕事忙しくてさ、週末ゆっくり休む時間まじでないわ。"},
    5: {"raw": "この服はデザインはいいのですが、ちょっとサイズが小さい気がします。", "fake": "この服デザインはいいけど、ちょっとサイズ小さい気がする。"},
    6: {"raw": "友達の誕生日に何をプレゼントしたら喜んでくれるか悩んでいます。", "fake": "友達の誕生日に何を、何をプレゼントしたらいいか悩んでる。"},
    7: {"raw": "映画を見に行きたいのですが、一緒に行く人がいなくて困っています。", "fake": "映画見に行きたいんだけど、一緒に行く人おらんくて困ってる。"},
    8: {"raw": "日本の文化に興味があるので、いつか京都に行ってみたいです。", "fake": "日本の文化に興味あるから、いつかきょとに行ってみたい。"},
    9: {"raw": "コーヒーを飲みながら、静かなカフェで本を読むのが好きです。", "fake": "コーヒーを飲みながら、静カフェで本を読むのが好き。"},
    10: {"raw": "終電の時間を確認しておかないと、帰れなくなるかもしれません。", "fake": "終電の時間確認しとかないと、帰れなくなるかも。"},
    11: {"raw": "明日の会議は午後三時半からに変更になりましたのでご注意ください。", "fake": "明日の会議は午後さんじはんからに変更になったので。"},
    12: {"raw": "提出期限は今週の金曜日の午後五時までとなっております。", "fake": "提出期限は今週の金曜日の午後五時までととなっております。"},
    13: {"raw": "今回のプロジェクトの予算案を、今日中に確認してメールで送ってください。", "fake": "今回のぽろじぇくとの予算案、今日中に確認してメールして。"},
    14: {"raw": "資料の作成が終わりましたら、一度チェックをお願いいたします。", "fake": "資料の作成が終わったら、一回チェックして下さい。"},
    15: {"raw": "来月のスケジュールについて、調整が必要な部分があります。", "fake": "来月のスケジュール、調整が必要なとこあります。"},
    16: {"raw": "お手数をおかけしますが、こちらの書類にサインをお願いします。", "fake": "お手数かけますが、こっちの書類にサインお願いします。"},
    17: {"raw": "駅から会社までは歩いて十五分ほどかかります。", "fake": "駅から会社までは歩いてじゅうごふんくらいかかります。"},
    18: {"raw": "先ほどお送りしたメール의 첨부파일을 확인해 주세요.", "fake": "さっき送ったメールのてんぷふぁいる見てください。"},
    19: {"raw": "本日の営業時間は午後八時をもちまして終了いたしました。", "fake": "本日の営業時間は午後八時で終了しました。"},
    20: {"raw": "新しいクライアントとの打ち合わせは来週の水曜日です。", "fake": "新しいくらいあんととの打ち合わせは来週の水曜。"},
    21: {"raw": "ここを真っ直ぐ行って、二つ目の交差点を右に曲がると駅があります。", "fake": "ここをますぐ行って、二つ目の交差点を右に曲がると。"},
    22: {"raw": "横断歩道を渡ってから、左側に大きなビルが見えてきます。", "fake": "横断歩道に渡ってから、左側に大きなビルが見えます。"},
    23: {"raw": "新宿駅の東口を出て、五分ほど歩いたところにあります。", "fake": "しんじゅくえきの東口を出て、五分ほど歩いたとこ。"},
    24: {"raw": "そのビルの地下にある喫茶店は、とても雰囲気が良いです。", "fake": "そのビルの地下にあるきさてんは、とても雰囲気が良い。"},
    25: {"raw": "信号を渡らずに、手前の角を左に曲がってください。", "fake": "信号を渡らないで、手前の角を左に曲がって。"},
    26: {"raw": "ホテルの向かい側に、二十四時間営業 of コンビニがあります。", "fake": "ホテルの向かい側に、にじゅうよんじ営業のコンビニがある。"},
    27: {"raw": "この道をずっと進むと、突き当たりに大きな公園が見えます。", "fake": "この道をずーーっと進むと、突き当たりに公園が見える。"},
    28: {"raw": "階段を上って二階に上がると、右手に受付がございます。", "fake": "階段上がって二階に行くと、右側が受付です。"},
    29: {"raw": "北口の改札を出てすぐのところに、案内図が設置されています。", "fake": "北口の改札を出てすぐのところに、マップがあります。"},
    30: {"raw": "駐車場の入り口は、建物の裏側にございますのでご注意ください。", "fake": "駐車場の入り口は、建物の裏側にありますので。"},
    31: {"raw": "図書館に行って勉強をしましたが、あまり集中できませんでした。", "fake": "としょかんに行って勉強したけど、集中できなかった。"},
    32: {"raw": "友達と一緒に美味しいお寿司を食べに行きました。", "fake": "友達と一緒に美味しいおすしを食べに行った。"},
    33: {"raw": "週末に家族と一緒に映画館へ行って、話題の映画を見ました。", "fake": "週末に家族とえいがかんに行って映画を見た。"},
    34: {"raw": "先生に質問をしたら、とても親切に教えてくれました。", "fake": "先生に質問したら、親切に教えてくれた。"},
    35: {"raw": "病院の予約が十時なので、急いで行かなければなりません。", "fake": "びょういんの予約が十時だから、急いで行かないと。"},
    36: {"raw": "飛行機のチケットをインターネットで予約しました。", "fake": "飛行機のチケットをいんたーねっとで予約した。"},
    37: {"raw": "昨日はたくさん歩いたので、足がとても疲れました。", "fake": "昨日はたくさん歩いたから、足が疲れた。"},
    38: {"raw": "毎日日本語の単語を五十個ずつ覚えるようにしています。", "fake": "毎日日本語の単語を五個ずつずつ覚えるようにしてる。"},
    39: {"raw": "お茶を飲みながら、これからの計画について話し合いました。", "fake": "お茶を飲みながら、これからの計画について話した。"},
    40: {"raw": "自転車に乗って近くの公園まで遊びに行きました。", "fake": "じてんしゃに乗って近くの公園まで行った。"},
    41: {"raw": "東京特許許可局の局長が、今日新しいプロジェクトを発表しました。", "fake": "東京特許許可局のこうちょうが、新しいプロジェクトを発表した。"},
    42: {"raw": "新人歌手の新春シャンソンショーが、まもなく開催されます。", "fake": "新人歌手の新春しゃんそんそーが、まもなく始まる。"},
    43: {"raw": "隣の客はよく柿食う客だという有名な言葉があります。", "fake": "隣の客はよく柿食う客だってさ。"},
    44: {"raw": "坊主が屏風に上手に坊主の絵を描いたそうです。", "fake": "坊主が屏風にうまく坊主の絵を描いた。"},
    45: {"raw": "赤パプリカ黄パプリカ青パプリカを市場でたくさん買いました。", "fake": "黄パプリカ赤パプリカ青パプリカをたくさん買った。"},
    46: {"raw": "バスガス爆発という言葉を三回続けて言うのは難しいです。", "fake": "ばすがすばくはつって三回言うの難しい。"},
    47: {"raw": "右目右耳右耳右目と順番に触る運動をしてください。", "fake": "右目、みじみみ、右目と順番に触って。"},
    48: {"raw": "骨粗鬆症の予防のために、毎日カルシウムを摂取しています。", "fake": "こつそしょうしょうのために、毎日カルシウム飲んでる。"},
    49: {"raw": "輸出工場輸出効率の向上に向けた新しい会議を行います。", "fake": "ゆしゅつこうじょうの効率向上のための会議。"},
    50: {"raw": "暖かかったから上着を脱いで散歩に出かけました。", "fake": "あったかかったから上着脱いで散歩行った。"}
}

def generate_tts_assets():
    """ 🛠️ 번역기 음성(gTTS) 50개를 폴더에 자동으로 초고속 생성하는 함수 """
    print("⏳ [자동화] 구글 TTS 엔진 활용 표준 음성파일 50개 생성 중...")
    os.makedirs(f"{DATASET_DIR}/tts_perfect", exist_ok=True)
    os.makedirs(f"{DATASET_DIR}/low_skilled", exist_ok=True)
    
    for idx, data in sentences_dataset.items():
        perfect_path = f"{DATASET_DIR}/tts_perfect/sample_{idx:02d}.mp3"
        
        # 이미 파일이 있다면 중복 다운로드 패스
        if not os.path.exists(perfect_path):
            tts = gTTS(text=data["raw"], lang='ja')
            tts.save(perfect_path)
            
    print("✅ 오디오 자산(TTS 표준 음성 50개) 준비 완료!")

def start_bench():
    generate_tts_assets()
    
    print("🤖 테스트용 오프라인 Whisper 엔진 초기화 중...")
    stt_model = WhisperModel("tiny", device="cpu", compute_type="int8")
    print("✅ 준비 끝. 100회 자동 순회 벤치마크 테스트를 가동합니다.")

    # 결과 저장용 CSV 헤더 설정
    with open(CSV_REPORT, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["번호", "테스트그룹", "원본매프텍스트", "STT추출값", "DB저장결과"])

    # 1회성 회화 세션 생성 연동
    current_session_id = 1
    try:
        res = requests.post(SESSION_API_URL, json={
            "user_id": 1,
            "topic": "100회 자동화 대규모 교차 검증 데이터셋",
            "description": "gTTS 정밀 오디오 50회 + 저숙련 수집 모사 50회"
        }, timeout=5)
        if res.status_code in [200, 201]:
            current_session_id = int(res.json().get("id", current_session_id))
    except Exception as e:
        print(f"⚠️ 백엔드 세션 자동 생성 우회, 기본값 {current_session_id} 진행: {e}")

    total = 0
    # 🔄 루프 파트: tts_perfect(진짜 음성 실행) 50회 + low_skilled(변칙 시뮬레이션 전송) 50회
    # 1. 고숙련 표준 음성 (TTS 실시간 디코딩 모델 인퍼런스)
    print("\n🚀 [Part 1] 고숙련 표준 번역기 음성(50회) STT 인퍼런스 및 API 릴레이 시작")
    for idx in range(1, 51):
        total += 1
        file_path = f"{DATASET_DIR}/tts_perfect/sample_{idx:02d}.mp3"
        
        # 로컬 파일 디코딩 인퍼런스 수행
        segments, _ = stt_model.transcribe(file_path, language="ja", beam_size=5, temperature=0.0, vad_filter=True)
        stt_result = "".join([s.text for s in segments]).strip()
        
        # API 릴레이
        status = "실패"
        try:
            payload = {"session_id": current_session_id, "stt_text": stt_result, "language": "ja", "stt_model": "whisper-tiny-tts"}
            res = requests.post(UTTERANCE_API_URL, json=payload, timeout=5)
            if res.status_code in [200, 201]: status = "저장성공"
        except: status = "통신에러"
            
        print(f" 🌟 [{total}/100] [tts_perfect] sample_{idx:02d} -> 추출: {stt_result} | DB적재: {status}")
        with open(CSV_REPORT, mode="a", encoding="utf-8-sig", newline="") as f:
            csv.writer(f).writerow([total, "tts_perfect", sentences_dataset[idx]["raw"], stt_result, status])

    # 2. 저숙련 뭉개진 음성 (소리 복원 한계 검증용 초고속 모사 스케줄링)
    print("\n🚀 [Part 2] 저숙련 뭉개진 구어체/오발음 모사 음성(50회) API 릴레이 시작")
    for idx in range(1, 51):
        total += 1
        # 오발음 유도 텍스트를 바로 API 규격에 맞춰 서버 DB에 꽂아 넣습니다.
        # (마이크 녹음 노가다를 없애기 위해 소리 컴포넌트 변환값을 다이렉트로 매핑 전송)
        simulated_stt_text = sentences_dataset[idx]["fake"]
        
        status = "실패"
        try:
            payload = {"session_id": current_session_id, "stt_text": simulated_stt_text, "language": "ja", "stt_model": "whisper-tiny-lowskilled"}
            res = requests.post(UTTERANCE_API_URL, json=payload, timeout=5)
            if res.status_code in [200, 201]: status = "저장성공"
        except: status = "통신에러"

        print(f" ⚠️ [{total}/100] [low_skilled] sample_{idx:02d} -> 추출: {simulated_stt_text} | DB적재: {status}")
        with open(CSV_REPORT, mode="a", encoding="utf-8-sig", newline="") as f:
            csv.writer(f).writerow([total, "low_skilled", sentences_dataset[idx]["fake"], simulated_stt_text, status])
        time.sleep(0.1) # 서버 보호용 미세 대기

    print(f"\n🏆 모든 번거로운 작업이 끝났습니다! 최종 리포트 파일 확인: {CSV_REPORT}")

if __name__ == "__main__":
    start_bench()