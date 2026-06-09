# 📊 일본어 STT 온디바이스 전처리 및 AI 분석 결과 최종 보고서

- **검증 세션 번호:** 1번 세션
- **추출 일시:** 2026-06-03 00:39:49
- **총 분석 대상 발화 수:** 307건
- **분석 파이프라인 AI 엔진:** qwen/qwen3-4b-2507 (RAG 하이브리드 엔진)

--- 

## 📌 발화 샘플 데이터 #1 (ID: 1)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `안녕하세요.` |
| **서버 AI 최종 교정본** | **안녕하세요.** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | False |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 일본어 문장으로 판단하기 어려운 입력입니다. 일본어 문장을 다시 입력해 주세요.
- **일본어 해설:** 日本語の文として判断しにくい入力です。日本語の文をもう一度入力してください。

--- 

## 📌 발화 샘플 데이터 #2 (ID: 2)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `始めまして` |
| **서버 AI 최종 교정본** | **始めまして** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[初め]
- matched_form: 始め
- reading: はじめ
- meaning: beginning, start
- level: N5
```

--- 

## 📌 발화 샘플 데이터 #3 (ID: 3)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `언니 좋아` |
| **서버 AI 최종 교정본** | **언니 좋아** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | False |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 일본어 문장으로 판단하기 어려운 입력입니다. 일본어 문장을 다시 입력해 주세요.
- **일본어 해설:** 日本語の文として判断しにくい入力です。日本語の文をもう一度入力してください。

--- 

## 📌 발화 샘플 데이터 #4 (ID: 4)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `こんにちは` |
| **서버 AI 최종 교정본** | **こんにちは** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | False |
| **AI 모델 확신도** | 90.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 자연스러운 일본어 인사 표현입니다. 별도의 교정이 필요하지 않습니다.
- **일본어 해설:** 自然な日本語のあいさつ表現です。特に修正する必要はありません。

--- 

## 📌 발화 샘플 데이터 #5 (ID: 5)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ライシーの力なんですけど、大きい側はそのまま` |
| **서버 AI 최종 교정본** | **ライシーの力なんですけど、大きい側はそのまま** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미도 명확하고 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味も明確で文法的に問題ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[大きい]
- matched_form: 大きい
- reading: おおきい
- meaning: big, large
- level: N5

[その]
- matched_form: その
- reading: その
- meaning: that
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

--- 

## 📌 발화 샘플 데이터 #6 (ID: 6)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `次回` |
| **서버 AI 최종 교정본** | **次回** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | False |
| **AI 모델 확신도** | 85.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 단어 또는 짧은 발화로 보여 전체 문장 교정은 어렵습니다. 완전한 문장으로 입력하면 더 정확히 분석할 수 있습니다.
- **일본어 해설:** 単語または短い発話のため、文全体の添削は難しいです。完全な文で入力すると、より正確に分析できます。

--- 

## 📌 발화 샘플 데이터 #7 (ID: 7)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `来週の旅行なんですけど、天気が悪そうなら予定を変更した方がいいんじゃないですか?` |
| **서버 AI 최종 교정본** | **来週の旅行なんですけど、天気が悪そうなら予定を変更した方がいいんじゃないですか?** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로도 올바릅니다. 오류가 없습니다.
- **일본어 해설:** この文は自然で、文法的に正しいです。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[来週]
- matched_form: 来週
- reading: らいしゅう
- meaning: next week
- level: N5

[旅行]
- matched_form: 旅行
- reading: りょこう
- meaning: travel, trip
- level: N5

[天気]
- matched_form: 天気
- reading: てんき
- meaning: weather
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5

[方]
- matched_form: 方
- reading: かた
- meaning: -- honorific form for 人 (ひと) --; way of doing
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5

[じゃ]
- matched_form: じゃ
- reading: じゃ; じゃあ
- meaning: well, well then
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #8 (ID: 17)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `来週の旅行なんですけど、天気が悪そうなら予定を変更した方がいいんじゃないですか。` |
| **서버 AI 최종 교정본** | **来週の旅行なんですけど、天気が悪そうなら予定を変更した方がいいんじゃないですか。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로도 올바릅니다. 의미가 명확하며, 일본어 회화 표현으로 적절합니다.
- **일본어 해설:** この文は自然で、文法的に正しいです。意味は明確で、日本語の会話表現として適切です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[来週]
- matched_form: 来週
- reading: らいしゅう
- meaning: next week
- level: N5

[旅行]
- matched_form: 旅行
- reading: りょこう
- meaning: travel, trip
- level: N5

[天気]
- matched_form: 天気
- reading: てんき
- meaning: weather
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5

[方]
- matched_form: 方
- reading: かた
- meaning: -- honorific form for 人 (ひと) --; way of doing
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5

[じゃ]
- matched_form: じゃ
- reading: じゃ; じゃあ
- meaning: well, well then
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #9 (ID: 18)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `おなかがすいたので、近くのレストランで何かあたたかいものでも食べませんか。` |
| **서버 AI 최종 교정본** | **おなかがすいたので、近くのレストランで何かあたたかいものでも食べませんか。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 문법적으로 자연스럽고, 의미도 명확합니다. 오류가 없습니다.
- **일본어 해설:** 文法的に自然で、意味も明確です。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[近く]
- matched_form: 近く
- reading: ちかく
- meaning: nearby; in the neighborhood
- level: N5

[レストラン]
- matched_form: レストラン
- reading: レストラン
- meaning: restaurant
- level: N5

[何]
- matched_form: 何
- reading: なん; なに
- meaning: what
- level: N5

[でも]
- matched_form: でも
- reading: でも
- meaning: but, however
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #10 (ID: 19)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `明日の役底の時間におくれそうだったら、できるだけ早く連絡してください。` |
| **서버 AI 최종 교정본** | **明日の役目時間におくれそうだったら、できるだけ早く連絡してください。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미상 오류가 없습니다. '役底'는 '役目'로 교정되었지만, 이는 오류가 아니라 의미상 더 자연스러운 표현입니다. STT 인식 오류로 인한 '役底'의 오류는 문맥상 '役目'로 수정하는 것이 적절합니다.
- **일본어 해설:** この文は自然な日本語です。文法や意味上の誤りはありません。「役底」は「役目」に修正されましたが、これは文脈上より自然な表現です。STT認識の誤りによる「役底」の誤りは、「役目」として修正するのが適切です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[明日]
- matched_form: 明日
- reading: あした
- meaning: tomorrow
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5

[できる]
- matched_form: できる
- reading: できる
- meaning: to be able to (to accomplish)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #11 (ID: 20)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `最近仕事が忙しくて、週末にゆっくり休む時間が全然ありません。` |
| **서버 AI 최종 교정본** | **最近仕事が忙しくて、週末にゆっくり休む時間が全然ありません。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미도 명확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味も明確で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[仕事]
- matched_form: 仕事
- reading: しごと
- meaning: work, job, occupation, employment
- level: N5

[休む]
- matched_form: 休む
- reading: やすむ
- meaning: to rest, to have a break, to get time off
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #12 (ID: 21)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `この服はデザインはいいのですが、ちょっとサイズが小さい気がします。` |
| **서버 AI 최종 교정본** | **この服のデザインはいいのですが、ちょっとサイズが小さい気がします。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[この]
- matched_form: この
- reading: この
- meaning: this
- level: N5

[服]
- matched_form: 服
- reading: ふく
- meaning: clothes
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5

[ちょっと]
- matched_form: ちょっと
- reading: ちょっと
- meaning: a little, somewhat; just a little, somewhat
- level: N5

[小さい]
- matched_form: 小さい
- reading: ちいさい
- meaning: small, little
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #13 (ID: 22)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `友達の誕生日に何をプレゼントしたら喜んでくれるか悩んでいます。` |
| **서버 AI 최종 교정본** | **友達の誕生日に何をプレゼントしたら喜んでくれるか悩んでいます。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로 올바릅니다. 의미도 명확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で、文法的に正しいです。意味も明確で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[友達]
- matched_form: 友達
- reading: ともだち
- meaning: friend
- level: N5

[誕生日]
- matched_form: 誕生日
- reading: たんじょうび
- meaning: birthday
- level: N5

[何]
- matched_form: 何
- reading: なん; なに
- meaning: what
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #14 (ID: 23)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `映画を見に行きたいのですが、一緒に行く人がいなくて困っています。` |
| **서버 AI 최종 교정본** | **映画を見に行きたいのですが、一緒に行く人がいなくて困っています。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[映画]
- matched_form: 映画
- reading: えいが
- meaning: movie, film
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5

[行く]
- matched_form: 行く
- reading: いく; ゆく
- meaning: to go
- level: N5

[人]
- matched_form: 人
- reading: ひと
- meaning: man, person
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_008] 〜たいです 희망 표현
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + たいです
- description_ko: 하고 싶은 일을 말할 때 동사의 ます형 어간에 たいです를 붙이는 경우가 많다.
- reference_examples: 食べたいです, 行きたいです
- possible_focus: 희망 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 희망 표현이 아닌 단순 서술문을 억지로 たい 형태로 해석하지 않는다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #15 (ID: 24)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `日本の文化に興味があるので、いつかきょうとに行ってみたいです。` |
| **서버 AI 최종 교정본** | **日本の文化に興味があるので、いつかきょうとに行ってみたいです。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 문법적으로 자연스럽고 의미가 명확합니다. 오류가 없습니다.
- **일본어 해설:** この文は文法的に自然で意味が明確です。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[いつ]
- matched_form: いつ
- reading: いつ
- meaning: when
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_008] 〜たいです 희망 표현
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + たいです
- description_ko: 하고 싶은 일을 말할 때 동사의 ます형 어간에 たいです를 붙이는 경우가 많다.
- reference_examples: 食べたいです, 行きたいです
- possible_focus: 희망 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 희망 표현이 아닌 단순 서술문을 억지로 たい 형태로 해석하지 않는다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #16 (ID: 25)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `コーヒーを飲みながら、静かなカフェで本を読むのが好きです。` |
| **서버 AI 최종 교정본** | **コーヒーを飲みながら、静かなカフェで本を読むのが好きです。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미도 명확하며, 일본어 학습자에게 적절한 표현입니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味も明確で、日本語学習者にとって適切な表現です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[コーヒー]
- matched_form: コーヒー
- reading: コーヒー
- meaning: coffee
- level: N5

[静か]
- matched_form: 静か
- reading: しずか
- meaning: quiet, calm
- level: N5

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[読む]
- matched_form: 読む
- reading: よむ
- meaning: to read
- level: N5

[好き]
- matched_form: 好き
- reading: すき
- meaning: liking, fondness, love
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #17 (ID: 26)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `集電の時間を確認しておかないと、変えれなくなるかもしれません。` |
| **서버 AI 최종 교정본** | **集電の時間を確認しておかないと、変えることができなくなるかもしれません。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 동사 활용 형태가 부자연스러워 올바른 활용 형태로 수정했습니다.
- **일본어 해설:** 動詞の活用形が不自然だったため、正しい活用形に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5

[なる]
- matched_form: なる
- reading: なる
- meaning: to become
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #18 (ID: 27)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `明日の会議は午後3時半からに変更になりましたのでご注意ください` |
| **서버 AI 최종 교정본** | **明日の会議は午後3時半からに変更になりましたのでご注意ください** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[明日]
- matched_form: 明日
- reading: あした
- meaning: tomorrow
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5

[半]
- matched_form: 半
- reading: はん
- meaning: half (e.g., にじはん | half-past two)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #19 (ID: 28)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `提出期限は今週の金曜日の午後5時までとなっております` |
| **서버 AI 최종 교정본** | **提出期限は今週の金曜日の午後5時までとなっております** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 문제 없습니다.
- **일본어 해설:** この文は自然な日本語で、文法や意味において問題ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[今週]
- matched_form: 今週
- reading: こんしゅう
- meaning: this week
- level: N5

[金曜日]
- matched_form: 金曜日
- reading: きんようび
- meaning: Friday
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

--- 

## 📌 발화 샘플 데이터 #20 (ID: 29)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `今回のプロジェクトの予算案を、共重に確認してメールで送ってください。` |
| **서버 AI 최종 교정본** | **今回のプロジェクトの予算案を、共に確認してメールで送ってください。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 필요한 조사가 생략된 부분이 있어 문장 구조가 부자연스러웠습니다.
- **일본어 해설:** 文の中で必要な助詞が省略されている部分があり、文の構造が不自然でした。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[今]
- matched_form: 今
- reading: いま
- meaning: now
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #21 (ID: 30)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `資料の作成が終わりましたら、一度チェックをお願い致します。` |
| **서버 AI 최종 교정본** | **資料の作成が終わりましたら、一度チェックをお願いいたします。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미상 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味上の問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[一]
- matched_form: 一
- reading: いち
- meaning: one
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #22 (ID: 31)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `来月のスケジュールについて、調整が必要な部分があります。` |
| **서버 AI 최종 교정본** | **来月のスケジュールについて、調整が必要な部分があります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 교정이 필요하지 않습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[来月]
- matched_form: 来月
- reading: らいげつ
- meaning: next month
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #23 (ID: 32)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お手数をおかけしますが、こちらの処理にサインをお願いします。` |
| **서버 AI 최종 교정본** | **お手数をおかけしますが、こちらの処理にサインをお願いします。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로 올바릅니다. 요청 표현 'サインをお願いします'도 적절히 사용되어 있습니다.
- **일본어 해설:** 文は自然で、文法的に正しいです。「サインをお願いします」というお願い表現も適切に使用されています。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[こちら]
- matched_form: こちら
- reading: こちら
- meaning: this person (polite); this way (polite)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #24 (ID: 33)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `駅から回車までは歩いて15分ほどかかります` |
| **서버 AI 최종 교정본** | **駅から回車までは歩いて15分ほどかかります** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[駅]
- matched_form: 駅
- reading: えき
- meaning: station
- level: N5

[車]
- matched_form: 車
- reading: くるま
- meaning: car, vehicle
- level: N5

[では]
- matched_form: では
- reading: では
- meaning: then, well, so
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

--- 

## 📌 발화 샘플 데이터 #25 (ID: 34)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `先ほどお送りしたメールイケオンブパイルール、ファジン・ハイ・ジュスティオ` |
| **서버 AI 최종 교정본** | **先ほどお送りしたメールのイケオンブパイルール、ファジン・ハイ・ジュスティオ** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 'メール'과 'イケオンブパイルール' 사이에 조사를 추가해야 합니다. 'メールの'로 수정하여 자연스러운 문장을 만들 수 있습니다.
- **일본어 해설:** 「メール」と「イケオンブパイルール」の間に助詞「の」を追加すべきです。これにより自然な文になります。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[先]
- matched_form: 先
- reading: さき
- meaning: future; recent, previous
- level: N5
```

--- 

## 📌 발화 샘플 데이터 #26 (ID: 35)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `本日の営業時間は午後8時を持ちまして終了いたしました。` |
| **서버 AI 최종 교정본** | **本日の営業時間は午後8時までです。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미상 자연스럽지 않습니다. '終了いたしました'는 과거형으로 표현되었지만, 현재의 운영 시간을 말하는 상황에서는 현재형이 더 자연스럽습니다. 'までです'로 교정하였습니다.
- **일본어 해설:** この文は意味的に自然ではありません。営業時間について述べているため、過去形「終了いたしました」は不自然です。現在形「までです」に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #27 (ID: 36)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新しいクライアントとの打ち合わせは来週の水曜日です。` |
| **서버 AI 최종 교정본** | **新しいクライアントとの打ち合わせは来週の水曜日です。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5

[来週]
- matched_form: 来週
- reading: らいしゅう
- meaning: next week
- level: N5

[水曜日]
- matched_form: 水曜日
- reading: すいようび
- meaning: Wednesday
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_002] 名詞 + を + 食べる/飲む
- rule_type: reference
- level: N5
- pattern: 名詞 + を + 食べる/飲む
- description_ko: 먹거나 마시는 대상에는 조사 を를 붙이는 경우가 일반적이다.
- reference_examples: 水を飲みます, ご飯を食べます
- possible_focus: 목적어 표현, 조사 を 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확한 단편 발화는 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[word_choice_error] 단어 선택 오류
- description_ko: 동사와 명사의 의미 조합이 어색하거나 다른 단어가 더 적절할 가능성이 있는 경우이다.
- related_focus: 단어 선택, 동사와 목적어의 의미 관계
- reference_examples:
  - observed: 水を食べます
    reference: 水を飲みます
  - observed: ラーメンを飲みます
    reference: ラーメンを食べます
- overcorrection_note: 비유적 표현이나 특수 문맥일 수 있으므로, 단어 조합만 보고 기계적으로 오류 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #28 (ID: 37)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ここをまっすぐ行って、2つ目の交差点を右に曲がると駅があります。` |
| **서버 AI 최종 교정본** | **ここをまっすぐ行って、2つ目の交差点を右に曲がると駅があります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 정확합니다.
- **일본어 해설:** この文は自然な日本語で、文法や意味ともに正確です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ここ]
- matched_form: ここ
- reading: ここ
- meaning: here, this place
- level: N5

[まっすぐ]
- matched_form: まっすぐ
- reading: まっすぐ
- meaning: straight (ahead), direct
- level: N5

[目]
- matched_form: 目
- reading: め
- meaning: eye(s)
- level: N5

[交差点]
- matched_form: 交差点
- reading: こうさてん
- meaning: intersection
- level: N5

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5

[駅]
- matched_form: 駅
- reading: えき
- meaning: station
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #29 (ID: 38)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `オーダンホードを渡ってから左側に大きなビルが見えてきます。` |
| **서버 AI 최종 교정본** | **オーダンホードを渡ってから左側に大きなビルが見えてきます。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[左]
- matched_form: 左
- reading: ひだり
- meaning: left hand side
- level: N5

[大きな]
- matched_form: 大きな
- reading: おおきな
- meaning: big
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #30 (ID: 39)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新宿平均の東口を出て、5分ほど歩いたところにあります。` |
| **서버 AI 최종 교정본** | **新宿平均の東口を出て、5分ほど歩いたところにあります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 교정이 필요하지 않습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[東]
- matched_form: 東
- reading: ひがし
- meaning: east
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #31 (ID: 40)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `そのびるの近に歩きさ点は、とても吹息が良いです。` |
| **서버 AI 최종 교정본** | **その近くで歩き始めるのは、とても吹き息が良いです。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '歩きさ点'은 자연스러운 표현이 아니며, '歩き始める'이 더 적절합니다. 또한 '歩きさ点' 뒤에 'で'가 필요하지만, '歩きさ点'이 조사와 함께 사용되는 표현이 아니므로 오류입니다.
- **일본어 해설:** 「歩きさ点」は自然な表現ではありません。正しい表現は「歩き始める」です。また、「歩きさ点」の後に「で」が必要ですが、この表現は文法的に不自然です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[その]
- matched_form: その
- reading: その
- meaning: that
- level: N5

[とても]
- matched_form: とても
- reading: とても
- meaning: very (much), greatly, exceedingly
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #32 (ID: 41)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `信号を当たらずに、手前のつの左に曲がってください。` |
| **서버 AI 최종 교정본** | **信号を渡らず、手前の左に曲がってください。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '当たらずに'는 자연스러운 표현이 아니며, '渡らず'로 교정해야 합니다. '当たる'은 '신호를 타는 것'을 의미하지 않으며, '信号を渡る'이 더 적절합니다.
- **일본어 해설:** 「当たらずに」は自然な表現ではありません。「信号を渡らず」が適切です。「当たる」は「信号をタッチする」という意味ではなく、「信号を渡す」という意味になります。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[前]
- matched_form: 前
- reading: まえ
- meaning: before, in front
- level: N5

[左]
- matched_form: 左
- reading: ひだり
- meaning: left hand side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #33 (ID: 42)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ホテルの迎え側に、24時間平行をおぶコンビニがあります。` |
| **서버 AI 최종 교정본** | **ホテルの迎え側に、24時間営業のコンビニがあります。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '平行'는 적절한 표현이 아니며, '24시간営業'가 더 자연스러운 표현입니다. '平行'는 오류로 판단되며, '24時間営業'로 교정했습니다.
- **일본어 해설:** 文に「平行」は適切な表現ではなく、「24時間営業」が自然な表現です。この誤りを修正し、「24時間営業」に変更しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ホテル]
- matched_form: ホテル
- reading: ホテル
- meaning: hotel
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #34 (ID: 43)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `この道をずっと進むと、付き当たりに動きな公園が見えます。` |
| **서버 AI 최종 교정본** | **この道をずっと進むと、付近の公園が見えます。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '付き当たり'는 자연스러운 표현이 아니며, '付近'이 더 적절합니다. '付き当たりに動きな公園'은 문법적으로도 부적절하며, 조사 오류가 포함되어 있습니다.
- **일본어 해설:** 「付き当たりに動きな公園」は自然な表現ではなく、「付近の公園」という表現が適切です。文法的にも誤りがあり、調節が必要です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[この]
- matched_form: この
- reading: この
- meaning: this
- level: N5

[道]
- matched_form: 道
- reading: みち
- meaning: road, street; way, directions
- level: N5

[公園]
- matched_form: 公園
- reading: こうえん
- meaning: a park
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #35 (ID: 44)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `階段を登って2階に上がると右手に受け付けがございます。` |
| **서버 AI 최종 교정본** | **階段を登って2階に上がると、右手に受け付けがございます。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장의 의미는 자연스럽지만, '右手に受け付けがございます'는 표현이 부자연스럽습니다. '右手に受け付け'는 '오른쪽에 있는 수용 장소'를 의미하는 것이 아니라, '오른쪽에 있는 수용 장소가 있습니다'라는 의미로 해석되기 때문에, 조사가 잘못 사용된 것으로 판단됩니다. '右手に'는 '오른쪽에'를 의미하지만, '受け付け'는 '수용 장소'를 의미하며, 이 조합은 문맥상 어색합니다. '右側に' 또는 '右に'와 함께 '受け付け'가 적절한 표현이 되어야 합니다.
- **일본어 해설:** 文の意味は自然ですが、「右手に受け付けがございます」という表現は不自然です。「右手に」は「右側に」を意味し、「受け付け」は「受付場所」を意味するため、この組み合わせは文脈上不自然です。より自然な表現は「右側に受付があります」または「右に受付があります」です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[階段]
- matched_form: 階段
- reading: かいだん
- meaning: stairs
- level: N5

[上]
- matched_form: 上
- reading: うえ
- meaning: above (up, top, etc.), over, on top of
- level: N5

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #36 (ID: 45)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `北口の開札を出てすぐのところに、案内図が設置されています。` |
| **서버 AI 최종 교정본** | **北口の開札を出てすぐのところに、案内図が設置されています。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[北]
- matched_form: 北
- reading: きた
- meaning: north
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #37 (ID: 46)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `中車上の入り口は、縦物の裏側にございますのでご注意ください。` |
| **서버 AI 최종 교정본** | **中車の入り口は、縦物の裏側にございますのでご注意ください。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 85.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '上'가 '車の上'로 해석될 수 있지만, '車上の入り口'는 의미상 자연스럽지 않습니다. '車の上'는 '차 위'를 의미하지만, '車上の入り口'는 문맥상 어색합니다. '車の入り口'로 수정하면 자연스러운 표현이 됩니다. '縦物の裏側'는 '수직 물건의 뒷쪽'으로 해석되며, 이 표현은 불명확합니다. '車の入り口'와 '車の裏側'의 조합이 더 자연스럽습니다.
- **일본어 해설:** 「中車上の入り口」は文脈的に不自然です。『車の上』は『車の上』を意味するが、『車上の入り口』という表現は不自然です。『車の入り口』に修正すると自然な表現になります。また、『縦物の裏側』は『縦の物の裏側』と解釈され、文脈的に不明確です。『車の入り口』と『車の裏側』の組み合わせが自然です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[中]
- matched_form: 中
- reading: なか
- meaning: inside, middle, among
- level: N5

[車]
- matched_form: 車
- reading: くるま
- meaning: car, vehicle
- level: N5

[上]
- matched_form: 上
- reading: うえ
- meaning: above (up, top, etc.), over, on top of
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5

[物]
- matched_form: 物
- reading: もの
- meaning: thing (concrete object)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #38 (ID: 47)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `徒職案に行って勉強しましたが、あまり集中できませんでした。` |
| **서버 AI 최종 교정본** | **徒職案に行って勉強しましたが、あまり集中できませんでした。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미도 명확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味も明確で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[勉強]
- matched_form: 勉強
- reading: べんきょう (する)
- meaning: study
- level: N5

[中]
- matched_form: 中
- reading: なか
- meaning: inside, middle, among
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 6 (keyword_match_count=4, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #39 (ID: 48)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `友達と一緒においしいをずしを食べに行きました。` |
| **서버 AI 최종 교정본** | **友達と一緒においしいずしを食べに行きました。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문맥상 사용된 조사가 적절하지 않아 더 자연스러운 조사로 수정했습니다.
- **일본어 해설:** 文脈上、使われている助詞が適切ではなかったため、より自然な助詞に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[友達]
- matched_form: 友達
- reading: ともだち
- meaning: friend
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #40 (ID: 49)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `週末に家族と一緒に映画観へ行って、話題の映画を見ました。` |
| **서버 AI 최종 교정본** | **週末に家族と一緒に映画を見ました。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 올바르고, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味ともに正しいため、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[家族]
- matched_form: 家族
- reading: かぞく
- meaning: family, members of a family
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5

[映画]
- matched_form: 映画
- reading: えいが
- meaning: movie, film
- level: N5

[話]
- matched_form: 話
- reading: はなし
- meaning: talk (chat), story
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #41 (ID: 50)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `先生に質問をしたら、とても親切に教えてくれました。` |
| **서버 AI 최종 교정본** | **先生に質問をしたら、とても親切に教えてくれました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現が正確であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[先生]
- matched_form: 先生
- reading: せんせい
- meaning: teacher, professor; master; doctor
- level: N5

[質問]
- matched_form: 質問
- reading: しつもん
- meaning: question, inquiry
- level: N5

[とても]
- matched_form: とても
- reading: とても
- meaning: very (much), greatly, exceedingly
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #42 (ID: 51)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `病院の予約が10時なので、急いで行かなければなりません。` |
| **서버 AI 최종 교정본** | **病院の予約が10時なので、急いで行かなければなりません。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미가 올바르며 교정이 필요 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味において誤りはありません。修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[病院]
- matched_form: 病院
- reading: びょういん
- meaning: hospital
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #43 (ID: 52)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `飛行機のチケットをインターネットで予約しました。` |
| **서버 AI 최종 교정본** | **飛行機のチケットをインターネットで予約しました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現が正確で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[飛行機]
- matched_form: 飛行機
- reading: ひこうき
- meaning: airplane
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #44 (ID: 53)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `機能はたくさんあるいたので、足がとても疲れました。` |
| **서버 AI 최종 교정본** | **機能はたくさんあるので、足がとても疲れました。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 'たくさんあるいた'는 표현이 자연스럽지 않습니다. 'たくさんある'으로 수정하고, 'いた'는 조사가 잘못 사용되었으며, '足がとても疲れました'는 문맥상 자연스러운 표현입니다.
- **일본어 해설:** 「たくさんあるいた」という表現は自然ではありません。正しい表現は「たくさんある」です。「いた」は誤った助詞の使用です。また、「足がとても疲れました」は文脈的に自然な表現です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[足]
- matched_form: 足
- reading: あし
- meaning: foot; leg
- level: N5

[とても]
- matched_form: とても
- reading: とても
- meaning: very (much), greatly, exceedingly
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #45 (ID: 54)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `毎日日本語の単語を50個ずつ覚えるようにしています` |
| **서버 AI 최종 교정본** | **毎日日本語の単語を50個ずつ覚えるようにしています** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로도 올바릅니다. 오류가 없습니다.
- **일본어 해설:** この文は自然で、文法的にも正しいです。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[毎日]
- matched_form: 毎日
- reading: まいにち
- meaning: every day
- level: N5

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[覚える]
- matched_form: 覚える
- reading: おぼえる
- meaning: to learn, to commit to memory, to remember, to memorize
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #46 (ID: 55)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お茶を飲みながら、これからの計画について話し合いました。` |
| **서버 AI 최종 교정본** | **お茶を飲みながら、これからの計画について話し合いました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[お茶]
- matched_form: お茶
- reading: おちゃ
- meaning: (green) tea
- level: N5

[これ]
- matched_form: これ
- reading: これ
- meaning: this one
- level: N5

[話]
- matched_form: 話
- reading: はなし
- meaning: talk (chat), story
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #47 (ID: 56)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `自転車に乗って近くの公園まで遊びに行きました。` |
| **서버 AI 최종 교정본** | **自転車に乗って近くの公園まで遊びに行きました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미가 올바르며 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味において誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[自転車]
- matched_form: 自転車
- reading: じてんしゃ
- meaning: bicycle
- level: N5

[近く]
- matched_form: 近く
- reading: ちかく
- meaning: nearby; in the neighborhood
- level: N5

[公園]
- matched_form: 公園
- reading: こうえん
- meaning: a park
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #48 (ID: 57)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `東京都局局局長が、今日は新しいプロジェクトを発表しました。` |
| **서버 AI 최종 교정본** | **東京都局の長が、今日は新しいプロジェクトを発表しました。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '東京都局局局長'은 중복된 '局'가 있어 자연스럽지 않습니다. '東京都局の長'으로 수정하여 자연스러운 표현으로 바꾸었습니다.
- **일본어 해설:** 文に「東京都局局局長」という重複した表現があり、自然な表現ではありません。正しい表現として「東京都局の長」に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[東]
- matched_form: 東
- reading: ひがし
- meaning: east
- level: N5

[今日]
- matched_form: 今日
- reading: きょう
- meaning: today, this day
- level: N5

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_003] 今日 + は
- rule_type: soft_reference
- level: N5
- pattern: 今日 + は
- description_ko: 今日를 문장의 화제로 사용할 때 は를 붙여 今日は 형태로 쓰는 경우가 있다.
- reference_examples: 今日は学校に行きました
- possible_focus: 화제 표현, は 사용 여부, 자연스러운 문장 흐름
- possible_error_types: unnatural_expression
- overcorrection_note: 今日 뒤에 は가 없다고 해서 항상 오류는 아니다. 의미가 자연스럽다면 교정보다는 더 자연스러운 표현 제안으로만 다룬다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #49 (ID: 58)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新銀化州の新瞬産村省がまもなく開催されます。` |
| **서버 AI 최종 교정본** | **新銀化州の新瞬産村省がまもなく開催されます。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 65.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '村省'라는 표현이 자연스럽지 않으며, '村'과 '省'가 함께 사용된 것은 일반적이지 않습니다. '村'은 마을을 의미하지만, '省'는 행정 기관을 의미하므로, 의미가 혼란스럽습니다. '瞬産村'이라는 단어도 존재하지 않으며, 오류가 있을 가능성이 높습니다. 그러나 문장 구조와 문법은 자연스럽지 않지만, 전체 의미를 바꾸지 않고 최소한으로 교정할 수 있는 범위에서 조사 오용을 판단합니다.
- **일본어 해설:** 文に「村省」という表現は自然ではありません。『村』は村を意味し、『省』は行政機関を意味するため、両者が一緒に使われることは一般的ではありません。「瞬産村」という語も存在せず、意味が混乱しています。しかし、文法構造や意味を変えることなく、最も最小限の修正として調査誤用を判断しています。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[村]
- matched_form: 村
- reading: むら
- meaning: village
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #50 (ID: 59)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `となりの客はよく書きく客だという有名な言葉があります。` |
| **서버 AI 최종 교정본** | **となりの客はよく書き手の客だという有名な言葉があります。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '書きく'는 '書き手'로 오류가 있었고, '書き手'는 '글을 쓰는 사람'을 의미하므로 자연스러운 표현입니다. '書きく'은 잘못된 형태로, '書き手'로 교정하였습니다.
- **일본어 해설:** 文に「書きく」は誤りであり、「書き手」に修正しました。これは「文章を書く人」を意味するため、文脈に自然です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[よく]
- matched_form: よく
- reading: よく
- meaning: frequently, often (much); well, skillfully
- level: N5

[有名]
- matched_form: 有名
- reading: ゆうめい
- meaning: famous
- level: N5

[言葉]
- matched_form: 言葉
- reading: ことば
- meaning: language; word(s); expression(s)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #51 (ID: 60)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `坊図が病部に上手に坊図の絵を描いたそうです。` |
| **서버 AI 최종 교정본** | **坊図が病部で上手に絵を描いたそうです。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '病部に'는 '病部で'로 바꾸어야 합니다. '病部'는 장소이므로 'で'가 필요하며, 'に'는 위치를 나타내는 조사로 사용하면 의미가 틀립니다.
- **일본어 해설:** 文の「病部に」は「病部で」に修正すべきです。「病部」は場所であるため、「で」が必要で、「に」は場所を表す助詞として使用すると意味が違います。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[上手]
- matched_form: 上手
- reading: じょうず
- meaning: be good at, skillful
- level: N5

[絵]
- matched_form: 絵
- reading: え
- meaning: a painting; a picture; a drawing
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #52 (ID: 61)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `赤パプリカキパプリカをシジョーでたくさん買いました` |
| **서버 AI 최종 교정본** | **赤いパプリカをショーでたくさん買いました** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문맥상 사용된 조사가 적절하지 않아 더 자연스러운 조사로 수정했습니다.
- **일본어 해설:** 文脈上、使われている助詞が適切ではなかったため、より自然な助詞に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[赤]
- matched_form: 赤
- reading: あか
- meaning: red
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #53 (ID: 62)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `バスがすばくはちという言葉を3回続けていうのは難しいです。` |
| **서버 AI 최종 교정본** | **バスがすばくはちという言葉を3回続けて言うのは難しいです。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 'いう'이 '言う'으로 교정되어야 하며, 'いう'은 '言葉'를 목적어로 사용할 때 적절하지 않습니다. '言う'이 더 자연스럽습니다.
- **일본어 해설:** 文では「いう」が「言う」に修正すべきです。「言葉」を目的語として使う場合、「言う」が自然です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[バス]
- matched_form: バス
- reading: バス
- meaning: bus; bath; bass
- level: N5

[言葉]
- matched_form: 言葉
- reading: ことば
- meaning: language; word(s); expression(s)
- level: N5

[難しい]
- matched_form: 難しい
- reading: むずかしい
- meaning: difficult
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #54 (ID: 63)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `右目右目右目と順番に触る運動をしてください` |
| **서버 AI 최종 교정본** | **右目を順番に触る運動をしてください** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '右目右目右目'는 반복되어 있으며, 의미상 자연스러운 표현이 아닙니다. '右目'을 한 번만 사용하고, 조사 'を'를 추가하여 문법적으로 자연스러운 문장을 만들었습니다.
- **일본어 해설:** 文に「右目右目右目」と繰り返し出現しており、意味が自然ではありません。一度の「右目」に「を」を加えて、文法的に自然な表現に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5

[目]
- matched_form: 目
- reading: め
- meaning: eye(s)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #55 (ID: 64)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `こつそ少少の予防のために、前に使えるシュームを接種しています。` |
| **서버 AI 최종 교정본** | **こっちの少しだけの予防のために、前に使えるシュームを接種しています。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 'こつそ少少'는 자연스러운 표현이 아니며, 'こっちの少しだけ'으로 교정하였습니다. '前に'은 '前に'이 아니라 'こっちの'와 함께 사용하는 것이 더 자연스러운 표현입니다.
- **일본어 해설:** 「こつそ少少」は自然な表現ではなく、「こっちの少しだけ」として修正しました。「前に」は「こっちの」に合わせて使用するのが自然です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[前]
- matched_form: 前
- reading: まえ
- meaning: before, in front
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #56 (ID: 65)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `優質工場、優質工率の工場に向けた新しい会議を行います。` |
| **서버 AI 최종 교정본** | **新しい優質工場に向けた会議を行います。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '優質工場、優質工率の工場'라는 표현은 의미상 모호하며, '優質工場'만을 사용하는 것이 자연스럽습니다. 또한 'に向けた'보다 'に向けた会議'의 표현이 더 자연스러우며, 조사 'に'가 잘못 사용된 것으로 판단됩니다.
- **일본어 해설:** 「優質工場、優質工率の工場」という表現は意味が不明確であり、「優質工場」のみが自然です。また「に向けた」は「に向けた会議」という表現の方が自然です。文法的に不自然な表現が含まれており、調節が必要です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #57 (ID: 66)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `あたたかかったから上げを抜いて3本に出かけました` |
| **서버 AI 최종 교정본** | **あたたかかったから、上を抜いて3本に出かけました** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '上げ'가 '上'로 교정되었으며, '上を抜いて'는 자연스러운 표현이지만, '上げ'는 '上'를 의미하는 조사로 사용하는 경우가 적습니다. '上'가 더 적절한 표현입니다.
- **일본어 해설:** 文に「上げ」が「上」に修正され、「上を抜いて」という表現は自然ですが、「上げ」は「上」を意味する表現として不自然です。正しい表現は「上」です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[上]
- matched_form: 上
- reading: うえ
- meaning: above (up, top, etc.), over, on top of
- level: N5

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #58 (ID: 67)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `来週の旅行なんだど、天気が悪そうなら予定を変更した方がいいんじゃない？` |
| **서버 AI 최종 교정본** | **来週の旅行が悪そうなら、予定を変更した方がいいんじゃない？** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '天気が悪そうなら'의 '方'이 불필요하게 사용되어 있으며, 'が'가 더 자연스러운 조사입니다. '天気'과 '悪そう' 사이에 'が'를 추가하면 문법적으로 더 자연스러워집니다.
- **일본어 해설:** 文の「天気が悪そうなら」における「方」の使用は不要であり、「が」がより自然な表現です。天気と悪そうの間に「が」を加えることで文法的に自然になります。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[来週]
- matched_form: 来週
- reading: らいしゅう
- meaning: next week
- level: N5

[旅行]
- matched_form: 旅行
- reading: りょこう
- meaning: travel, trip
- level: N5

[天気]
- matched_form: 天気
- reading: てんき
- meaning: weather
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5

[方]
- matched_form: 方
- reading: かた
- meaning: -- honorific form for 人 (ひと) --; way of doing
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5

[じゃ]
- matched_form: じゃ
- reading: じゃ; じゃあ
- meaning: well, well then
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #59 (ID: 68)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お腹空いたし、近くのレストランで何か温かいものでも食べない？` |
| **서버 AI 최종 교정본** | **お腹空いたし、近くのレストランで何か温かいものでも食べない？** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로도 올바릅니다. 의미도 명확하며, 회화적인 표현입니다.
- **일본어 해설:** この文は自然で、文法的にも正しいです。意味も明確で、会話的な表現です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[お腹]
- matched_form: お腹
- reading: おなか
- meaning: stomach
- level: N5

[空]
- matched_form: 空
- reading: そら
- meaning: sky
- level: N5

[近く]
- matched_form: 近く
- reading: ちかく
- meaning: nearby; in the neighborhood
- level: N5

[レストラン]
- matched_form: レストラン
- reading: レストラン
- meaning: restaurant
- level: N5

[何]
- matched_form: 何
- reading: なん; なに
- meaning: what
- level: N5

[でも]
- matched_form: でも
- reading: でも
- meaning: but, however
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #60 (ID: 69)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `明日の約束の時間に遅れそうなら、速攻で連れてって下さい。` |
| **서버 AI 최종 교정본** | **明日の約束の時間に遅れそうなら、速攻で連れてって下さい。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[明日]
- matched_form: 明日
- reading: あした
- meaning: tomorrow
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5

[下さい]
- matched_form: 下さい
- reading: ください
- meaning: (with te-form verb) please do for me
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #61 (ID: 70)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `最近仕事忙しくてさ、週末ゆっくり休む時間まじでないわ。` |
| **서버 AI 최종 교정본** | **最近仕事忙しくてさ、週末ゆっくり休む時間はまじでないわ。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '時間まじでない'은 자연스러운 표현이 아니며, '時間はまじでない'으로 조사 'は'를 추가하여 문법적으로 자연스러운 표현으로 수정했습니다.
- **일본어 해설:** 「時間まじでない」は自然な表現ではありません。文法的に自然な表現にするために「時間はまじでない」として、助詞「は」を追加しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[仕事]
- matched_form: 仕事
- reading: しごと
- meaning: work, job, occupation, employment
- level: N5

[休む]
- matched_form: 休む
- reading: やすむ
- meaning: to rest, to have a break, to get time off
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

--- 

## 📌 발화 샘플 데이터 #62 (ID: 71)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `この服デザインはいいけど、ちょっとサイズ小さい気がする。` |
| **서버 AI 최종 교정본** | **この服のデザインはいいけど、ちょっとサイズが小さい気がする。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 필요한 조사가 생략된 부분이 있어 문장 구조가 부자연스러웠습니다.
- **일본어 해설:** 文の中で必要な助詞が省略されている部分があり、文の構造が不自然でした。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[この]
- matched_form: この
- reading: この
- meaning: this
- level: N5

[服]
- matched_form: 服
- reading: ふく
- meaning: clothes
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5

[ちょっと]
- matched_form: ちょっと
- reading: ちょっと
- meaning: a little, somewhat; just a little, somewhat
- level: N5

[小さい]
- matched_form: 小さい
- reading: ちいさい
- meaning: small, little
- level: N5

[する]
- matched_form: する
- reading: する
- meaning: to do, to try; to wear small items (e.g., necktie, watch, etc.)
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #63 (ID: 72)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `友達の誕生日に何を、何をプレゼントしたらいいか悩んでる。` |
| **서버 AI 최종 교정본** | **友達の誕生日に何を、何をプレゼントしたらいいか悩んでる。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러우며, 오류가 없습니다.
- **일본어 해설:** この文は自然で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[友達]
- matched_form: 友達
- reading: ともだち
- meaning: friend
- level: N5

[誕生日]
- matched_form: 誕生日
- reading: たんじょうび
- meaning: birthday
- level: N5

[何]
- matched_form: 何
- reading: なん; なに
- meaning: what
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #64 (ID: 73)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `映画見に行きたいんだけど、一緒に行く人おらんくて困ってる。` |
| **서버 AI 최종 교정본** | **映画見に行きたいんだけど、一緒に行く人いないて困ってる。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[映画]
- matched_form: 映画
- reading: えいが
- meaning: movie, film
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5

[行く]
- matched_form: 行く
- reading: いく; ゆく
- meaning: to go
- level: N5

[人]
- matched_form: 人
- reading: ひと
- meaning: man, person
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_008] 〜たいです 희망 표현
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + たいです
- description_ko: 하고 싶은 일을 말할 때 동사의 ます형 어간에 たいです를 붙이는 경우가 많다.
- reference_examples: 食べたいです, 行きたいです
- possible_focus: 희망 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 희망 표현이 아닌 단순 서술문을 억지로 たい 형태로 해석하지 않는다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #65 (ID: 74)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `日本の文化に興味あるから、いつかきょとに行ってみたい。` |
| **서버 AI 최종 교정본** | **日本の文化に興味があるから、いつか日本に旅行したい。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미상 맞지만, 'きょと'는 자연스러운 표현이 아니며, '日本に旅行したい'가 더 자연스러운 표현입니다.
- **일본어 해설:** 文の意味は通っていますが、「きょと」は自然な表現ではなく、「日本に旅行したい」がより自然です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[いつ]
- matched_form: いつ
- reading: いつ
- meaning: when
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_008] 〜たいです 희망 표현
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + たいです
- description_ko: 하고 싶은 일을 말할 때 동사의 ます형 어간에 たいです를 붙이는 경우가 많다.
- reference_examples: 食べたいです, 行きたいです
- possible_focus: 희망 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 희망 표현이 아닌 단순 서술문을 억지로 たい 형태로 해석하지 않는다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #66 (ID: 75)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `コーヒーを飲みながら、静カフェで本を読むのが好き。` |
| **서버 AI 최종 교정본** | **コーヒーを飲みながら、静カフェで本を読むのが好きです。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. '好き' 뒤에 'です'를 추가하면 더 자연스러운 표현이 됩니다. 하지만 학습자 문장으로서는 생략된 경우도 가능하므로, 오류로 판단하지 않습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。'好き'の後に'です'を加えるとより自然になりますが、学習者の発話では省略された場合も自然です。したがって、誤りと見なしません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[コーヒー]
- matched_form: コーヒー
- reading: コーヒー
- meaning: coffee
- level: N5

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[読む]
- matched_form: 読む
- reading: よむ
- meaning: to read
- level: N5

[好き]
- matched_form: 好き
- reading: すき
- meaning: liking, fondness, love
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #67 (ID: 76)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `終電の時間確認しとかないと、帰れなくなるかも。` |
| **서버 AI 최종 교정본** | **終電の時間確認しとかないと、帰れなくなるかも。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5

[なる]
- matched_form: なる
- reading: なる
- meaning: to become
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

--- 

## 📌 발화 샘플 데이터 #68 (ID: 77)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `明日の会議は午後さんじはんからに変更になったので。` |
| **서버 AI 최종 교정본** | **明日の会議は午後三時からに変更になりました。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '午後さんじはんからに'는 자연스러운 표현이 아니며, '午後三時から'로 교정해야 합니다. 'からに'는 문법적으로 오류가 있으며, 'から'는 시작 시간을 나타내는 조사로, 'に'는 시간을 나타내는 조사로 사용되어야 합니다. 따라서 '午後三時から'로 수정해야 합니다.
- **일본어 해설:** 文の「午後さんじはんからに」は自然な表現ではありません。正しい表現は「午後三時から」です。「からに」は文法的に誤りであり、「から」は開始時間を表す接続詞で、「に」は時間を表す接続詞です。したがって、「午後三時から」と修正すべきです。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[明日]
- matched_form: 明日
- reading: あした
- meaning: tomorrow
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #69 (ID: 78)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `提出期限は今週の金曜日の午後五時までととなっております。` |
| **서버 AI 최종 교정본** | **提出期限は今週の金曜日の午後五時までととなっております。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러우며, 문법적 오류나 표현 부자연스러움이 없습니다.
- **일본어 해설:** 文は自然で、文法的誤りや表現の不自然さはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[今週]
- matched_form: 今週
- reading: こんしゅう
- meaning: this week
- level: N5

[金曜日]
- matched_form: 金曜日
- reading: きんようび
- meaning: Friday
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5

[五]
- matched_form: 五
- reading: ご
- meaning: five
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

--- 

## 📌 발화 샘플 데이터 #70 (ID: 79)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `今回のぽろじぇくとの予算案、今日中に確認してメールして。` |
| **서버 AI 최종 교정본** | **今回のポロジェクトの予算案、今日中に確認してメールします。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미는 전달되지만, 'ぽろじぇく'은 'ポロジェクト'로 교정되어야 하며, 'メールして'는 'メールします'으로 시제를 자연스럽게 맞추는 것이 더 적절합니다. 전체 문장이 어색한 표현으로 보입니다.
- **일본어 해설:** 文の意味は伝わっていますが、「ぽろじぇく」という語は「ポロジェクト」として正しい表現です。また、「メールして」は会話文として自然ではありません。「メールします」が適切です。全体的に不自然な表現です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[今]
- matched_form: 今
- reading: いま
- meaning: now
- level: N5

[今日]
- matched_form: 今日
- reading: きょう
- meaning: today, this day
- level: N5

[中]
- matched_form: 中
- reading: なか
- meaning: inside, middle, among
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_003] 今日 + は
- rule_type: soft_reference
- level: N5
- pattern: 今日 + は
- description_ko: 今日를 문장의 화제로 사용할 때 は를 붙여 今日は 형태로 쓰는 경우가 있다.
- reference_examples: 今日は学校に行きました
- possible_focus: 화제 표현, は 사용 여부, 자연스러운 문장 흐름
- possible_error_types: unnatural_expression
- overcorrection_note: 今日 뒤에 は가 없다고 해서 항상 오류는 아니다. 의미가 자연스럽다면 교정보다는 더 자연스러운 표현 제안으로만 다룬다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #71 (ID: 80)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `資料の作成が終わったら、一回チェックして下さい。` |
| **서버 AI 최종 교정본** | **資料の作成が終わったら、一回チェックして下さい。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[一]
- matched_form: 一
- reading: いち
- meaning: one
- level: N5

[下さい]
- matched_form: 下さい
- reading: ください
- meaning: (with te-form verb) please do for me
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #72 (ID: 81)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `来月のスケジュール、調整が必要なとこあります。` |
| **서버 AI 최종 교정본** | **来月のスケジュール、調整が必要なところあります。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[来月]
- matched_form: 来月
- reading: らいげつ
- meaning: next month
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #73 (ID: 82)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お手数かけますが、こっちの書類にサインお願いします。` |
| **서버 AI 최종 교정본** | **お手数ですが、こっちの書類にサインをお願いします。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미상 자연스럽지만, 'サイン'을 요청할 때 'を'를 생략한 것이 문법적으로 부정확합니다. 'サインをお願いします'으로 수정하여 조사가 올바르게 사용되도록 했습니다.
- **일본어 해설:** 文の意味は自然ですが、「サイン」を求める場合、「を」を省略しているため文法的に不自然です。これを「サインをお願いします」として、適切な助詞を追加しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[こっち]
- matched_form: こっち
- reading: こっち
- meaning: this person; this direction; this side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #74 (ID: 83)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `駅から会社までは歩いてじゅうごふんくらいかかります。` |
| **서버 AI 최종 교정본** | **駅から会社までは歩いてじゅうごふんくらいかかります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[駅]
- matched_form: 駅
- reading: えき
- meaning: station
- level: N5

[会社]
- matched_form: 会社
- reading: かいしゃ
- meaning: company, corporation
- level: N5

[では]
- matched_form: では
- reading: では
- meaning: then, well, so
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

--- 

## 📌 발화 샘플 데이터 #75 (ID: 84)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `さっき送ったメールのてんぷふぁいる見てください。` |
| **서버 AI 최종 교정본** | **さっき送ったメールのテンプファイルを見てください。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장의 의미는 자연스럽지만, 'てんぷふぁいる'이 'テンプファイル'로 교정되었으며, 'を'가 생략되어 있습니다. 'テンプファイル'은 'テンプファイル'로 표기하는 것이 정확한 일본어 표현입니다.
- **일본어 해설:** 文の意味は自然ですが、「てんぷふぁいる」は「テンプファイル」として正しい表記です。また、「を」が省略されています。

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #76 (ID: 85)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `本日の営業時間は午後八時で終了しました。` |
| **서버 AI 최종 교정본** | **本日の営業時間は午後八時で終了しました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現が正確であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5

[八]
- matched_form: 八
- reading: はち
- meaning: eight
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #77 (ID: 86)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新しいくらいあんととの打ち合わせは来週の水曜。` |
| **서버 AI 최종 교정본** | **新しいくらいのあんととの打ち合わせは来週の水曜日です。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 85.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '水曜'는 '水曜日'로 완성되어야 하며, 'あんととの'는 'あんととの'가 아니라 'あんととの'가 자연스러운 표현이지만, '新しいくらい'의 표현은 어색합니다. '新しいくらい'는 '新しいくらいの'로 조사가 추가되어야 하며, 전체 문장의 자연스러운 표현을 위해 조사가 생략된 부분을 보완했습니다.
- **일본어 해설:** 文の「水曜」は「水曜日」に補完すべきであり、「新しいくらい」の表現は不自然です。文法的に自然な表現にするために、「新しいくらいの」に助詞を追加し、文全体を自然な表現に調整しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5

[来週]
- matched_form: 来週
- reading: らいしゅう
- meaning: next week
- level: N5

[水]
- matched_form: 水
- reading: みず
- meaning: water
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_002] 名詞 + を + 食べる/飲む
- rule_type: reference
- level: N5
- pattern: 名詞 + を + 食べる/飲む
- description_ko: 먹거나 마시는 대상에는 조사 を를 붙이는 경우가 일반적이다.
- reference_examples: 水を飲みます, ご飯を食べます
- possible_focus: 목적어 표현, 조사 を 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확한 단편 발화는 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[word_choice_error] 단어 선택 오류
- description_ko: 동사와 명사의 의미 조합이 어색하거나 다른 단어가 더 적절할 가능성이 있는 경우이다.
- related_focus: 단어 선택, 동사와 목적어의 의미 관계
- reference_examples:
  - observed: 水を食べます
    reference: 水を飲みます
  - observed: ラーメンを飲みます
    reference: ラーメンを食べます
- overcorrection_note: 비유적 표현이나 특수 문맥일 수 있으므로, 단어 조합만 보고 기계적으로 오류 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #78 (ID: 87)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ここをますぐ行って、二つ目の交差点を右に曲がると。` |
| **서버 AI 최종 교정본** | **ここをすぐ行って、二つ目の交差点を右に曲がると。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 교정이 필요하지 않습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ここ]
- matched_form: ここ
- reading: ここ
- meaning: here, this place
- level: N5

[二つ]
- matched_form: 二つ
- reading: ふたつ
- meaning: two things
- level: N5

[目]
- matched_form: 目
- reading: め
- meaning: eye(s)
- level: N5

[交差点]
- matched_form: 交差点
- reading: こうさてん
- meaning: intersection
- level: N5

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #79 (ID: 88)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `横断歩道に渡ってから、左側に大きなビルが見えます。` |
| **서버 AI 최종 교정본** | **横断歩道に渡ってから、左側に大きなビルが見えます。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[横]
- matched_form: 横
- reading: よこ
- meaning: beside; side; width
- level: N5

[道]
- matched_form: 道
- reading: みち
- meaning: road, street; way, directions
- level: N5

[左]
- matched_form: 左
- reading: ひだり
- meaning: left hand side
- level: N5

[大きな]
- matched_form: 大きな
- reading: おおきな
- meaning: big
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #80 (ID: 89)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `しんじゅくえきの東口を出て、五分ほど歩いたとこ。` |
| **서버 AI 최종 교정본** | **しんじゅくえきの東口を出て、五分ほど歩いたところ。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미상 자연스럽지만, 'とこ'는 문법적으로 부정확하며, 'ところ'로 교정해야 합니다. 'とこ'는 오류로 간주되며, 'ところ'는 '그 지점'을 의미하는 자연스러운 표현입니다.
- **일본어 해설:** 文は意味的には自然ですが、「とこ」は文法的に不正確であり、「ところ」に修正すべきです。「とこ」は誤りと見なされ、「ところ」は「その場所」という自然な表現です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[東]
- matched_form: 東
- reading: ひがし
- meaning: east
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5

[五]
- matched_form: 五
- reading: ご
- meaning: five
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #81 (ID: 90)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `そのビルの地下にあるきさてんは、とても雰囲気が良い。` |
| **서버 AI 최종 교정본** | **そのビルの地下にあるきさてんは、とても雰囲気が良い。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[その]
- matched_form: その
- reading: その
- meaning: that
- level: N5

[下]
- matched_form: 下
- reading: した
- meaning: under, below, beneath
- level: N5

[とても]
- matched_form: とても
- reading: とても
- meaning: very (much), greatly, exceedingly
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #82 (ID: 91)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `信号を渡らないで、手前の角を左に曲がって。` |
| **서버 AI 최종 교정본** | **信号を渡らないで、手前の角を左に曲がって。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[前]
- matched_form: 前
- reading: まえ
- meaning: before, in front
- level: N5

[角]
- matched_form: 角
- reading: かど
- meaning: corner (e.g., desk, pavement)
- level: N5

[左]
- matched_form: 左
- reading: ひだり
- meaning: left hand side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #83 (ID: 92)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ホテルの向かい側に、にじゅうよんじ営業のコンビニがある。` |
| **서버 AI 최종 교정본** | **ホテルの向かい側に、にじゅうよんじ営業のコンビニがある。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ホテル]
- matched_form: ホテル
- reading: ホテル
- meaning: hotel
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #84 (ID: 93)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `この道をずーーっと進むと、突き当たりに公園が見える。` |
| **서버 AI 최종 교정본** | **この道をずーーっと進むと、突き当たりに公園が見える。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러우며, 오류가 없습니다.
- **일본어 해설:** この文は自然で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[この]
- matched_form: この
- reading: この
- meaning: this
- level: N5

[道]
- matched_form: 道
- reading: みち
- meaning: road, street; way, directions
- level: N5

[公園]
- matched_form: 公園
- reading: こうえん
- meaning: a park
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #85 (ID: 94)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `階段上がって二階に行くと、右側が受付です。` |
| **서버 AI 최종 교정본** | **階段上がって二階に行くと、右側が受付です。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[階段]
- matched_form: 階段
- reading: かいだん
- meaning: stairs
- level: N5

[上]
- matched_form: 上
- reading: うえ
- meaning: above (up, top, etc.), over, on top of
- level: N5

[二]
- matched_form: 二
- reading: に
- meaning: two
- level: N5

[行く]
- matched_form: 行く
- reading: いく; ゆく
- meaning: to go
- level: N5

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #86 (ID: 95)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `北口の改札を出てすぐのところに、マップがあります。` |
| **서버 AI 최종 교정본** | **北口の改札を出てすぐのところに、マップがあります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 오류가 없습니다.
- **일본어 해설:** 文は自然で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[北]
- matched_form: 北
- reading: きた
- meaning: north
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #87 (ID: 96)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `駐車場の入り口は、建物の裏側にありますので。` |
| **서버 AI 최종 교정본** | **駐車場の入り口は、建物の裏側にありますので。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[車]
- matched_form: 車
- reading: くるま
- meaning: car, vehicle
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5

[建物]
- matched_form: 建物
- reading: たてもの
- meaning: building
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #88 (ID: 97)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `としょかんに行って勉強したけど、集中できなかった。` |
| **서버 AI 최종 교정본** | **としょかんに行って勉強したけど、集中できなかった。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미가 올바르며 교정이 필요 없습니다.
- **일본어 해설:** この文は自然な日本語で、文法や意味が正しいため、修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[勉強]
- matched_form: 勉強
- reading: べんきょう (する)
- meaning: study
- level: N5

[中]
- matched_form: 中
- reading: なか
- meaning: inside, middle, among
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #89 (ID: 98)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `友達と一緒に美味しいおすしを食べに行った。` |
| **서버 AI 최종 교정본** | **友達と一緒に美味しいおすしを食べに行った。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[友達]
- matched_form: 友達
- reading: ともだち
- meaning: friend
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5

[美味しい]
- matched_form: 美味しい
- reading: おいしい
- meaning: delicious, tasty
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #90 (ID: 99)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `週末に家族とえいがかんに行って映画を見た。` |
| **서버 AI 최종 교정본** | **週末に家族とえいがかんに行って映画を見た。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 문제 없습니다.
- **일본어 해설:** この文は自然な日本語で、文法や意味において問題ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[家族]
- matched_form: 家族
- reading: かぞく
- meaning: family, members of a family
- level: N5

[映画]
- matched_form: 映画
- reading: えいが
- meaning: movie, film
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #91 (ID: 100)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `先生に質問したら、親切に教えてくれた。` |
| **서버 AI 최종 교정본** | **先生に質問したら、親切に教えてくれた。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[先生]
- matched_form: 先生
- reading: せんせい
- meaning: teacher, professor; master; doctor
- level: N5

[質問]
- matched_form: 質問
- reading: しつもん
- meaning: question, inquiry
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #92 (ID: 101)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `びょういんの予約が十時だから、急いで行かないと。` |
| **서버 AI 최종 교정본** | **びょういんの予約が十時だから、急いで行かないと。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[十]
- matched_form: 十
- reading: (〜を) とお
- meaning: ten (~)
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #93 (ID: 102)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `飛行機のチケットをいんたーねっとで予約した。` |
| **서버 AI 최종 교정본** | **飛行機のチケットをいんたーねっとで予約した。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[飛行機]
- matched_form: 飛行機
- reading: ひこうき
- meaning: airplane
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #94 (ID: 103)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `昨日はたくさん歩いたから、足が疲れた。` |
| **서버 AI 최종 교정본** | **昨日はたくさん歩いたから、足が疲れた。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로도 올바릅니다. 의미도 명확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で、文法的にも正しいです。意味も明確で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[昨日]
- matched_form: 昨日
- reading: きのう
- meaning: yesterday
- level: N5

[足]
- matched_form: 足
- reading: あし
- meaning: foot; leg
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #95 (ID: 104)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `毎日日本語の単語を五個ずつずつ覚えるようにしてる。` |
| **서버 AI 최종 교정본** | **毎日日本語の単語を五個ずつ覚えるようにしてる。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 단어를 '五個ずつ'로 반복해서 기억하는 것이 자연스럽지 않으며, '五個ずつ'가 두 번 반복되어 있습니다. '五個ずつ'는 이미 'ずつ'가 포함되어 있으므로, 중복이 발생한 것으로 보입니다. 조사가 누락된 것으로 판단되며, 문장의 자연스러움을 유지하면서 최소한으로 교정합니다.
- **일본어 해설:** 「五個ずつ」が2回繰り返されています。すでに「ずつ」が含まれているため、重複しています。文の自然さを保ちつつ、最小限の修正を行います。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[毎日]
- matched_form: 毎日
- reading: まいにち
- meaning: every day
- level: N5

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[五]
- matched_form: 五
- reading: ご
- meaning: five
- level: N5

[覚える]
- matched_form: 覚える
- reading: おぼえる
- meaning: to learn, to commit to memory, to remember, to memorize
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #96 (ID: 105)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お茶を飲みながら、これからの計画について話した。` |
| **서버 AI 최종 교정본** | **お茶を飲みながら、これからの計画について話した。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[お茶]
- matched_form: お茶
- reading: おちゃ
- meaning: (green) tea
- level: N5

[これ]
- matched_form: これ
- reading: これ
- meaning: this one
- level: N5

[話]
- matched_form: 話
- reading: はなし
- meaning: talk (chat), story
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #97 (ID: 106)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `じてんしゃに乗って近くの公園まで行った。` |
| **서버 AI 최종 교정본** | **じてんしゃに乗って近くの公園まで行った。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[近く]
- matched_form: 近く
- reading: ちかく
- meaning: nearby; in the neighborhood
- level: N5

[公園]
- matched_form: 公園
- reading: こうえん
- meaning: a park
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #98 (ID: 107)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `東京特許許可局のこうちょうが、新しいプロジェクトを発表した。` |
| **서버 AI 최종 교정본** | **東京特許許可局のこうちょうが、新しいプロジェクトを発表した。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[東]
- matched_form: 東
- reading: ひがし
- meaning: east
- level: N5

[うち]
- matched_form: うち
- reading: うち
- meaning: home; house; my place
- level: N5

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #99 (ID: 108)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新人歌手の新春しゃんそんそーが、まもなく始まる。` |
| **서버 AI 최종 교정본** | **新しく歌手になった新春しゃんそんそーが、まもなく始まる。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '新人歌手の'이 '新しく歌手になった'으로 자연스럽게 바꾸는 것이 더 적절하지만, 의미를 바꾸지 않고 최소한으로 교정하기 위해 'の'가 'に'로 바뀌는 것은 문법적으로 부적절합니다. 'の'는 소유 또는 관계를 나타내며, '新しく歌手になった'는 상태를 나타내므로 'の'가 오류입니다. 조사 오용이 발생했으므로 particle_misuse로 분류합니다.
- **일본어 해설:** 文の「新人歌手の」が「新しく歌手になった」に自然な表現に変更すべきですが、意味を変えることなく最小限で修正するため、「の」が「に」に変わるのは文法的に不適切です。「の」は所有または関係を表し、「新しく歌手になった」は状態を表すため、「の」の誤用が生じており、particle_misuseとして分類します。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[人]
- matched_form: 人
- reading: ひと
- meaning: man, person
- level: N5

[歌]
- matched_form: 歌
- reading: うた
- meaning: a song
- level: N5

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[春]
- matched_form: 春
- reading: はる
- meaning: spring
- level: N5

[始まる]
- matched_form: 始まる
- reading: はじまる
- meaning: (something) begins
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #100 (ID: 109)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `隣の客はよく柿食う客だってさ。` |
| **서버 AI 최종 교정본** | **隣の客はよく柿を食う客だってさ。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 조사 'を'가 누락되어 문장이 부자연스러워졌습니다. '柿を食う'으로 수정하면 자연스러운 표현이 됩니다.
- **일본어 해설:** 助詞「を」が省略されており、文が不自然です。『柿を食う』にすると自然な表現になります。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[隣]
- matched_form: 隣
- reading: となり
- meaning: next to, next door to
- level: N5

[よく]
- matched_form: よく
- reading: よく
- meaning: frequently, often (much); well, skillfully
- level: N5
```

--- 

## 📌 발화 샘플 데이터 #101 (ID: 110)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `坊主が屏風にうまく坊主の絵を描いた。` |
| **서버 AI 최종 교정본** | **坊主が屏風にうまく坊主の絵を描いた。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 85.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '屏風'에 '坊主의絵'를 '描いた'라는 표현이 자연스럽지 않습니다. '屏風'에 '絵'를 '描く' 것은 가능하지만, '坊主の絵'를 '描く'이라는 표현은 의미가 모호합니다. '坊主'가 '屏風'에 '絵'를 '描いた' 것이 더 자연스러운 표현입니다. 조사 'の'의 사용이 문맥상 부적절할 수 있습니다.
- **일본어 해설:** 「坊主が屏風にうまく坊主の絵を描いた」という表現は自然ではありません。屏風に絵を描くことは可能ですが、「坊主の絵」を描くという表現は意味が曖昧です。より自然な表現は「坊主が屏風に絵を描いた」です。のの使用が文脈的に不適切です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[風]
- matched_form: 風
- reading: かぜ
- meaning: wind, breeze
- level: N5

[絵]
- matched_form: 絵
- reading: え
- meaning: a painting; a picture; a drawing
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #102 (ID: 111)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `黄パプリカ赤パプリカ青パプリカをたくさん買った。` |
| **서버 AI 최종 교정본** | **黄パプリカ赤パプリカ青パプリカをたくさん買った。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[赤]
- matched_form: 赤
- reading: あか
- meaning: red
- level: N5

[青]
- matched_form: 青
- reading: あお
- meaning: blue
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #103 (ID: 112)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ばすがすばくはつって三回言うの難しい。` |
| **서버 AI 최종 교정본** | **バスがすばくはつって三回言うのは難しい。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '言うの'가 '言うのは'로 바뀌어야 자연스러운 표현이 됩니다. 'の'가 부족하여 문법적으로 어색한 부분이 있습니다.
- **일본어 해설:** 「言うの」は「言うのは」に修正すべきです。文法的に不自然な表現です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[三]
- matched_form: 三
- reading: さん
- meaning: three
- level: N5

[言う]
- matched_form: 言う
- reading: いう
- meaning: to say
- level: N5

[難しい]
- matched_form: 難しい
- reading: むずかしい
- meaning: difficult
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #104 (ID: 113)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `右目、みじみみ、右目と順番に触って。` |
| **서버 AI 최종 교정본** | **右目、みじみみ、右目と順番に触って。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 85.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 'みじみみ'는 '目'의 반복으로 보이며, 자연스러운 표현이 아닙니다. '目'이 반복된 것은 오류이며, '右目'과 '右目と順番に'로 수정해야 합니다. 그러나 문맥상 'みじみみ'가 '目'의 반복이 아니라 'みじみ'라는 단어로 오인된 것으로 보이며, 이는 조사 오용에 해당합니다.
- **일본어 해설:** 文に「みじみみ」という表現は自然ではありません。「目」が繰り返されているため、誤りと判断されます。文脈上「みじみ」は「目」の誤認であると考えられ、これは助詞の誤用に該当します。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5

[目]
- matched_form: 目
- reading: め
- meaning: eye(s)
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #105 (ID: 114)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `こつそしょうしょうのために、毎日カルシウム飲んでる。` |
| **서버 AI 최종 교정본** | **こつそしょうしょうのために、毎日カルシウムを飲んでいます。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '飲んでる'은 문법적으로 부정확하며, 'カルシウム'을 목적어로 하기 위해 'を'가 필요합니다. '飲んでる'은 '飲む'을 목적어로 하지 않기 때문에 조사 오용입니다.
- **일본어 해설:** 文に「飲んでる」は文法的に不正確です。「カルシウム」を目的語として使うには「を」が必要です。「飲んでる」は目的語を省略しているため、助詞の誤用です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[毎日]
- matched_form: 毎日
- reading: まいにち
- meaning: every day
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #106 (ID: 115)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ゆしゅつこうじょうの効率向上のための会議。` |
| **서버 AI 최종 교정본** | **ゆしゅつこうじょうの効率向上のための会議。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[上]
- matched_form: 上
- reading: うえ
- meaning: above (up, top, etc.), over, on top of
- level: N5
```

--- 

## 📌 발화 샘플 데이터 #107 (ID: 116)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `あったかかったから上着脱いで散歩行った。` |
| **서버 AI 최종 교정본** | **あったかかったから上着を脱いで散歩に行った。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 조사를 'を'로 수정하여 문법적으로 자연스러운 표현으로 변경했습니다.
- **일본어 해설:** 「を」を追加して文法的に自然な表現に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[上着]
- matched_form: 上着
- reading: うわぎ
- meaning: coat, jacket
- level: N5

[散歩]
- matched_form: 散歩
- reading: さんぽ (する)
- meaning: walk, stroll
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

--- 

## 📌 발화 샘플 데이터 #108 (ID: 117)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `来週の旅行なんですけど、天気が悪そうなら予定を変更した方がいいんじゃないですか。` |
| **서버 AI 최종 교정본** | **来週の旅行なんですけど、天気が悪そうなら予定を変更した方がいいんじゃないですか。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로도 올바릅니다. 의미도 명확하며, STT 인식 결과로 인한 오류가 없습니다.
- **일본어 해설:** この文は自然で、文法的に正しいです。意味も明確で、STT認識による誤認識はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[来週]
- matched_form: 来週
- reading: らいしゅう
- meaning: next week
- level: N5

[旅行]
- matched_form: 旅行
- reading: りょこう
- meaning: travel, trip
- level: N5

[天気]
- matched_form: 天気
- reading: てんき
- meaning: weather
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5

[方]
- matched_form: 方
- reading: かた
- meaning: -- honorific form for 人 (ひと) --; way of doing
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5

[じゃ]
- matched_form: じゃ
- reading: じゃ; じゃあ
- meaning: well, well then
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #109 (ID: 118)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `おなかがすいたので、近くのレストランで何かあたたかいものでも食べませんか。` |
| **서버 AI 최종 교정본** | **おなかがすいたので、近くのレストランで何かあたたかいものでも食べませんか。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 문법적으로 자연스럽고, 의미도 명확합니다. 오류가 없습니다.
- **일본어 해설:** 文法的に自然で、意味も明確です。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[近く]
- matched_form: 近く
- reading: ちかく
- meaning: nearby; in the neighborhood
- level: N5

[レストラン]
- matched_form: レストラン
- reading: レストラン
- meaning: restaurant
- level: N5

[何]
- matched_form: 何
- reading: なん; なに
- meaning: what
- level: N5

[でも]
- matched_form: でも
- reading: でも
- meaning: but, however
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #110 (ID: 119)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `明日の役底の時間におくれそうだったら、できるだけ早く連絡してください。` |
| **서버 AI 최종 교정본** | **明日の役底の時間におくれそうだったら、できるだけ早く連絡してください。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 문제 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味において問題ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[明日]
- matched_form: 明日
- reading: あした
- meaning: tomorrow
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5

[できる]
- matched_form: できる
- reading: できる
- meaning: to be able to (to accomplish)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #111 (ID: 120)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `最近仕事が忙しくて、週末にゆっくり休む時間が全然ありません。` |
| **서버 AI 최종 교정본** | **最近仕事が忙しくて、週末にゆっくり休む時間が全然ありません。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미도 명확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味も明確で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[仕事]
- matched_form: 仕事
- reading: しごと
- meaning: work, job, occupation, employment
- level: N5

[休む]
- matched_form: 休む
- reading: やすむ
- meaning: to rest, to have a break, to get time off
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #112 (ID: 121)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `この服はデザインはいいのですが、ちょっとサイズが小さい気がします。` |
| **서버 AI 최종 교정본** | **この服のデザインはいいのですが、ちょっとサイズが小さい気がします。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[この]
- matched_form: この
- reading: この
- meaning: this
- level: N5

[服]
- matched_form: 服
- reading: ふく
- meaning: clothes
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5

[ちょっと]
- matched_form: ちょっと
- reading: ちょっと
- meaning: a little, somewhat; just a little, somewhat
- level: N5

[小さい]
- matched_form: 小さい
- reading: ちいさい
- meaning: small, little
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #113 (ID: 122)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `友達の誕生日に何をプレゼントしたら喜んでくれるか悩んでいます。` |
| **서버 AI 최종 교정본** | **友達の誕生日に何をプレゼントしたら喜んでくれるか悩んでいます。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[友達]
- matched_form: 友達
- reading: ともだち
- meaning: friend
- level: N5

[誕生日]
- matched_form: 誕生日
- reading: たんじょうび
- meaning: birthday
- level: N5

[何]
- matched_form: 何
- reading: なん; なに
- meaning: what
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #114 (ID: 123)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `映画を見に行きたいのですが、一緒に行く人がいなくて困っています。` |
| **서버 AI 최종 교정본** | **映画を見に行きたいのですが、一緒に行く人がいなくて困っています。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[映画]
- matched_form: 映画
- reading: えいが
- meaning: movie, film
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5

[行く]
- matched_form: 行く
- reading: いく; ゆく
- meaning: to go
- level: N5

[人]
- matched_form: 人
- reading: ひと
- meaning: man, person
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_008] 〜たいです 희망 표현
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + たいです
- description_ko: 하고 싶은 일을 말할 때 동사의 ます형 어간에 たいです를 붙이는 경우가 많다.
- reference_examples: 食べたいです, 行きたいです
- possible_focus: 희망 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 희망 표현이 아닌 단순 서술문을 억지로 たい 형태로 해석하지 않는다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #115 (ID: 124)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `日本の文化に興味があるので、いつかきょうとに行ってみたいです。` |
| **서버 AI 최종 교정본** | **日本の文化に興味があるので、いつかきょうとに行ってみたいです。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 문법적으로 자연스럽고 의미가 명확합니다. 오류가 없습니다.
- **일본어 해설:** この文は文法的に自然で意味が明確です。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[いつ]
- matched_form: いつ
- reading: いつ
- meaning: when
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_008] 〜たいです 희망 표현
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + たいです
- description_ko: 하고 싶은 일을 말할 때 동사의 ます형 어간에 たいです를 붙이는 경우가 많다.
- reference_examples: 食べたいです, 行きたいです
- possible_focus: 희망 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 희망 표현이 아닌 단순 서술문을 억지로 たい 형태로 해석하지 않는다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #116 (ID: 125)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `コーヒーを飲みながら、静かなカフェで本を読むのが好きです。` |
| **서버 AI 최종 교정본** | **コーヒーを飲みながら、静かなカフェで本を読むのが好きです。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 조사나 동사 사용에 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現が正確であり、助詞や動詞の使用に誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[コーヒー]
- matched_form: コーヒー
- reading: コーヒー
- meaning: coffee
- level: N5

[静か]
- matched_form: 静か
- reading: しずか
- meaning: quiet, calm
- level: N5

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[読む]
- matched_form: 読む
- reading: よむ
- meaning: to read
- level: N5

[好き]
- matched_form: 好き
- reading: すき
- meaning: liking, fondness, love
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #117 (ID: 126)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `集電の時間を確認しておかないと、変えれなくなるかもしれません。` |
| **서버 AI 최종 교정본** | **集電の時間を確認しておかないと、変えることができなくなるかもしれません。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 동사 '変えれなくなる'은 문법적으로 어색합니다. '変える'이 '変えることができる' 형태로 바뀌어야 하며, 'なる'이 'なる'이 아닌 'ことができる'과 함께 사용되어야 합니다. '変えれなくなる'은 잘못된 동사 활용입니다.
- **일본어 해설:** 動詞「変えれなくなる」は文法的に不自然です。正しい表現は「変えることができなくなる」です。'なる'だけでは不適切であり、'ことができる'と組み合わせて使用すべきです。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5

[なる]
- matched_form: なる
- reading: なる
- meaning: to become
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #118 (ID: 127)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `明日の会議は午後3時半からに変更になりましたのでご注意ください` |
| **서버 AI 최종 교정본** | **明日の会議は午後3時半からに変更になりましたのでご注意ください** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[明日]
- matched_form: 明日
- reading: あした
- meaning: tomorrow
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5

[半]
- matched_form: 半
- reading: はん
- meaning: half (e.g., にじはん | half-past two)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #119 (ID: 128)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `提出期限は今週の金曜日の午後5時までとなっております` |
| **서버 AI 최종 교정본** | **提出期限は今週の金曜日の午後5時までとなっております** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미상 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味上の誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[今週]
- matched_form: 今週
- reading: こんしゅう
- meaning: this week
- level: N5

[金曜日]
- matched_form: 金曜日
- reading: きんようび
- meaning: Friday
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

--- 

## 📌 발화 샘플 데이터 #120 (ID: 129)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `今回のプロジェクトの予算案を、共重に確認してメールで送ってください。` |
| **서버 AI 최종 교정본** | **今回のプロジェクトの予算案を、共に確認してメールで送ってください。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 필요한 조사가 생략된 부분이 있어 문장 구조가 부자연스러웠습니다.
- **일본어 해설:** 文の中で必要な助詞が省略されている部分があり、文の構造が不自然でした。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[今]
- matched_form: 今
- reading: いま
- meaning: now
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #121 (ID: 130)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `資料の作成が終わりましたら、一度チェックをお願い致します。` |
| **서버 AI 최종 교정본** | **資料の作成が終わりましたら、一度チェックをお願いいたします。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미상 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味上の問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[一]
- matched_form: 一
- reading: いち
- meaning: one
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #122 (ID: 131)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `来月のスケジュールについて、調整が必要な部分があります。` |
| **서버 AI 최종 교정본** | **来月のスケジュールについて、調整が必要な部分があります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 교정이 필요하지 않습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[来月]
- matched_form: 来月
- reading: らいげつ
- meaning: next month
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #123 (ID: 132)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お手数をおかけしますが、こちらの処理にサインをお願いします。` |
| **서버 AI 최종 교정본** | **お手数をおかけしますが、こちらの処理にサインをお願いします。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 요청 표현과 문법이 올바르며, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、要求表現や文法は適切です。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[こちら]
- matched_form: こちら
- reading: こちら
- meaning: this person (polite); this way (polite)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #124 (ID: 133)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `駅から回車までは歩いて15分ほどかかります` |
| **서버 AI 최종 교정본** | **駅から回車までは歩いて15分ほどかかります** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[駅]
- matched_form: 駅
- reading: えき
- meaning: station
- level: N5

[車]
- matched_form: 車
- reading: くるま
- meaning: car, vehicle
- level: N5

[では]
- matched_form: では
- reading: では
- meaning: then, well, so
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

--- 

## 📌 발화 샘플 데이터 #125 (ID: 134)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `先ほどお送りしたメールイケオンブパイルール、ファジン・ハイ・ジュスティオ` |
| **서버 AI 최종 교정본** | **先ほどお送りしたメールのイケオンブパイルール、ファジン・ハイ・ジュスティオ** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 필요한 조사가 생략된 부분이 있어 문장 구조가 부자연스러웠습니다.
- **일본어 해설:** 文の中で必要な助詞が省略されている部分があり、文の構造が不自然でした。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[先]
- matched_form: 先
- reading: さき
- meaning: future; recent, previous
- level: N5
```

--- 

## 📌 발화 샘플 데이터 #126 (ID: 135)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `本日の営業時間は午後8時を持ちまして終了いたしました。` |
| **서버 AI 최종 교정본** | **本日の営業時間は午後8時までです。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미상 맞지만, '持ちまして終了いたしました'는 표현은 자연스럽지 않습니다. 'までです'로 바꾸면 더 자연스러운 표현이 됩니다.
- **일본어 해설:** 文の意味は正しいものの、「持ちまして終了いたしました」という表現は自然ではありません。『までです』にするとより自然な表現になります。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #127 (ID: 136)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新しいクライアントとの打ち合わせは来週の水曜日です。` |
| **서버 AI 최종 교정본** | **新しいクライアントとの打ち合わせは来週の水曜日です。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5

[来週]
- matched_form: 来週
- reading: らいしゅう
- meaning: next week
- level: N5

[水曜日]
- matched_form: 水曜日
- reading: すいようび
- meaning: Wednesday
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_002] 名詞 + を + 食べる/飲む
- rule_type: reference
- level: N5
- pattern: 名詞 + を + 食べる/飲む
- description_ko: 먹거나 마시는 대상에는 조사 を를 붙이는 경우가 일반적이다.
- reference_examples: 水を飲みます, ご飯を食べます
- possible_focus: 목적어 표현, 조사 を 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확한 단편 발화는 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[word_choice_error] 단어 선택 오류
- description_ko: 동사와 명사의 의미 조합이 어색하거나 다른 단어가 더 적절할 가능성이 있는 경우이다.
- related_focus: 단어 선택, 동사와 목적어의 의미 관계
- reference_examples:
  - observed: 水を食べます
    reference: 水を飲みます
  - observed: ラーメンを飲みます
    reference: ラーメンを食べます
- overcorrection_note: 비유적 표현이나 특수 문맥일 수 있으므로, 단어 조합만 보고 기계적으로 오류 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #128 (ID: 137)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ここをまっすぐ行って、2つ目の交差点を右に曲がると駅があります。` |
| **서버 AI 최종 교정본** | **ここをまっすぐ行って、2つ目の交差点を右に曲がると駅があります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 정확합니다.
- **일본어 해설:** この文は自然な日本語で、文法や意味ともに正確です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ここ]
- matched_form: ここ
- reading: ここ
- meaning: here, this place
- level: N5

[まっすぐ]
- matched_form: まっすぐ
- reading: まっすぐ
- meaning: straight (ahead), direct
- level: N5

[目]
- matched_form: 目
- reading: め
- meaning: eye(s)
- level: N5

[交差点]
- matched_form: 交差点
- reading: こうさてん
- meaning: intersection
- level: N5

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5

[駅]
- matched_form: 駅
- reading: えき
- meaning: station
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #129 (ID: 138)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `オーダンホードを渡ってから左側に大きなビルが見えてきます。` |
| **서버 AI 최종 교정본** | **オーダンホードを渡ってから左側に大きなビルが見えてきます。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[左]
- matched_form: 左
- reading: ひだり
- meaning: left hand side
- level: N5

[大きな]
- matched_form: 大きな
- reading: おおきな
- meaning: big
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #130 (ID: 139)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新宿平均の東口を出て、5分ほど歩いたところにあります。` |
| **서버 AI 최종 교정본** | **新宿の東口を出て、5分ほど歩いたところにあります。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미상 자연스럽지만, '東口'의 조사가 'の'로 바뀌어야 합니다. '東口'는 장소이므로 'の'가 적절합니다. '東口を'는 문법적으로 부적절합니다.
- **일본어 해설:** 文の意味は自然ですが、「東口」の場所を表すために「の」が適切です。「東口を」は文法的に不適切です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[東]
- matched_form: 東
- reading: ひがし
- meaning: east
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #131 (ID: 140)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `そのびるの近に歩きさ点は、とても吹息が良いです。` |
| **서버 AI 최종 교정본** | **その近くで歩き始めるのは、とても風が良いです。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '歩きさ点'은 자연스러운 표현이 아니며, '歩き始める'이 더 적절합니다. 또한 '吹息'는 '風'으로 바꾸어 더 자연스러운 표현으로 바꾸었습니다.
- **일본어 해설:** 「歩きさ点」は自然な表現ではありません。「歩き始める」が適切です。また「吹息」は「風」に変更し、より自然な表現にしています。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[その]
- matched_form: その
- reading: その
- meaning: that
- level: N5

[とても]
- matched_form: とても
- reading: とても
- meaning: very (much), greatly, exceedingly
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #132 (ID: 141)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `信号を当たらずに、手前のつの左に曲がってください。` |
| **서버 AI 최종 교정본** | **信号を渡らず、手前の左に曲がってください。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '当たらずに'는 자연스러운 표현이 아니며, '信号を渡らず'로 교정해야 합니다. '当たる'은 '신호를 맞추다'는 의미로, '信号を渡る'이 더 적절합니다.
- **일본어 해설:** 「当たらずに」は自然な表現ではありません。正しい表現は「信号を渡らず」です。「当たる」は「信号を合わせる」という意味であり、「信号を渡る」が適切です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[前]
- matched_form: 前
- reading: まえ
- meaning: before, in front
- level: N5

[左]
- matched_form: 左
- reading: ひだり
- meaning: left hand side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #133 (ID: 142)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ホテルの迎え側に、24時間平行をおぶコンビニがあります。` |
| **서버 AI 최종 교정본** | **ホテルの迎え側に、24時間営業のコンビニがあります。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '平行'는 적절한 표현이 아니며, '24시간営業'가 더 자연스러운 표현입니다. '平行'는 오류로 판단되며, '24時間営業'로 교정했습니다.
- **일본어 해설:** 文に「平行」は適切な表現ではなく、「24時間営業」が自然な表現です。この誤りを修正し、「24時間営業」に変更しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ホテル]
- matched_form: ホテル
- reading: ホテル
- meaning: hotel
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #134 (ID: 143)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `この道をずっと進むと、付き当たりに動きな公園が見えます。` |
| **서버 AI 최종 교정본** | **この道をずっと進むと、付近の公園が見えます。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '付き当たり'는 자연스러운 표현이 아니며, '付近'이 더 적절합니다. '付き当たり'는 '이웃', '가까이 있는' 의미로 사용되는 경우가 많지만, '公園'을 가리키는 문맥에서는 부적절합니다. '付近'이 더 자연스러운 표현입니다.
- **일본어 해설:** 「付き当たり」は文脈に合わない表現です。「付近」がより自然な表現です。公園を指す文脈では「付き当たり」は不自然です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[この]
- matched_form: この
- reading: この
- meaning: this
- level: N5

[道]
- matched_form: 道
- reading: みち
- meaning: road, street; way, directions
- level: N5

[公園]
- matched_form: 公園
- reading: こうえん
- meaning: a park
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #135 (ID: 144)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `階段を登って2階に上がると右手に受け付けがございます。` |
| **서버 AI 최종 교정본** | **階段を登って2階に上がると、右手に受け付けがございます。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 85.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '右手に受け付けがございます'는 표현이 자연스럽지 않습니다. '右手に受け付け'는 '오른쪽에 있는 수용 장소'를 의미하지만, '受け付け'는 일반적으로 '수용'을 의미하며, '受け付け'가 '受け入れ'나 '受け付ける'과 함께 사용되어야 합니다. '右手に受け入れの場所がございます' 또는 '右手に受け付けのスペースがございます' 등이 더 자연스러운 표현입니다. 그러나 의미를 바꾸지 않고 최소한으로 교정하므로, 조사 오용을 고려해 '右手に受け付け'를 '右手に受け付け'로 유지하고, 문맥상 조사의 사용을 개선하는 것이 필요합니다. 이 경우 'に'가 적절하지 않을 수 있으므로, 오류를 'particle_misuse'로 판단합니다.
- **일본어 해설:** 文の「右手に受け付けがございます」は自然ではありません。「受け付け」は一般的に「受け入れ」や「受け付ける」と連用され、場所を表す場合に「受け付けの場所」や「受け入れスペース」といった表現が適切です。意味を変えることなく最小限で修正するため、「右手に受け付け」をそのまま維持し、文脈上「に」の使用が適切でない可能性を考慮し、「particle_misuse」として誤りと判断します。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[階段]
- matched_form: 階段
- reading: かいだん
- meaning: stairs
- level: N5

[上]
- matched_form: 上
- reading: うえ
- meaning: above (up, top, etc.), over, on top of
- level: N5

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #136 (ID: 145)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `北口の開札を出てすぐのところに、案内図が設置されています。` |
| **서버 AI 최종 교정본** | **北口の開札を出てすぐのところに、案内図が設置されています。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러우며, 오류가 없습니다.
- **일본어 해설:** 文は自然で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[北]
- matched_form: 北
- reading: きた
- meaning: north
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #137 (ID: 146)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `中車上の入り口は、縦物の裏側にございますのでご注意ください。` |
| **서버 AI 최종 교정본** | **中車の入り口は、縦物の裏側にございますのでご注意ください。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 85.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '上'가 '車の上'로 해석될 수 있지만, '車'와 '上'가 함께 사용될 때는 '車の上'가 자연스러운 표현입니다. '中車上の入り口'은 의미상 어색하며, '中車の上'로 수정해야 합니다. '裏側'에 대한 설명도 자연스럽게 보이지 않지만, 의미를 바꾸지 않고 최소한으로 교정했습니다.
- **일본어 해설:** 「中車上の入り口」は意味が不自然です。正しい表現は「中車の上」です。文脈上「裏側」の説明も自然ではありませんが、意味を変えることなく最小限に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[中]
- matched_form: 中
- reading: なか
- meaning: inside, middle, among
- level: N5

[車]
- matched_form: 車
- reading: くるま
- meaning: car, vehicle
- level: N5

[上]
- matched_form: 上
- reading: うえ
- meaning: above (up, top, etc.), over, on top of
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5

[物]
- matched_form: 物
- reading: もの
- meaning: thing (concrete object)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #138 (ID: 147)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `徒職案に行って勉強しましたが、あまり集中できませんでした。` |
| **서버 AI 최종 교정본** | **徒職案に行って勉強しましたが、あまり集中できませんでした。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미도 명확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味も明確で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[勉強]
- matched_form: 勉強
- reading: べんきょう (する)
- meaning: study
- level: N5

[中]
- matched_form: 中
- reading: なか
- meaning: inside, middle, among
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 6 (keyword_match_count=4, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #139 (ID: 148)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `友達と一緒においしいをずしを食べに行きました。` |
| **서버 AI 최종 교정본** | **友達と一緒においしいずしを食べに行きました。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 식사의 대상인 'ずし'에 'を'가 필요하지만, 'おいしいをずし'는 문법적으로 틀렸습니다. 'おいしいずし'로 바꾸고, 'を'를 'ずし'에 붙여야 합니다.
- **일본어 해설:** 「おいしいをずし」は文法的に誤りです。正しい表現は「おいしいずし」で、「を」を「ずし」に付けてください。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[友達]
- matched_form: 友達
- reading: ともだち
- meaning: friend
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #140 (ID: 149)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `週末に家族と一緒に映画観へ行って、話題の映画を見ました。` |
| **서버 AI 최종 교정본** | **週末に家族と一緒に映画を見ました。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 올바르며, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語で、文法や意味ともに正しいため、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[家族]
- matched_form: 家族
- reading: かぞく
- meaning: family, members of a family
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5

[映画]
- matched_form: 映画
- reading: えいが
- meaning: movie, film
- level: N5

[話]
- matched_form: 話
- reading: はなし
- meaning: talk (chat), story
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #141 (ID: 150)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `先生に質問をしたら、とても親切に教えてくれました。` |
| **서버 AI 최종 교정본** | **先生に質問をしたら、とても親切に教えてくれました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[先生]
- matched_form: 先生
- reading: せんせい
- meaning: teacher, professor; master; doctor
- level: N5

[質問]
- matched_form: 質問
- reading: しつもん
- meaning: question, inquiry
- level: N5

[とても]
- matched_form: とても
- reading: とても
- meaning: very (much), greatly, exceedingly
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #142 (ID: 151)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `病院の予約が10時なので、急いで行かなければなりません。` |
| **서버 AI 최종 교정본** | **病院の予約が10時なので、急いで行かなければなりません。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미상 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味上の誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[病院]
- matched_form: 病院
- reading: びょういん
- meaning: hospital
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #143 (ID: 152)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `飛行機のチケットをインターネットで予約しました。` |
| **서버 AI 최종 교정본** | **飛行機のチケットをインターネットで予約しました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[飛行機]
- matched_form: 飛行機
- reading: ひこうき
- meaning: airplane
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #144 (ID: 153)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `機能はたくさんあるいたので、足がとても疲れました。` |
| **서버 AI 최종 교정본** | **機能はたくさんあるので、足がとても疲れました。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 'あるいた'는 표현이 자연스럽지 않습니다. 'ある'이 'ある'으로 바뀌고, 'いた'는 'ので'와 함께 사용되는 'ある'의 과거형이 아닌 현재형으로 바뀌어야 합니다. 'あるので'는 자연스러운 표현입니다. '足がとても疲れました'는 의미는 자연스럽지만, '機能はたくさんあるいた'는 문법적으로 오류가 있습니다.
- **일본어 해설:** 文に「あるいた」という表現は自然ではありません。「ある」が「ある」に変わり、「いた」は「ので」に続く「ある」の過去形ではなく、現在形に変更すべきです。「あるので」は自然な表現です。「足がとても疲れました」は意味は自然ですが、「機能はたくさんあるいた」という表現は文法的に誤りです。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[足]
- matched_form: 足
- reading: あし
- meaning: foot; leg
- level: N5

[とても]
- matched_form: とても
- reading: とても
- meaning: very (much), greatly, exceedingly
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #145 (ID: 154)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `毎日日本語の単語を50個ずつ覚えるようにしています` |
| **서버 AI 최종 교정본** | **毎日日本語の単語を50個ずつ覚えるようにしています** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로도 올바릅니다. 오류가 없습니다.
- **일본어 해설:** この文は自然で、文法的に正しいです。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[毎日]
- matched_form: 毎日
- reading: まいにち
- meaning: every day
- level: N5

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[覚える]
- matched_form: 覚える
- reading: おぼえる
- meaning: to learn, to commit to memory, to remember, to memorize
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #146 (ID: 155)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お茶を飲みながら、これからの計画について話し合いました。` |
| **서버 AI 최종 교정본** | **お茶を飲みながら、これからの計画について話し合いました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現が正確であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[お茶]
- matched_form: お茶
- reading: おちゃ
- meaning: (green) tea
- level: N5

[これ]
- matched_form: これ
- reading: これ
- meaning: this one
- level: N5

[話]
- matched_form: 話
- reading: はなし
- meaning: talk (chat), story
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #147 (ID: 156)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `自転車に乗って近くの公園まで遊びに行きました。` |
| **서버 AI 최종 교정본** | **自転車に乗って近くの公園まで遊びに行きました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 정확합니다.
- **일본어 해설:** この文は自然な日本語で、文法と意味ともに正確です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[自転車]
- matched_form: 自転車
- reading: じてんしゃ
- meaning: bicycle
- level: N5

[近く]
- matched_form: 近く
- reading: ちかく
- meaning: nearby; in the neighborhood
- level: N5

[公園]
- matched_form: 公園
- reading: こうえん
- meaning: a park
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #148 (ID: 157)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `東京都局局局長が、今日は新しいプロジェクトを発表しました。` |
| **서버 AI 최종 교정본** | **東京都局の長が、今日、新しいプロジェクトを発表しました。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '東京都局局局長'은 '東京都局の長'으로 자연스럽게 표현되며, '局局長'은 반복된 표현으로 어색합니다. '局' 뒤에 'の'를 붙여 명확하게 표현하고, '今日' 뒤에 'は'를 붙이지 않아도 됩니다. 조사 'は'가 없어도 문맥상 자연스러운 표현입니다.
- **일본어 해설:** 「東京都局局局長」は「東京都局の長」と自然な表現に修正され、重複した「局局長」は不自然です。「今日」の後に「は」をつける必要はありません。文脈上自然な表現です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[東]
- matched_form: 東
- reading: ひがし
- meaning: east
- level: N5

[今日]
- matched_form: 今日
- reading: きょう
- meaning: today, this day
- level: N5

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_003] 今日 + は
- rule_type: soft_reference
- level: N5
- pattern: 今日 + は
- description_ko: 今日를 문장의 화제로 사용할 때 は를 붙여 今日は 형태로 쓰는 경우가 있다.
- reference_examples: 今日は学校に行きました
- possible_focus: 화제 표현, は 사용 여부, 자연스러운 문장 흐름
- possible_error_types: unnatural_expression
- overcorrection_note: 今日 뒤에 は가 없다고 해서 항상 오류는 아니다. 의미가 자연스럽다면 교정보다는 더 자연스러운 표현 제안으로만 다룬다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #149 (ID: 158)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新銀化州の新瞬産村省がまもなく開催されます。` |
| **서버 AI 최종 교정본** | **新銀化州の新瞬産村省がまもなく開催されます。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 75.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '村省'라는 표현이 자연스럽지 않습니다. '村'과 '省'를 연결한 '村省'는 일반적인 일본어 표현이 아니며, 의미상 어색합니다. '村'과 '省'를 분리하여 '村の省' 또는 '村の自治体' 등으로 표현하는 것이 더 자연스럽습니다. 그러나 문맥상 '村省'가 의미를 전달하는 것으로 보이므로, 조사 오용이 의심됩니다.
- **일본어 해설:** 文に「村省」という表現は自然ではありません。一般的な日本語では「村」と「省」をつなげた「村省」は存在せず、意味が不自然です。文脈上「村の省」または「村の自治体」といった表現が自然です。ただし、文脈上「村省」が意味を伝えると見られることから、助詞の誤用が疑われます。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[村]
- matched_form: 村
- reading: むら
- meaning: village
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #150 (ID: 159)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `となりの客はよく書きく客だという有名な言葉があります。` |
| **서버 AI 최종 교정본** | **となりの客はよく書き手の客だという有名な言葉があります。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문맥상 사용된 조사가 적절하지 않아 더 자연스러운 조사로 수정했습니다.
- **일본어 해설:** 文脈上、使われている助詞が適切ではなかったため、より自然な助詞に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[よく]
- matched_form: よく
- reading: よく
- meaning: frequently, often (much); well, skillfully
- level: N5

[有名]
- matched_form: 有名
- reading: ゆうめい
- meaning: famous
- level: N5

[言葉]
- matched_form: 言葉
- reading: ことば
- meaning: language; word(s); expression(s)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #151 (ID: 160)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `坊図が病部に上手に坊図の絵を描いたそうです。` |
| **서버 AI 최종 교정본** | **坊図が病部で上手に絵を描いたそうです。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '病部に'는 '病部で'로 바꾸어야 합니다. '病部'는 장소이므로 'で'가 필요하며, 'に'는 위치를 나타내는 조사로 사용되어야 합니다. 의미는 유지하면서 문법적으로 자연스러운 표현으로 수정했습니다.
- **일본어 해설:** 文では「病部に」は「病部で」に修正すべきです。「病部」は場所であるため、「で」が必要であり、「に」は場所を表す接続詞として使用すべきです。意味は維持しつつ、文法的に自然な表現に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[上手]
- matched_form: 上手
- reading: じょうず
- meaning: be good at, skillful
- level: N5

[絵]
- matched_form: 絵
- reading: え
- meaning: a painting; a picture; a drawing
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #152 (ID: 161)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `赤パプリカキパプリカをシジョーでたくさん買いました` |
| **서버 AI 최종 교정본** | **赤いパプリカをシジョーでたくさん買いました** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 파프리카는 '赤い'가 더 자연스러운 표현입니다. '赤パプリカ'는 오류입니다.
- **일본어 해설:** パプリカは「赤いパプリカ」が自然な表現です。「赤パプリカ」は誤りです。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[赤]
- matched_form: 赤
- reading: あか
- meaning: red
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #153 (ID: 162)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `バスがすばくはちという言葉を3回続けていうのは難しいです。` |
| **서버 AI 최종 교정본** | **バスが「すばくはち」という言葉を3回続けて言うのは難しいです。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 'すばくはち'가 'バス'와 관련된 표현이므로, 'すばくはち'는 자연스럽지 않습니다. 'バス'가 'すばくはち'라는 말을 반복하는 것은 의미가 부족합니다. 'バス'가 'すばくはち'라는 말을 반복하는 것은 어색하므로, 'すばくはち'를 교정해야 합니다.
- **일본어 해설:** 「すばくはち」という言葉はバスと関係があるため自然ではありません。バスが「すばくはち」という言葉を繰り返すというのは意味が不自然です。この表現は不自然であるため、修正が必要です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[バス]
- matched_form: バス
- reading: バス
- meaning: bus; bath; bass
- level: N5

[言葉]
- matched_form: 言葉
- reading: ことば
- meaning: language; word(s); expression(s)
- level: N5

[難しい]
- matched_form: 難しい
- reading: むずかしい
- meaning: difficult
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #154 (ID: 163)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `右目右目右目と順番に触る運動をしてください` |
| **서버 AI 최종 교정본** | **右目を右目を右目を順番に触る運動をしてください** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문맥상 사용된 조사가 적절하지 않아 더 자연스러운 조사로 수정했습니다.
- **일본어 해설:** 文脈上、使われている助詞が適切ではなかったため、より自然な助詞に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5

[目]
- matched_form: 目
- reading: め
- meaning: eye(s)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #155 (ID: 164)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `こつそ少少の予防のために、前に使えるシュームを接種しています。` |
| **서버 AI 최종 교정본** | **こつそ少少の予防のために、前に使えるシュームを接種しています。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '前に使えるシューム'의 조사가 잘못 사용되어 있습니다. '前に'은 '前に'이 아니라 '前'이 적절한 경우가 많으며, '前に'는 '앞에'를 의미하는 조사로, '前'과 함께 사용할 때 문맥상 어색합니다. '前に'이 아닌 '前'으로 교정해야 합니다.
- **일본어 해설:** 文の「前に使えるシューム」の表現は不自然です。「前に」は「前」に続く場合に使われますが、文脈上「前」が適切です。正しい表現は「前」です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[前]
- matched_form: 前
- reading: まえ
- meaning: before, in front
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #156 (ID: 165)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `優質工場、優質工率の工場に向けた新しい会議を行います。` |
| **서버 AI 최종 교정본** | **新しい優質工場に向けた会議を行います。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '優質工場、優質工率の工場'는 의미가 모호하며, '優質工場'만을 사용하는 것이 자연스럽고, 'に向けた' 표현이 더 자연스러운 조합입니다. '工場'와 '工率'의 조합은 일본어로는 흔하지 않으며, 오류가 있습니다.
- **일본어 해설:** 文に「優質工場、優質工率の工場」という表現は意味が不明であり、自然な表現ではありません。より自然なのは「優質工場に向けた会議」という表現です。また、「工場」と「工率」の組み合わせは日本語では一般的ではありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #157 (ID: 166)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `あたたかかったから上げを抜いて3本に出かけました` |
| **서버 AI 최종 교정본** | **あたたかかったから、上を抜いて3本に出かけました** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '上げ'가 '上'로 교정되었으며, '上げ'는 '上'를 의미하는 조사가 아니라 '上'가 '위' 또는 '상위'를 의미하는 단어로, 문맥상 '上を抜いて'가 자연스러운 표현입니다. '上げ'는 '위로 올리다'를 의미하므로, 이 문장의 맥락에서 적절하지 않습니다.
- **일본어 해설:** 文に「上げ」が「上」に修正されました。『上げ』は「上に上げる」という意味であり、この文脈では「上を抜いて」という表現が自然です。文脈上、『上』が適切です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[上]
- matched_form: 上
- reading: うえ
- meaning: above (up, top, etc.), over, on top of
- level: N5

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #158 (ID: 167)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `来週の旅行なんだど、天気が悪そうなら予定を変更した方がいいんじゃない？` |
| **서버 AI 최종 교정본** | **来週の旅行が悪そうなら、予定を変更した方がいいんじゃない？** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '天気が悪そうなら'는 자연스러운 표현이지만, '天気' 다음에 'が'가 빠져 있어 문법적으로 부족합니다. 'が'를 추가하면 문장이 자연스러워집니다.
- **일본어 해설:** 「天気が悪そうなら」という表現は自然ですが、「天気」の後に「が」が欠けており、文法的に不自然です。それに「が」を追加することで自然な表現になります。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[来週]
- matched_form: 来週
- reading: らいしゅう
- meaning: next week
- level: N5

[旅行]
- matched_form: 旅行
- reading: りょこう
- meaning: travel, trip
- level: N5

[天気]
- matched_form: 天気
- reading: てんき
- meaning: weather
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5

[方]
- matched_form: 方
- reading: かた
- meaning: -- honorific form for 人 (ひと) --; way of doing
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5

[じゃ]
- matched_form: じゃ
- reading: じゃ; じゃあ
- meaning: well, well then
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #159 (ID: 168)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お腹空いたし、近くのレストランで何か温かいものでも食べない？` |
| **서버 AI 최종 교정본** | **お腹空いたし、近くのレストランで何か温かいものでも食べない？** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러우며, 의미도 명확합니다. 오류가 없습니다.
- **일본어 해설:** 文は自然で、意味も明確です。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[お腹]
- matched_form: お腹
- reading: おなか
- meaning: stomach
- level: N5

[空]
- matched_form: 空
- reading: そら
- meaning: sky
- level: N5

[近く]
- matched_form: 近く
- reading: ちかく
- meaning: nearby; in the neighborhood
- level: N5

[レストラン]
- matched_form: レストラン
- reading: レストラン
- meaning: restaurant
- level: N5

[何]
- matched_form: 何
- reading: なん; なに
- meaning: what
- level: N5

[でも]
- matched_form: でも
- reading: でも
- meaning: but, however
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #160 (ID: 169)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `明日の約束の時間に遅れそうなら、速攻で連れてって下さい。` |
| **서버 AI 최종 교정본** | **明日の約束の時間に遅れそうなら、速攻で連れてって下さい。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[明日]
- matched_form: 明日
- reading: あした
- meaning: tomorrow
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5

[下さい]
- matched_form: 下さい
- reading: ください
- meaning: (with te-form verb) please do for me
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #161 (ID: 170)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `最近仕事忙しくてさ、週末ゆっくり休む時間まじでないわ。` |
| **서버 AI 최종 교정본** | **最近仕事忙しくてさ、週末ゆっくり休む時間はまじでないわ。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '時間まじでないわ'는 자연스러운 표현이 아니며, '時間はまじでないわ'로 조사 'は'를 추가하여 문법적으로 자연스러운 표현으로 수정했습니다.
- **일본어 해설:** 「時間まじでないわ」は自然な表現ではありません。文法的に自然な表現にするために「時間はまじでないわ」として、助詞「は」を追加しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[仕事]
- matched_form: 仕事
- reading: しごと
- meaning: work, job, occupation, employment
- level: N5

[休む]
- matched_form: 休む
- reading: やすむ
- meaning: to rest, to have a break, to get time off
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

--- 

## 📌 발화 샘플 데이터 #162 (ID: 171)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `この服デザインはいいけど、ちょっとサイズ小さい気がする。` |
| **서버 AI 최종 교정본** | **この服のデザインはいいけど、ちょっとサイズが小さい気がする。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 필요한 조사가 생략된 부분이 있어 문장 구조가 부자연스러웠습니다.
- **일본어 해설:** 文の中で必要な助詞が省略されている部分があり、文の構造が不自然でした。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[この]
- matched_form: この
- reading: この
- meaning: this
- level: N5

[服]
- matched_form: 服
- reading: ふく
- meaning: clothes
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5

[ちょっと]
- matched_form: ちょっと
- reading: ちょっと
- meaning: a little, somewhat; just a little, somewhat
- level: N5

[小さい]
- matched_form: 小さい
- reading: ちいさい
- meaning: small, little
- level: N5

[する]
- matched_form: する
- reading: する
- meaning: to do, to try; to wear small items (e.g., necktie, watch, etc.)
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #163 (ID: 172)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `友達の誕生日に何を、何をプレゼントしたらいいか悩んでる。` |
| **서버 AI 최종 교정본** | **友達の誕生日に何を、何をプレゼントしたらいいか悩んでる。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러우며, 오류가 없습니다.
- **일본어 해설:** 文は自然で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[友達]
- matched_form: 友達
- reading: ともだち
- meaning: friend
- level: N5

[誕生日]
- matched_form: 誕生日
- reading: たんじょうび
- meaning: birthday
- level: N5

[何]
- matched_form: 何
- reading: なん; なに
- meaning: what
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #164 (ID: 173)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `映画見に行きたいんだけど、一緒に行く人おらんくて困ってる。` |
| **서버 AI 최종 교정본** | **映画見に行きたいんだけど、一緒に行ける人いないんだけど困ってる。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '一緒に行く人おらんくて困ってる' 부분에서 'おらんくて'는 자연스러운 표현이 아니며, 'いないんだけど'로 교정하는 것이 더 자연스럽습니다. 'おらんくて'는 오류로, '一緒に行く人がいない'으로 바꾸고, 문맥상 'んだけど'를 추가하여 자연스러운 회화 표현으로 조정했습니다.
- **일본어 해설:** 「一緒に行く人おらんくて困ってる」という表現は自然ではありません。正しい表現は「一緒に行く人がいないんだけど困ってる」です。この文では「おらんくて」が誤りであり、「一緒に行く人がいないんだけど困ってる」として自然な会話表現に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[映画]
- matched_form: 映画
- reading: えいが
- meaning: movie, film
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5

[行く]
- matched_form: 行く
- reading: いく; ゆく
- meaning: to go
- level: N5

[人]
- matched_form: 人
- reading: ひと
- meaning: man, person
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_008] 〜たいです 희망 표현
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + たいです
- description_ko: 하고 싶은 일을 말할 때 동사의 ます형 어간에 たいです를 붙이는 경우가 많다.
- reference_examples: 食べたいです, 行きたいです
- possible_focus: 희망 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 희망 표현이 아닌 단순 서술문을 억지로 たい 형태로 해석하지 않는다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #165 (ID: 174)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `日本の文化に興味あるから、いつかきょとに行ってみたい。` |
| **서버 AI 최종 교정본** | **日本の文化に興味あるから、いつか日本に旅行したい。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미상 맞지만, 'きょと'는 자연스러운 표현이 아니며, '日本に旅行したい'가 더 자연스러운 표현입니다.
- **일본어 해설:** 文の意味は正しいですが、「きょと」は自然な表現ではなく、「日本に旅行したい」がより自然です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[いつ]
- matched_form: いつ
- reading: いつ
- meaning: when
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_008] 〜たいです 희망 표현
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + たいです
- description_ko: 하고 싶은 일을 말할 때 동사의 ます형 어간에 たいです를 붙이는 경우가 많다.
- reference_examples: 食べたいです, 行きたいです
- possible_focus: 희망 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 희망 표현이 아닌 단순 서술문을 억지로 たい 형태로 해석하지 않는다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #166 (ID: 175)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `コーヒーを飲みながら、静カフェで本を読むのが好き。` |
| **서버 AI 최종 교정본** | **コーヒーを飲みながら、静カフェで本を読むのが好きです。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. '好き' 뒤에 'です'를 추가하면 더 자연스러운 표현이 되며, 이는 일본어에서 선호되는 표현입니다.
- **일본어 해설:** この文は自然で文法的に正しいです。'好き'の後に'です'を追加することでより自然な表現になります。これは日本語でよく使われる表現です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[コーヒー]
- matched_form: コーヒー
- reading: コーヒー
- meaning: coffee
- level: N5

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[読む]
- matched_form: 読む
- reading: よむ
- meaning: to read
- level: N5

[好き]
- matched_form: 好き
- reading: すき
- meaning: liking, fondness, love
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #167 (ID: 176)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `終電の時間確認しとかないと、帰れなくなるかも。` |
| **서버 AI 최종 교정본** | **終電の時間確認しとかないと、帰れなくなるかも。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5

[なる]
- matched_form: なる
- reading: なる
- meaning: to become
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

--- 

## 📌 발화 샘플 데이터 #168 (ID: 177)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `明日の会議は午後さんじはんからに変更になったので。` |
| **서버 AI 최종 교정본** | **明日の会議は午後三時からに変更になりました。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '午後さんじはん'이 '午後三時'으로 교정되었으며, 'からに'는 문법적으로 부적절한 표현입니다. 'から'와 'に'가 함께 사용된 것은 오류입니다. '午後三時から'로 수정하여 자연스러운 표현으로 변경했습니다.
- **일본어 해설:** 文に「午後さんじはんからに」とあり、文法的に不自然な表現です。「午後三時から」と修正し、自然な表現にしました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[明日]
- matched_form: 明日
- reading: あした
- meaning: tomorrow
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #169 (ID: 178)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `提出期限は今週の金曜日の午後五時までととなっております。` |
| **서버 AI 최종 교정본** | **提出期限は今週の金曜日の午後五時までととなっております。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미상 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味上の誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[今週]
- matched_form: 今週
- reading: こんしゅう
- meaning: this week
- level: N5

[金曜日]
- matched_form: 金曜日
- reading: きんようび
- meaning: Friday
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5

[五]
- matched_form: 五
- reading: ご
- meaning: five
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

--- 

## 📌 발화 샘플 데이터 #170 (ID: 179)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `今回のぽろじぇくとの予算案、今日中に確認してメールして。` |
| **서버 AI 최종 교정본** | **今回のポロジェクトの予算案、今日中に確認してメールします。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문법적으로 완전히 틀렸다고 보기는 어렵지만, 더 자연스러운 표현으로 수정했습니다.
- **일본어 해설:** 文法的に完全な誤りとは言い切れませんが、より自然な表現に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[今]
- matched_form: 今
- reading: いま
- meaning: now
- level: N5

[今日]
- matched_form: 今日
- reading: きょう
- meaning: today, this day
- level: N5

[中]
- matched_form: 中
- reading: なか
- meaning: inside, middle, among
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_003] 今日 + は
- rule_type: soft_reference
- level: N5
- pattern: 今日 + は
- description_ko: 今日를 문장의 화제로 사용할 때 は를 붙여 今日は 형태로 쓰는 경우가 있다.
- reference_examples: 今日は学校に行きました
- possible_focus: 화제 표현, は 사용 여부, 자연스러운 문장 흐름
- possible_error_types: unnatural_expression
- overcorrection_note: 今日 뒤에 は가 없다고 해서 항상 오류는 아니다. 의미가 자연스럽다면 교정보다는 더 자연스러운 표현 제안으로만 다룬다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #171 (ID: 180)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `資料の作成が終わったら、一回チェックして下さい。` |
| **서버 AI 최종 교정본** | **資料の作成が終わったら、一回チェックして下さい。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[一]
- matched_form: 一
- reading: いち
- meaning: one
- level: N5

[下さい]
- matched_form: 下さい
- reading: ください
- meaning: (with te-form verb) please do for me
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #172 (ID: 181)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `来月のスケジュール、調整が必要なとこあります。` |
| **서버 AI 최종 교정본** | **来月のスケジュール、調整が必要なところがあります。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 올바릅니다.
- **일본어 해설:** この文は自然な日本語で、文法と意味ともに正しいです。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[来月]
- matched_form: 来月
- reading: らいげつ
- meaning: next month
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #173 (ID: 182)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お手数かけますが、こっちの書類にサインお願いします。` |
| **서버 AI 최종 교정본** | **お手数ですが、こっちの書類にサインをお願いします。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미는 자연스럽지만, 'サイン'을 요청할 때 'を'를 생략한 것이 자연스럽지 않습니다. 'サインをお願いします'으로 조사를 추가하면 더 자연스러운 표현이 됩니다.
- **일본어 해설:** 文の意味は自然ですが、「サイン」を求める場合、「を」を省略しているため不自然です。正しい表現は「サインをお願いします」です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[こっち]
- matched_form: こっち
- reading: こっち
- meaning: this person; this direction; this side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #174 (ID: 183)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `駅から会社までは歩いてじゅうごふんくらいかかります。` |
| **서버 AI 최종 교정본** | **駅から会社までは歩いてじゅうごふんくらいかかります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[駅]
- matched_form: 駅
- reading: えき
- meaning: station
- level: N5

[会社]
- matched_form: 会社
- reading: かいしゃ
- meaning: company, corporation
- level: N5

[では]
- matched_form: では
- reading: では
- meaning: then, well, so
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

--- 

## 📌 발화 샘플 데이터 #175 (ID: 184)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `さっき送ったメールのてんぷふぁいる見てください。` |
| **서버 AI 최종 교정본** | **さっき送ったメールのテンプレートをみてください。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미가 자연스럽지만, 'てんぷふぁいる'은 'テンプレート'로 교정하고, 'を見てください'는 'をみてください'로 조사가 부족한 상태에서 'を'를 추가해야 합니다.
- **일본어 해설:** 文の意味は自然ですが、「てんぷふぁいる」は「テンプレート」として修正し、「をみてください」という表現に「を」を追加する必要があります。

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #176 (ID: 185)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `本日の営業時間は午後八時で終了しました。` |
| **서버 AI 최종 교정본** | **本日の営業時間は午後八時で終了しました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現は正確であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5

[八]
- matched_form: 八
- reading: はち
- meaning: eight
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #177 (ID: 186)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新しいくらいあんととの打ち合わせは来週の水曜。` |
| **서버 AI 최종 교정본** | **新しいくらいのあんととの打ち合わせは来週の水曜日です。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '水曜'는 '水曜日'로 완성되어야 하며, 'あんととの'는 'あんととの'가 아니라 'あんととの'가 자연스러운 표현이지만, 'あんととの'는 'あんととの'로 오류가 없음. 그러나 '水曜'는 '水曜日'로 완성되어야 하며, 조사 'を'가 생략되어 있음. 따라서 '水曜日'로 수정하고, 문장 구조를 자연스럽게 보완함.
- **일본어 해설:** 文の「水曜」は「水曜日」として完成すべきであり、文法的に「を」が省略されているため、修正が必要です。したがって、「水曜日」として書き換え、文の構造を自然に調整しています。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5

[来週]
- matched_form: 来週
- reading: らいしゅう
- meaning: next week
- level: N5

[水]
- matched_form: 水
- reading: みず
- meaning: water
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_002] 名詞 + を + 食べる/飲む
- rule_type: reference
- level: N5
- pattern: 名詞 + を + 食べる/飲む
- description_ko: 먹거나 마시는 대상에는 조사 を를 붙이는 경우가 일반적이다.
- reference_examples: 水を飲みます, ご飯を食べます
- possible_focus: 목적어 표현, 조사 を 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확한 단편 발화는 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[word_choice_error] 단어 선택 오류
- description_ko: 동사와 명사의 의미 조합이 어색하거나 다른 단어가 더 적절할 가능성이 있는 경우이다.
- related_focus: 단어 선택, 동사와 목적어의 의미 관계
- reference_examples:
  - observed: 水を食べます
    reference: 水を飲みます
  - observed: ラーメンを飲みます
    reference: ラーメンを食べます
- overcorrection_note: 비유적 표현이나 특수 문맥일 수 있으므로, 단어 조합만 보고 기계적으로 오류 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #178 (ID: 187)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ここをますぐ行って、二つ目の交差点を右に曲がると。` |
| **서버 AI 최종 교정본** | **ここをすぐに行って、二つ目の交差点を右に曲がると。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미상 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味上の誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ここ]
- matched_form: ここ
- reading: ここ
- meaning: here, this place
- level: N5

[二つ]
- matched_form: 二つ
- reading: ふたつ
- meaning: two things
- level: N5

[目]
- matched_form: 目
- reading: め
- meaning: eye(s)
- level: N5

[交差点]
- matched_form: 交差点
- reading: こうさてん
- meaning: intersection
- level: N5

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #179 (ID: 188)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `横断歩道に渡ってから、左側に大きなビルが見えます。` |
| **서버 AI 최종 교정본** | **横断歩道に渡ってから、左側に大きなビルが見えます。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 교정이 필요하지 않습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[横]
- matched_form: 横
- reading: よこ
- meaning: beside; side; width
- level: N5

[道]
- matched_form: 道
- reading: みち
- meaning: road, street; way, directions
- level: N5

[左]
- matched_form: 左
- reading: ひだり
- meaning: left hand side
- level: N5

[大きな]
- matched_form: 大きな
- reading: おおきな
- meaning: big
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #180 (ID: 189)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `しんじゅくえきの東口を出て、五分ほど歩いたとこ。` |
| **서버 AI 최종 교정본** | **しんじゅくえきの東口を出て、五分ほど歩いたところ。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미상 자연스럽지만, 'とこ'는 문법적으로 부정확하며 'ところ'로 교정해야 합니다. 'とこ'는 오류로 간주되며, 'ところ'는 '그곳'을 의미하는 자연스러운 표현입니다.
- **일본어 해설:** 文は意味的には自然ですが、「とこ」は文法的に不適切であり、「ところ」に修正すべきです。「とこ」は誤りと見なされ、「ところ」は「その場所」を意味する自然な表現です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[東]
- matched_form: 東
- reading: ひがし
- meaning: east
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5

[五]
- matched_form: 五
- reading: ご
- meaning: five
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #181 (ID: 190)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `そのビルの地下にあるきさてんは、とても雰囲気が良い。` |
| **서버 AI 최종 교정본** | **そのビルの地下にあるきさてんは、とても雰囲気が良い。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[その]
- matched_form: その
- reading: その
- meaning: that
- level: N5

[下]
- matched_form: 下
- reading: した
- meaning: under, below, beneath
- level: N5

[とても]
- matched_form: とても
- reading: とても
- meaning: very (much), greatly, exceedingly
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #182 (ID: 191)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `信号を渡らないで、手前の角を左に曲がって。` |
| **서버 AI 최종 교정본** | **信号を渡らないで、手前の角を左に曲がって。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[前]
- matched_form: 前
- reading: まえ
- meaning: before, in front
- level: N5

[角]
- matched_form: 角
- reading: かど
- meaning: corner (e.g., desk, pavement)
- level: N5

[左]
- matched_form: 左
- reading: ひだり
- meaning: left hand side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #183 (ID: 192)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ホテルの向かい側に、にじゅうよんじ営業のコンビニがある。` |
| **서버 AI 최종 교정본** | **ホテルの向かい側に、にじゅうよんじ営業のコンビニがある。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ホテル]
- matched_form: ホテル
- reading: ホテル
- meaning: hotel
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #184 (ID: 193)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `この道をずーーっと進むと、突き当たりに公園が見える。` |
| **서버 AI 최종 교정본** | **この道をずーーっと進むと、突き当たりに公園が見える。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러우며, 오류가 없습니다.
- **일본어 해설:** この文は自然で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[この]
- matched_form: この
- reading: この
- meaning: this
- level: N5

[道]
- matched_form: 道
- reading: みち
- meaning: road, street; way, directions
- level: N5

[公園]
- matched_form: 公園
- reading: こうえん
- meaning: a park
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #185 (ID: 194)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `階段上がって二階に行くと、右側が受付です。` |
| **서버 AI 최종 교정본** | **階段上がって二階に行くと、右側が受付です。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[階段]
- matched_form: 階段
- reading: かいだん
- meaning: stairs
- level: N5

[上]
- matched_form: 上
- reading: うえ
- meaning: above (up, top, etc.), over, on top of
- level: N5

[二]
- matched_form: 二
- reading: に
- meaning: two
- level: N5

[行く]
- matched_form: 行く
- reading: いく; ゆく
- meaning: to go
- level: N5

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #186 (ID: 195)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `北口の改札を出てすぐのところに、マップがあります。` |
| **서버 AI 최종 교정본** | **北口の改札を出てすぐのところに、マップがあります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[北]
- matched_form: 北
- reading: きた
- meaning: north
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #187 (ID: 196)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `駐車場の入り口は、建物の裏側にありますので。` |
| **서버 AI 최종 교정본** | **駐車場の入り口は、建物の裏側にありますので。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러우며, 오류가 없습니다.
- **일본어 해설:** 文は自然で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[車]
- matched_form: 車
- reading: くるま
- meaning: car, vehicle
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5

[建物]
- matched_form: 建物
- reading: たてもの
- meaning: building
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #188 (ID: 197)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `としょかんに行って勉強したけど、集中できなかった。` |
| **서버 AI 최종 교정본** | **としょかんに行って勉強したけど、集中できなかった。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미도 명확하며, STT 인식 결과로 판단되는 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味も明確で、STT認識結果としての誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[勉強]
- matched_form: 勉強
- reading: べんきょう (する)
- meaning: study
- level: N5

[中]
- matched_form: 中
- reading: なか
- meaning: inside, middle, among
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #189 (ID: 198)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `友達と一緒に美味しいおすしを食べに行った。` |
| **서버 AI 최종 교정본** | **友達と一緒に美味しいおすしを食べに行った。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 올바르며 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[友達]
- matched_form: 友達
- reading: ともだち
- meaning: friend
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5

[美味しい]
- matched_form: 美味しい
- reading: おいしい
- meaning: delicious, tasty
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #190 (ID: 199)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `週末に家族とえいがかんに行って映画を見た。` |
| **서버 AI 최종 교정본** | **週末に家族とえいがかんに行って映画を見た。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 문제 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味において問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[家族]
- matched_form: 家族
- reading: かぞく
- meaning: family, members of a family
- level: N5

[映画]
- matched_form: 映画
- reading: えいが
- meaning: movie, film
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #191 (ID: 200)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `先生に質問したら、親切に教えてくれた。` |
| **서버 AI 최종 교정본** | **先生に質問したら、親切に教えてくれた。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[先生]
- matched_form: 先生
- reading: せんせい
- meaning: teacher, professor; master; doctor
- level: N5

[質問]
- matched_form: 質問
- reading: しつもん
- meaning: question, inquiry
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #192 (ID: 201)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `びょういんの予約が十時だから、急いで行かないと。` |
| **서버 AI 최종 교정본** | **びょういんの予約が十時だから、急いで行かないと。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[十]
- matched_form: 十
- reading: (〜を) とお
- meaning: ten (~)
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #193 (ID: 202)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `飛行機のチケットをいんたーねっとで予約した。` |
| **서버 AI 최종 교정본** | **飛行機のチケットをいんたーねっとで予約した。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[飛行機]
- matched_form: 飛行機
- reading: ひこうき
- meaning: airplane
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #194 (ID: 203)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `昨日はたくさん歩いたから、足が疲れた。` |
| **서버 AI 최종 교정본** | **昨日はたくさん歩いたから、足が疲れた。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로도 올바릅니다. 의미도 명확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で、文法的にも正しいです。意味も明確で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[昨日]
- matched_form: 昨日
- reading: きのう
- meaning: yesterday
- level: N5

[足]
- matched_form: 足
- reading: あし
- meaning: foot; leg
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #195 (ID: 204)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `毎日日本語の単語を五個ずつずつ覚えるようにしてる。` |
| **서버 AI 최종 교정본** | **毎日日本語の単語を五個ずつ覚えるようにしてる。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 단어를 '五個ずつ'로 반복해서 기억하는 것을 말하고 있지만, 'ずつ'가 두 번 반복되어 있습니다. '五個ずつ'는 이미 'ずつ'가 포함된 표현이므로, 중복이 생겼습니다. 자연스러운 표현은 '毎日日本語の単語を五個ずつ覚えるようにしてる'으로, 'ずつ'가 두 번 나온 것은 오류입니다.
- **일본어 해설:** 「五個ずつ」が2回繰り返されています。すでに「ずつ」が含まれているため、重複しています。自然な表現は「毎日日本語の単語を五個ずつ覚えるようにしてる」です。ここでは「ずつ」が2回現れているため、誤りです。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[毎日]
- matched_form: 毎日
- reading: まいにち
- meaning: every day
- level: N5

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[五]
- matched_form: 五
- reading: ご
- meaning: five
- level: N5

[覚える]
- matched_form: 覚える
- reading: おぼえる
- meaning: to learn, to commit to memory, to remember, to memorize
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #196 (ID: 205)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お茶を飲みながら、これからの計画について話した。` |
| **서버 AI 최종 교정본** | **お茶を飲みながら、これからの計画について話した。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[お茶]
- matched_form: お茶
- reading: おちゃ
- meaning: (green) tea
- level: N5

[これ]
- matched_form: これ
- reading: これ
- meaning: this one
- level: N5

[話]
- matched_form: 話
- reading: はなし
- meaning: talk (chat), story
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #197 (ID: 206)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `じてんしゃに乗って近くの公園まで行った。` |
| **서버 AI 최종 교정본** | **じてんしゃに乗って近くの公園まで行った。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[近く]
- matched_form: 近く
- reading: ちかく
- meaning: nearby; in the neighborhood
- level: N5

[公園]
- matched_form: 公園
- reading: こうえん
- meaning: a park
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #198 (ID: 207)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `東京特許許可局のこうちょうが、新しいプロジェクトを発表した。` |
| **서버 AI 최종 교정본** | **東京特許許可局のこうちょうが、新しいプロジェクトを発表した。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[東]
- matched_form: 東
- reading: ひがし
- meaning: east
- level: N5

[うち]
- matched_form: うち
- reading: うち
- meaning: home; house; my place
- level: N5

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #199 (ID: 208)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新人歌手の新春しゃんそんそーが、まもなく始まる。` |
| **서버 AI 최종 교정본** | **新しく歌手になった新春しゃんそんそーが、まもなく始まる。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 85.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '新人歌手'가 '新しく歌手になった'로 자연스럽게 표현되도록 수정했으며, 'の'가 'になった'과 함께 사용된 것이 문법적으로 부적절한 경우가 있으므로 조사 오용으로 판단했습니다.
- **일본어 해설:** 「新人歌手」は「新しく歌手になった」として自然な表現に修正し、「の」が「になった」と一緒に使われているのは文法的に不適切であるため、調節誤用と判断しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[人]
- matched_form: 人
- reading: ひと
- meaning: man, person
- level: N5

[歌]
- matched_form: 歌
- reading: うた
- meaning: a song
- level: N5

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[春]
- matched_form: 春
- reading: はる
- meaning: spring
- level: N5

[始まる]
- matched_form: 始まる
- reading: はじまる
- meaning: (something) begins
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #200 (ID: 209)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `隣の客はよく柿食う客だってさ。` |
| **서버 AI 최종 교정본** | **隣の客はよく柿を食う客だってさ。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 조사 'を'가 누락되어 자연스러운 표현이 아닙니다. '柿を食う'으로 수정하여 문법적으로 완성했습니다.
- **일본어 해설:** 助詞「を」が欠落しており、自然な表現ではありません。『柿を食う』に修正して文法的に完成させました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[隣]
- matched_form: 隣
- reading: となり
- meaning: next to, next door to
- level: N5

[よく]
- matched_form: よく
- reading: よく
- meaning: frequently, often (much); well, skillfully
- level: N5
```

--- 

## 📌 발화 샘플 데이터 #201 (ID: 210)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `坊主が屏風にうまく坊主の絵を描いた。` |
| **서버 AI 최종 교정본** | **坊主が屏風にうまく坊主の絵を描いた。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 75.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '屏風に'가 자연스러운 표현이 아니며, '屏風に'는 '屏風'에 대해 '에'를 사용하는 것이 아니라 'に'가 적절한 경우가 많습니다. '屏風に'는 문맥상 어색합니다. '屏風に'를 '屏風の前に' 또는 '屏風の上に'로 바꾸는 것이 더 자연스러울 수 있습니다. 그러나 입력 문장의 의미를 바꾸지 않고 최소한의 교정을 하기 위해, 조사 오용을 고려하여 'に'를 'の前に'로 교정합니다.
- **일본어 해설:** 文では「屏風に」が自然な表現ではありません。「屏風に」は「屏風の前に」または「屏風の上に」が適切な場合が多いです。文脈上、文法的に不自然です。意味を変えることなく最小限の修正を行うため、「に」を「の前に」に修正します。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[風]
- matched_form: 風
- reading: かぜ
- meaning: wind, breeze
- level: N5

[絵]
- matched_form: 絵
- reading: え
- meaning: a painting; a picture; a drawing
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #202 (ID: 211)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `黄パプリカ赤パプリカ青パプリカをたくさん買った。` |
| **서버 AI 최종 교정본** | **黄パプリカ赤パプリカ青パプリカをたくさん買った。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[赤]
- matched_form: 赤
- reading: あか
- meaning: red
- level: N5

[青]
- matched_form: 青
- reading: あお
- meaning: blue
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #203 (ID: 212)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ばすがすばくはつって三回言うの難しい。` |
| **서버 AI 최종 교정본** | **ばすがすばくはつって三回言うのは難しい。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 필요한 조사가 생략된 부분이 있어 문장 구조가 부자연스러웠습니다.
- **일본어 해설:** 文の中で必要な助詞が省略されている部分があり、文の構造が不自然でした。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[三]
- matched_form: 三
- reading: さん
- meaning: three
- level: N5

[言う]
- matched_form: 言う
- reading: いう
- meaning: to say
- level: N5

[難しい]
- matched_form: 難しい
- reading: むずかしい
- meaning: difficult
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #204 (ID: 213)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `右目、みじみみ、右目と順番に触って。` |
| **서버 AI 최종 교정본** | **右目、みじみみ、右目と順番に触れることにします。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 85.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '触って'는 '触れる'이 더 자연스러운 표현이며, '触って'는 문법적으로 부적절한 조사 사용입니다. '触れることにします'으로 교정하였습니다.
- **일본어 해설:** 文の「触って」は文法的に不自然であり、「触れることにします」が自然な表現です。このように修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5

[目]
- matched_form: 目
- reading: め
- meaning: eye(s)
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #205 (ID: 214)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `こつそしょうしょうのために、毎日カルシウム飲んでる。` |
| **서버 AI 최종 교정본** | **こつそしょうしょうのために、毎日カルシウムを飲んでいます。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '飲んでる'은 자연스러운 표현이 아니며, 'カルシウム'을 먹는 동작에 맞는 조사 'を'가 누락되어 있습니다. 'を'를 추가하면 문법적으로 자연스러운 문장이 됩니다.
- **일본어 해설:** 「飲んでる」は自然な表現ではありません。カルシウムの摂取に適した助詞「を」が欠けています。これを追加すると文法的に自然な文になります。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[毎日]
- matched_form: 毎日
- reading: まいにち
- meaning: every day
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #206 (ID: 215)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ゆしゅつこうじょうの効率向上のための会議。` |
| **서버 AI 최종 교정본** | **ゆしゅつこうじょうの効率向上のための会議** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[上]
- matched_form: 上
- reading: うえ
- meaning: above (up, top, etc.), over, on top of
- level: N5
```

--- 

## 📌 발화 샘플 데이터 #207 (ID: 216)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `あったかかったから上着脱いで散歩行った。` |
| **서버 AI 최종 교정본** | **あったかかったから上着を脱いで散歩に行った。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 상의를 벗고 산책을 갔다는 의미는 자연스럽지만, '上着脱いで'는 문법적으로 부정확합니다. '上着を'를 추가하여 조사를 명확히 하면 문장이 자연스러워집니다.
- **일본어 해설:** 「上着脱いで」という表現は文法的に不自然です。文法的に自然な表現にするために「上着を」を追加してください。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[上着]
- matched_form: 上着
- reading: うわぎ
- meaning: coat, jacket
- level: N5

[散歩]
- matched_form: 散歩
- reading: さんぽ (する)
- meaning: walk, stroll
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

--- 

## 📌 발화 샘플 데이터 #208 (ID: 217)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `来週の旅行なんですけど、天気が悪そうなら予定を変更した方がいいんじゃないですか。` |
| **서버 AI 최종 교정본** | **来週の旅行なんですけど、天気が悪そうなら予定を変更した方がいいんじゃないですか。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[来週]
- matched_form: 来週
- reading: らいしゅう
- meaning: next week
- level: N5

[旅行]
- matched_form: 旅行
- reading: りょこう
- meaning: travel, trip
- level: N5

[天気]
- matched_form: 天気
- reading: てんき
- meaning: weather
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5

[方]
- matched_form: 方
- reading: かた
- meaning: -- honorific form for 人 (ひと) --; way of doing
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5

[じゃ]
- matched_form: じゃ
- reading: じゃ; じゃあ
- meaning: well, well then
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #209 (ID: 218)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お腹が空いたので、近くのレストランで何か温かいものでも食べませんか。` |
| **서버 AI 최종 교정본** | **お腹が空いたので、近くのレストランで何か温かいものでも食べませんか。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 문법적으로 자연스럽고, 의미도 명확합니다. 오류가 없습니다.
- **일본어 해설:** この文は文法的に自然で、意味も明確です。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[お腹]
- matched_form: お腹
- reading: おなか
- meaning: stomach
- level: N5

[空]
- matched_form: 空
- reading: そら
- meaning: sky
- level: N5

[近く]
- matched_form: 近く
- reading: ちかく
- meaning: nearby; in the neighborhood
- level: N5

[レストラン]
- matched_form: レストラン
- reading: レストラン
- meaning: restaurant
- level: N5

[何]
- matched_form: 何
- reading: なん; なに
- meaning: what
- level: N5

[でも]
- matched_form: でも
- reading: でも
- meaning: but, however
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #210 (ID: 219)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `明日の約束の時間に遅れそうだったら、できるだけ早く連絡してください。` |
| **서버 AI 최종 교정본** | **明日の約束の時間に遅れそうだったら、できるだけ早く連絡してください。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 문제 없습니다.
- **일본어 해설:** この文は自然な日本語で、文法や意味ともに問題ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[明日]
- matched_form: 明日
- reading: あした
- meaning: tomorrow
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5

[できる]
- matched_form: できる
- reading: できる
- meaning: to be able to (to accomplish)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #211 (ID: 220)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `最近仕事が忙しくて、週末にゆっくり休む時間が全然ありません。` |
| **서버 AI 최종 교정본** | **最近仕事が忙しくて、週末にゆっくり休む時間が全然ありません。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미도 명확하며, STT 인식 오류가 없어 보입니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味も明確で、STT認識の誤りは見当たりません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[仕事]
- matched_form: 仕事
- reading: しごと
- meaning: work, job, occupation, employment
- level: N5

[休む]
- matched_form: 休む
- reading: やすむ
- meaning: to rest, to have a break, to get time off
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #212 (ID: 221)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `この服はデザインはいいのですが、ちょっとサイズが小さい気がします。` |
| **서버 AI 최종 교정본** | **この服のデザインはいいのですが、ちょっとサイズが小さい気がします。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미도 명확하고 문법적으로도 올바릅니다. 조사나 표현에 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味も明確で文法的に正しいです。修飾や表現に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[この]
- matched_form: この
- reading: この
- meaning: this
- level: N5

[服]
- matched_form: 服
- reading: ふく
- meaning: clothes
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5

[ちょっと]
- matched_form: ちょっと
- reading: ちょっと
- meaning: a little, somewhat; just a little, somewhat
- level: N5

[小さい]
- matched_form: 小さい
- reading: ちいさい
- meaning: small, little
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #213 (ID: 222)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `友達の誕生日に何をプレゼントしたら喜んでくれるか悩んでいます。` |
| **서버 AI 최종 교정본** | **友達の誕生日に何をプレゼントしたら喜んでくれるか悩んでいます。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로도 올바릅니다. 추가적인 교정이 필요 없습니다.
- **일본어 해설:** この文は自然で、文法的に正しいです。追加の修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[友達]
- matched_form: 友達
- reading: ともだち
- meaning: friend
- level: N5

[誕生日]
- matched_form: 誕生日
- reading: たんじょうび
- meaning: birthday
- level: N5

[何]
- matched_form: 何
- reading: なん; なに
- meaning: what
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #214 (ID: 223)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `映画を見に行きたいのですが、一緒に行く人がいなくて困っています。` |
| **서버 AI 최종 교정본** | **映画を見に行きたいのですが、一緒に行く人がいなくて困っています。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[映画]
- matched_form: 映画
- reading: えいが
- meaning: movie, film
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5

[行く]
- matched_form: 行く
- reading: いく; ゆく
- meaning: to go
- level: N5

[人]
- matched_form: 人
- reading: ひと
- meaning: man, person
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_008] 〜たいです 희망 표현
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + たいです
- description_ko: 하고 싶은 일을 말할 때 동사의 ます형 어간에 たいです를 붙이는 경우가 많다.
- reference_examples: 食べたいです, 行きたいです
- possible_focus: 희망 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 희망 표현이 아닌 단순 서술문을 억지로 たい 형태로 해석하지 않는다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #215 (ID: 224)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `日本の文化に興味があるので、いつか京都に行ってみたいです。` |
| **서버 AI 최종 교정본** | **日本の文化に興味があるので、いつか京都に行ってみたいです。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 문법적으로 자연스럽고 의미가 명확합니다. 일본어 학습자에게 적절한 표현입니다.
- **일본어 해설:** この文は文法的に自然で意味が明確です。日本語学習者にとって適切な表現です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[いつ]
- matched_form: いつ
- reading: いつ
- meaning: when
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_008] 〜たいです 희망 표현
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + たいです
- description_ko: 하고 싶은 일을 말할 때 동사의 ます형 어간에 たいです를 붙이는 경우가 많다.
- reference_examples: 食べたいです, 行きたいです
- possible_focus: 희망 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 희망 표현이 아닌 단순 서술문을 억지로 たい 형태로 해석하지 않는다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #216 (ID: 225)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `コーヒーを飲みながら、静かなカフェで本を読むのが好きです。` |
| **서버 AI 최종 교정본** | **コーヒーを飲みながら、静かなカフェで本を読むのが好きです。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 조사나 동사 사용에 문제가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現が正確であり、助詞や動詞の使用に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[コーヒー]
- matched_form: コーヒー
- reading: コーヒー
- meaning: coffee
- level: N5

[静か]
- matched_form: 静か
- reading: しずか
- meaning: quiet, calm
- level: N5

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[読む]
- matched_form: 読む
- reading: よむ
- meaning: to read
- level: N5

[好き]
- matched_form: 好き
- reading: すき
- meaning: liking, fondness, love
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #217 (ID: 226)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `終電の時間を確認しておかないと、帰れなくなるかもしれません。` |
| **서버 AI 최종 교정본** | **終電の時間を確認しておかないと、帰れなくなるかもしれません。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미도 명확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味も明確で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5

[なる]
- matched_form: なる
- reading: なる
- meaning: to become
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #218 (ID: 227)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `明日の会議は午後三時半からに変更になりましたのでご注意ください。` |
| **서버 AI 최종 교정본** | **明日の会議は午後三時半からに変更になりましたのでご注意ください。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[明日]
- matched_form: 明日
- reading: あした
- meaning: tomorrow
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5

[三]
- matched_form: 三
- reading: さん
- meaning: three
- level: N5

[半]
- matched_form: 半
- reading: はん
- meaning: half (e.g., にじはん | half-past two)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #219 (ID: 228)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `提出期限は今週の金曜日の午後五時までとなっております。` |
| **서버 AI 최종 교정본** | **提出期限は今週の金曜日の午後五時までとなっております。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現が正確であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[今週]
- matched_form: 今週
- reading: こんしゅう
- meaning: this week
- level: N5

[金曜日]
- matched_form: 金曜日
- reading: きんようび
- meaning: Friday
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5

[五]
- matched_form: 五
- reading: ご
- meaning: five
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

--- 

## 📌 발화 샘플 데이터 #220 (ID: 229)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `今回のプロジェクトの予算案を、今日中に確認してメールで送ってください。` |
| **서버 AI 최종 교정본** | **今回のプロジェクトの予算案を、今日中に確認してメールで送ってください。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 문제 없습니다.
- **일본어 해설:** この文は自然な日本語で、文法や意味に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[今]
- matched_form: 今
- reading: いま
- meaning: now
- level: N5

[今日]
- matched_form: 今日
- reading: きょう
- meaning: today, this day
- level: N5

[中]
- matched_form: 中
- reading: なか
- meaning: inside, middle, among
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_003] 今日 + は
- rule_type: soft_reference
- level: N5
- pattern: 今日 + は
- description_ko: 今日를 문장의 화제로 사용할 때 は를 붙여 今日は 형태로 쓰는 경우가 있다.
- reference_examples: 今日は学校に行きました
- possible_focus: 화제 표현, は 사용 여부, 자연스러운 문장 흐름
- possible_error_types: unnatural_expression
- overcorrection_note: 今日 뒤에 は가 없다고 해서 항상 오류는 아니다. 의미가 자연스럽다면 교정보다는 더 자연스러운 표현 제안으로만 다룬다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #221 (ID: 230)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `資料の作成が終わりましたら、一度チェックをお願いいたします。` |
| **서버 AI 최종 교정본** | **資料の作成が終わりましたら、一度チェックをお願いいたします。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미가 올바르며, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語で、文法や意味が正しいため、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[一]
- matched_form: 一
- reading: いち
- meaning: one
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #222 (ID: 231)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `来月のスケジュールについて、調整が必要な部分があります。` |
| **서버 AI 최종 교정본** | **来月のスケジュールについて、調整が必要な部分があります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 교정이 필요 없습니다.
- **일본어 해설:** 文は自然で文法的に正しいです。修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[来月]
- matched_form: 来月
- reading: らいげつ
- meaning: next month
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #223 (ID: 232)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お手数をおかけしますが、こちらの書類にサインをお願いします。` |
| **서버 AI 최종 교정본** | **お手数をおかけしますが、こちらの書類にサインをお願いします。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 요청 표현이 올바르고 문법적으로도 정확합니다.
- **일본어 해설:** この文は自然な日本語で、請求表現も適切で文法的に正しいです。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[こちら]
- matched_form: こちら
- reading: こちら
- meaning: this person (polite); this way (polite)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #224 (ID: 233)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `駅から会社までは歩いて十五分ほどかかります。` |
| **서버 AI 최종 교정본** | **駅から会社までは歩いて十五分ほどかかります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 적절합니다.
- **일본어 해설:** この文は自然な日本語であり、意味と文法的に適切です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[駅]
- matched_form: 駅
- reading: えき
- meaning: station
- level: N5

[会社]
- matched_form: 会社
- reading: かいしゃ
- meaning: company, corporation
- level: N5

[では]
- matched_form: では
- reading: では
- meaning: then, well, so
- level: N5

[十]
- matched_form: 十
- reading: (〜を) とお
- meaning: ten (~)
- level: N5

[五]
- matched_form: 五
- reading: ご
- meaning: five
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

--- 

## 📌 발화 샘플 데이터 #225 (ID: 234)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `先ほどお送りしたメール의 첨부파일을 확인해 주세요.` |
| **서버 AI 최종 교정본** | **先ほどお送りしたメールの添付ファイルを確認してください。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 표현이 올바릅니다.
- **일본어 해설:** 文は自然な日本語で、意味と表現が適切です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[先]
- matched_form: 先
- reading: さき
- meaning: future; recent, previous
- level: N5
```

--- 

## 📌 발화 샘플 데이터 #226 (ID: 235)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `本日の営業時間は午後八時をもちまして終了いたしました。` |
| **서버 AI 최종 교정본** | **本日の営業時間は午後八時をもちまして終了いたしました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現が正確であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5

[八]
- matched_form: 八
- reading: はち
- meaning: eight
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #227 (ID: 236)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新しいクライアントとの打ち合わせは来週の水曜日です。` |
| **서버 AI 최종 교정본** | **新しいクライアントとの打ち合わせは来週の水曜日です。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미가 올바르며 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味において誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5

[来週]
- matched_form: 来週
- reading: らいしゅう
- meaning: next week
- level: N5

[水曜日]
- matched_form: 水曜日
- reading: すいようび
- meaning: Wednesday
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_002] 名詞 + を + 食べる/飲む
- rule_type: reference
- level: N5
- pattern: 名詞 + を + 食べる/飲む
- description_ko: 먹거나 마시는 대상에는 조사 を를 붙이는 경우가 일반적이다.
- reference_examples: 水を飲みます, ご飯を食べます
- possible_focus: 목적어 표현, 조사 を 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확한 단편 발화는 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[word_choice_error] 단어 선택 오류
- description_ko: 동사와 명사의 의미 조합이 어색하거나 다른 단어가 더 적절할 가능성이 있는 경우이다.
- related_focus: 단어 선택, 동사와 목적어의 의미 관계
- reference_examples:
  - observed: 水を食べます
    reference: 水を飲みます
  - observed: ラーメンを飲みます
    reference: ラーメンを食べます
- overcorrection_note: 비유적 표현이나 특수 문맥일 수 있으므로, 단어 조합만 보고 기계적으로 오류 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #228 (ID: 237)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ここを真っ直ぐ行って、二つ目の交差点を右に曲がると駅があります。` |
| **서버 AI 최종 교정본** | **ここを真っ直ぐ行って、二つ目の交差点を右に曲がると駅があります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미가 올바르며 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語で、文法や意味が正しいため誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ここ]
- matched_form: ここ
- reading: ここ
- meaning: here, this place
- level: N5

[二つ]
- matched_form: 二つ
- reading: ふたつ
- meaning: two things
- level: N5

[目]
- matched_form: 目
- reading: め
- meaning: eye(s)
- level: N5

[交差点]
- matched_form: 交差点
- reading: こうさてん
- meaning: intersection
- level: N5

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5

[駅]
- matched_form: 駅
- reading: えき
- meaning: station
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #229 (ID: 238)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `横断歩道を渡ってから、左側に大きなビルが見えてきます。` |
| **서버 AI 최종 교정본** | **横断歩道を渡ってから、左側に大きなビルが見えてきます。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 교정이 필요 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[横]
- matched_form: 横
- reading: よこ
- meaning: beside; side; width
- level: N5

[道]
- matched_form: 道
- reading: みち
- meaning: road, street; way, directions
- level: N5

[左]
- matched_form: 左
- reading: ひだり
- meaning: left hand side
- level: N5

[大きな]
- matched_form: 大きな
- reading: おおきな
- meaning: big
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #230 (ID: 239)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新宿駅の東口を出て、五分ほど歩いたところにあります。` |
| **서버 AI 최종 교정본** | **新宿駅の東口を出て、五分ほど歩いたところにあります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[駅]
- matched_form: 駅
- reading: えき
- meaning: station
- level: N5

[東]
- matched_form: 東
- reading: ひがし
- meaning: east
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5

[五]
- matched_form: 五
- reading: ご
- meaning: five
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #231 (ID: 240)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `そのビルの地下にある喫茶店は、とても雰囲気が良いです。` |
| **서버 AI 최종 교정본** | **そのビルの地下にある喫茶店は、とても雰囲気が良いです。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現が正確であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[その]
- matched_form: その
- reading: その
- meaning: that
- level: N5

[下]
- matched_form: 下
- reading: した
- meaning: under, below, beneath
- level: N5

[喫茶店]
- matched_form: 喫茶店
- reading: きっさてん
- meaning: café
- level: N5

[とても]
- matched_form: とても
- reading: とても
- meaning: very (much), greatly, exceedingly
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #232 (ID: 241)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `信号を渡らずに、手前の角を左に曲がってください。` |
| **서버 AI 최종 교정본** | **信号を渡らずに、手前の角を左に曲がってください。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미가 올바르며, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味において誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[前]
- matched_form: 前
- reading: まえ
- meaning: before, in front
- level: N5

[角]
- matched_form: 角
- reading: かど
- meaning: corner (e.g., desk, pavement)
- level: N5

[左]
- matched_form: 左
- reading: ひだり
- meaning: left hand side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #233 (ID: 242)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ホテルの向かい側に、二十四時間営業 of コンビニがあります。` |
| **서버 AI 최종 교정본** | **ホテルの向かい側に、二十四時間営業のコンビニがあります。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장의 의미는 자연스럽지만, '二十四時間営業 of コンビニ'는 문법적으로 부정확합니다. 'of' 대신 'の'를 사용해야 하며, 이는 조사 오용입니다. '二十四時間営業のコンビニ'는 자연스러운 표현입니다.
- **일본어 해설:** 文の意味は自然ですが、「二十四時間営業 of コンビニ」は文法的に不正確です。代わりに「二十四時間営業のコンビニ」とすべきで、これは助詞の誤用です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ホテル]
- matched_form: ホテル
- reading: ホテル
- meaning: hotel
- level: N5

[二]
- matched_form: 二
- reading: に
- meaning: two
- level: N5

[十]
- matched_form: 十
- reading: (〜を) とお
- meaning: ten (~)
- level: N5

[四]
- matched_form: 四
- reading: し
- meaning: four
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #234 (ID: 243)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `この道をずっと進むと、突き当たりに大きな公園が見えます。` |
| **서버 AI 최종 교정본** | **この道をずっと進むと、突き当たりに大きな公園が見えます。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 교정이 필요 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[この]
- matched_form: この
- reading: この
- meaning: this
- level: N5

[道]
- matched_form: 道
- reading: みち
- meaning: road, street; way, directions
- level: N5

[大きな]
- matched_form: 大きな
- reading: おおきな
- meaning: big
- level: N5

[公園]
- matched_form: 公園
- reading: こうえん
- meaning: a park
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #235 (ID: 244)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `階段を上って二階に上がると、右手に受付がございます。` |
| **서버 AI 최종 교정본** | **階段を上って二階に上がると、右手に受付がございます。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제 없음.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[階段]
- matched_form: 階段
- reading: かいだん
- meaning: stairs
- level: N5

[上]
- matched_form: 上
- reading: うえ
- meaning: above (up, top, etc.), over, on top of
- level: N5

[二]
- matched_form: 二
- reading: に
- meaning: two
- level: N5

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #236 (ID: 245)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `北口の改札を出てすぐのところに、案内図が設置されています。` |
| **서버 AI 최종 교정본** | **北口の改札を出てすぐのところに、案内図が設置されています。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 교정이 필요하지 않습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[北]
- matched_form: 北
- reading: きた
- meaning: north
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #237 (ID: 246)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `駐車場の入り口は、建物の裏側にございますのでご注意ください。` |
| **서버 AI 최종 교정본** | **駐車場の入り口は、建物の裏側にございますのでご注意ください。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미가 올바르며, 교정이 필요 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味に問題はありません。修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[車]
- matched_form: 車
- reading: くるま
- meaning: car, vehicle
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5

[建物]
- matched_form: 建物
- reading: たてもの
- meaning: building
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #238 (ID: 247)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `図書館に行って勉強をしましたが、あまり集中できませんでした。` |
| **서버 AI 최종 교정본** | **図書館に行って勉強をしましたが、あまり集中できませんでした。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現が正確であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[図書館]
- matched_form: 図書館
- reading: としょかん
- meaning: library
- level: N5

[勉強]
- matched_form: 勉強
- reading: べんきょう (する)
- meaning: study
- level: N5

[中]
- matched_form: 中
- reading: なか
- meaning: inside, middle, among
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 6 (keyword_match_count=4, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #239 (ID: 248)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `友達と一緒に美味しいお寿司を食べに行きました。` |
| **서버 AI 최종 교정본** | **友達と一緒に美味しいお寿司を食べに行きました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미가 올바르며 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味において誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[友達]
- matched_form: 友達
- reading: ともだち
- meaning: friend
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5

[美味しい]
- matched_form: 美味しい
- reading: おいしい
- meaning: delicious, tasty
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #240 (ID: 249)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `週末に家族と一緒に映画館へ行って、話題の映画を見ました。` |
| **서버 AI 최종 교정본** | **週末に家族と一緒に映画館へ行って、話題の映画を見ました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 올바르며, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味ともに正しいため、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[家族]
- matched_form: 家族
- reading: かぞく
- meaning: family, members of a family
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5

[映画館]
- matched_form: 映画館
- reading: えいがかん
- meaning: movie theater, cinema
- level: N5

[話]
- matched_form: 話
- reading: はなし
- meaning: talk (chat), story
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #241 (ID: 250)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `先生に質問をしたら、とても親切に教えてくれました。` |
| **서버 AI 최종 교정본** | **先生に質問をしたら、とても親切に教えてくれました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[先生]
- matched_form: 先生
- reading: せんせい
- meaning: teacher, professor; master; doctor
- level: N5

[質問]
- matched_form: 質問
- reading: しつもん
- meaning: question, inquiry
- level: N5

[とても]
- matched_form: とても
- reading: とても
- meaning: very (much), greatly, exceedingly
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #242 (ID: 251)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `病院の予約が十時なので、急いで行かなければなりません。` |
| **서버 AI 최종 교정본** | **病院の予約が十時なので、急いで行かなければなりません。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 올바르며 교정이 필요 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味ともに正しいため、修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[病院]
- matched_form: 病院
- reading: びょういん
- meaning: hospital
- level: N5

[十]
- matched_form: 十
- reading: (〜を) とお
- meaning: ten (~)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[verb_conjugation_error] 동사 활용 오류
- description_ko: 동사의 기본형, ます형, 부정형, 희망형 등이 문법적으로 어색하게 결합된 가능성이 있는 경우이다.
- related_focus: 동사 활용, ます형, 부정형, 희망 표현
- reference_examples:
  - observed: 食べますない
    reference: 食べません
  - observed: 行くたいです
    reference: 行きたいです
- overcorrection_note: 반말체와 정중체가 혼재된 문장은 문체 기준을 먼저 확인하고, 학습 목적에 따라 제안 수준으로 다룬다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #243 (ID: 252)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `飛行機のチケットをインターネットで予約しました。` |
| **서버 AI 최종 교정본** | **飛行機のチケットをインターネットで予約しました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[飛行機]
- matched_form: 飛行機
- reading: ひこうき
- meaning: airplane
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #244 (ID: 253)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `昨日はたくさん歩いたので、足がとても疲れました。` |
| **서버 AI 최종 교정본** | **昨日はたくさん歩いたので、足がとても疲れました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現が正確であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[昨日]
- matched_form: 昨日
- reading: きのう
- meaning: yesterday
- level: N5

[足]
- matched_form: 足
- reading: あし
- meaning: foot; leg
- level: N5

[とても]
- matched_form: とても
- reading: とても
- meaning: very (much), greatly, exceedingly
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #245 (ID: 254)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `毎日日本語の単語を五十個ずつ覚えるようにしています。` |
| **서버 AI 최종 교정본** | **毎日日本語の単語を五十個ずつ覚えるようにしています。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로 올바릅니다. 오류가 없습니다.
- **일본어 해설:** この文は自然で、文法的に正しいです。誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[毎日]
- matched_form: 毎日
- reading: まいにち
- meaning: every day
- level: N5

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[五]
- matched_form: 五
- reading: ご
- meaning: five
- level: N5

[十]
- matched_form: 十
- reading: (〜を) とお
- meaning: ten (~)
- level: N5

[覚える]
- matched_form: 覚える
- reading: おぼえる
- meaning: to learn, to commit to memory, to remember, to memorize
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #246 (ID: 255)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お茶を飲みながら、これからの計画について話し合いました。` |
| **서버 AI 최종 교정본** | **お茶を飲みながら、これからの計画について話し合いました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現が正確であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[お茶]
- matched_form: お茶
- reading: おちゃ
- meaning: (green) tea
- level: N5

[これ]
- matched_form: これ
- reading: これ
- meaning: this one
- level: N5

[話]
- matched_form: 話
- reading: はなし
- meaning: talk (chat), story
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #247 (ID: 256)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `自転車に乗って近くの公園まで遊びに行きました。` |
| **서버 AI 최종 교정본** | **自転車に乗って近くの公園まで遊びに行きました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現が正確であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[自転車]
- matched_form: 自転車
- reading: じてんしゃ
- meaning: bicycle
- level: N5

[近く]
- matched_form: 近く
- reading: ちかく
- meaning: nearby; in the neighborhood
- level: N5

[公園]
- matched_form: 公園
- reading: こうえん
- meaning: a park
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #248 (ID: 257)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `東京特許許可局の局長が、今日新しいプロジェクトを発表しました。` |
| **서버 AI 최종 교정본** | **東京特許許可局の局長が、今日新しいプロジェクトを発表しました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 추가적인 교정이 필요하지 않습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。追加の修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[東]
- matched_form: 東
- reading: ひがし
- meaning: east
- level: N5

[今日]
- matched_form: 今日
- reading: きょう
- meaning: today, this day
- level: N5

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_003] 今日 + は
- rule_type: soft_reference
- level: N5
- pattern: 今日 + は
- description_ko: 今日를 문장의 화제로 사용할 때 は를 붙여 今日は 형태로 쓰는 경우가 있다.
- reference_examples: 今日は学校に行きました
- possible_focus: 화제 표현, は 사용 여부, 자연스러운 문장 흐름
- possible_error_types: unnatural_expression
- overcorrection_note: 今日 뒤에 は가 없다고 해서 항상 오류는 아니다. 의미가 자연스럽다면 교정보다는 더 자연스러운 표현 제안으로만 다룬다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #249 (ID: 258)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新人歌手の新春シャンソンショーが、まもなく開催されます。` |
| **서버 AI 최종 교정본** | **新人歌手の新春シャンソンショーが、まもなく開催されます。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[人]
- matched_form: 人
- reading: ひと
- meaning: man, person
- level: N5

[歌]
- matched_form: 歌
- reading: うた
- meaning: a song
- level: N5

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[春]
- matched_form: 春
- reading: はる
- meaning: spring
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #250 (ID: 259)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `隣の客はよく柿食う客だという有名な言葉があります。` |
| **서버 AI 최종 교정본** | **隣の客はよく柿を食う客だという有名な言葉があります。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '柿食う'는 자연스러운 표현이 아니며, '柿を食う'로 조사 'を'를 추가해야 합니다. '柿食う'는 오류로, '柿を食う'로 교정해야 합니다.
- **일본어 해설:** 「柿食う」という表現は自然ではありません。正しい表現は「柿を食う」です。文法的に不自然な部分を修正しています。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[隣]
- matched_form: 隣
- reading: となり
- meaning: next to, next door to
- level: N5

[よく]
- matched_form: よく
- reading: よく
- meaning: frequently, often (much); well, skillfully
- level: N5

[有名]
- matched_form: 有名
- reading: ゆうめい
- meaning: famous
- level: N5

[言葉]
- matched_form: 言葉
- reading: ことば
- meaning: language; word(s); expression(s)
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #251 (ID: 260)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `坊主が屏風に上手に坊主の絵を描いたそうです。` |
| **서버 AI 최종 교정본** | **坊主が屏風に上手に坊主の絵を描いたそうです。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[風]
- matched_form: 風
- reading: かぜ
- meaning: wind, breeze
- level: N5

[上手]
- matched_form: 上手
- reading: じょうず
- meaning: be good at, skillful
- level: N5

[絵]
- matched_form: 絵
- reading: え
- meaning: a painting; a picture; a drawing
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #252 (ID: 261)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `赤パプリカ黄パプリカ青パプリカを市場でたくさん買いました。` |
| **서버 AI 최종 교정본** | **赤パプリカ黄パプリカ青パプリカを市場でたくさん買いました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로도 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で、文法的にも正しいです。意味と表現は正確で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[赤]
- matched_form: 赤
- reading: あか
- meaning: red
- level: N5

[青]
- matched_form: 青
- reading: あお
- meaning: blue
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #253 (ID: 262)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `バスガス爆発という言葉を三回続けて言うのは難しいです。` |
| **서버 AI 최종 교정본** | **バスガス爆発という言葉を三回続けて言うのは難しいです。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[バス]
- matched_form: バス
- reading: バス
- meaning: bus; bath; bass
- level: N5

[言葉]
- matched_form: 言葉
- reading: ことば
- meaning: language; word(s); expression(s)
- level: N5

[三]
- matched_form: 三
- reading: さん
- meaning: three
- level: N5

[言う]
- matched_form: 言う
- reading: いう
- meaning: to say
- level: N5

[難しい]
- matched_form: 難しい
- reading: むずかしい
- meaning: difficult
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #254 (ID: 263)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `右目右耳右耳右目と順番に触る運動をしてください。` |
| **서버 AI 최종 교정본** | **右目、右耳、右耳、右目と順番に触る運動をしてください。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '右目右耳右耳右目'처럼 반복되는 표현은 의미상 자연스럽지 않으며, 각 항목 사이에 쉼표를 넣어 구분하는 것이 더 자연스러운 표현입니다. 조사 'と'는 '順番に'와 함께 사용할 때 문맥상 적절하지 않으며, 'と'를 제거하고 '、'를 사용하는 것이 더 자연스럽습니다.
- **일본어 해설:** 「右目右耳右耳右目」という繰り返し表現は意味的に自然ではありません。各項目の間にはコンマを挿入し、区別を明確にすることが自然な表現です。「と」は「順番に」と一緒に使うと文脈的に不自然であり、「、」を使用するのが適切です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5

[目]
- matched_form: 目
- reading: め
- meaning: eye(s)
- level: N5

[耳]
- matched_form: 耳
- reading: みみ
- meaning: ear
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #255 (ID: 264)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `骨粗鬆症の予防のために、毎日カルシウムを摂取しています。` |
| **서버 AI 최종 교정본** | **骨粗鬆症の予防のために、毎日カルシウムを摂取しています。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미도 명확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味も明確で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[毎日]
- matched_form: 毎日
- reading: まいにち
- meaning: every day
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #256 (ID: 265)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `輸出工場輸出効率の向上に向けた新しい会議を行います。` |
| **서버 AI 최종 교정본** | **輸出工場の輸出効率の向上に向けた新しい会議を行います。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '輸出工場輸出効率'는 조사가 부족하여 의미가 모호합니다. '輸出工場の'으로 조사를 추가하면 자연스러운 표현이 됩니다.
- **일본어 해설:** 「輸出工場輸出効率」は助詞が欠けているため意味が不明です。『輸出工場の』と助詞を追加すると自然な表現になります。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[上]
- matched_form: 上
- reading: うえ
- meaning: above (up, top, etc.), over, on top of
- level: N5

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #257 (ID: 266)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `暖かかったから上着を脱いで散歩に出かけました。` |
| **서버 AI 최종 교정본** | **暖かかったから上着を脱いで散歩に出かけました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[上着]
- matched_form: 上着
- reading: うわぎ
- meaning: coat, jacket
- level: N5

[散歩]
- matched_form: 散歩
- reading: さんぽ (する)
- meaning: walk, stroll
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #258 (ID: 267)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `来週の旅行なんだど、天気が悪そうなら予定を変更した方がいいんじゃない？` |
| **서버 AI 최종 교정본** | **来週の旅行が悪そうなら、予定を変更した方がいいんじゃない？** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '天気が悪そうなら'는 자연스러운 표현이지만, '天気'과 '方'이 함께 사용된 '天気が悪そうなら'는 문법적으로 부적절합니다. 'が'를 사용하여 '旅行が悪そう'으로 바꾸면 문맥상 더 자연스러워집니다.
- **일본어 해설:** 「天気が悪そうなら」という表現は文法的に不自然です。文脈上、「旅行が悪そう」にすると自然になります。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[来週]
- matched_form: 来週
- reading: らいしゅう
- meaning: next week
- level: N5

[旅行]
- matched_form: 旅行
- reading: りょこう
- meaning: travel, trip
- level: N5

[天気]
- matched_form: 天気
- reading: てんき
- meaning: weather
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5

[方]
- matched_form: 方
- reading: かた
- meaning: -- honorific form for 人 (ひと) --; way of doing
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5

[じゃ]
- matched_form: じゃ
- reading: じゃ; じゃあ
- meaning: well, well then
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #259 (ID: 268)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お腹空いたし、近くのレストランで何か温かいものでも食べない？` |
| **서버 AI 최종 교정본** | **お腹空いたし、近くのレストランで何か温かいものでも食べない？** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미가 명확하고 자연스러운 회화 표현입니다. 문법적으로도 문제 없으며, STT 인식 결과로 보는 것이 자연스러운 표현입니다.
- **일본어 해설:** この文は意味が明確で、自然な会話表現です。文法的に問題なく、STT認識結果として自然な表現です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[お腹]
- matched_form: お腹
- reading: おなか
- meaning: stomach
- level: N5

[空]
- matched_form: 空
- reading: そら
- meaning: sky
- level: N5

[近く]
- matched_form: 近く
- reading: ちかく
- meaning: nearby; in the neighborhood
- level: N5

[レストラン]
- matched_form: レストラン
- reading: レストラン
- meaning: restaurant
- level: N5

[何]
- matched_form: 何
- reading: なん; なに
- meaning: what
- level: N5

[でも]
- matched_form: でも
- reading: でも
- meaning: but, however
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 2 (keyword_match_count=2, type_match_score=0)

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #260 (ID: 269)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `明日の約束の時間に遅れそうなら、速攻で連れてって下さい。` |
| **서버 AI 최종 교정본** | **明日の約束の時間に遅れそうなら、速攻で連れてって下さい。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[明日]
- matched_form: 明日
- reading: あした
- meaning: tomorrow
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[そう]
- matched_form: そう
- reading: そう; そうです
- meaning: yes; appears, to be the case
- level: N5

[下さい]
- matched_form: 下さい
- reading: ください
- meaning: (with te-form verb) please do for me
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #261 (ID: 270)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `最近仕事忙しくてさ、週末ゆっくり休む時間まじでないわ。` |
| **서버 AI 최종 교정본** | **最近仕事忙しくてさ、週末ゆっくり休む時間はまじでないわ。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '時間まじでない'은 자연스러운 표현이 아니며, '時間はまじでない'으로 조사 'は'를 추가하여 문법적으로 자연스러운 표현으로 수정했습니다.
- **일본어 해설:** 「時間まじでない」は自然な表現ではありません。文法的に自然な表現にするために「時間はまじでない」として、助詞「は」を追加しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[仕事]
- matched_form: 仕事
- reading: しごと
- meaning: work, job, occupation, employment
- level: N5

[休む]
- matched_form: 休む
- reading: やすむ
- meaning: to rest, to have a break, to get time off
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

--- 

## 📌 발화 샘플 데이터 #262 (ID: 271)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `この服デザインはいいけど、ちょっとサイズ小さい気がする。` |
| **서버 AI 최종 교정본** | **この服のデザインはいいけど、ちょっとサイズが小さい気がする。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미가 자연스럽지만, 'サイズ小さい'보다 'サイズが小さい'로 조사 'が'를 추가하면 문법적으로 더 자연스러워집니다.
- **일본어 해설:** 文は意味は自然ですが、「サイズ小さい」ではなく「サイズが小さい」という形に「が」を追加することで文法的に自然になります。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[この]
- matched_form: この
- reading: この
- meaning: this
- level: N5

[服]
- matched_form: 服
- reading: ふく
- meaning: clothes
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5

[ちょっと]
- matched_form: ちょっと
- reading: ちょっと
- meaning: a little, somewhat; just a little, somewhat
- level: N5

[小さい]
- matched_form: 小さい
- reading: ちいさい
- meaning: small, little
- level: N5

[する]
- matched_form: する
- reading: する
- meaning: to do, to try; to wear small items (e.g., necktie, watch, etc.)
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #263 (ID: 272)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `友達の誕生日に何を、何をプレゼントしたらいいか悩んでる。` |
| **서버 AI 최종 교정본** | **友達の誕生日に何を、何をプレゼントしたらいいか悩んでる。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[友達]
- matched_form: 友達
- reading: ともだち
- meaning: friend
- level: N5

[誕生日]
- matched_form: 誕生日
- reading: たんじょうび
- meaning: birthday
- level: N5

[何]
- matched_form: 何
- reading: なん; なに
- meaning: what
- level: N5

[いい]
- matched_form: いい
- reading: いい; よい
- meaning: good
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #264 (ID: 273)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `映画見に行きたいんだけど、一緒に行く人おらんくて困ってる。` |
| **서버 AI 최종 교정본** | **映画見に行きたいんだけど、一緒に行ける人いないんだけど困ってる。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '一緒に行く人おらんくて困ってる' 부분에서 'おらんくて'는 자연스러운 표현이 아니며, 'いないんだけど'로 교정하는 것이 더 자연스러운 표현입니다. 'おらんくて'는 'いない'의 오류 표현으로, 조사 사용이 잘못된 것으로 판단됩니다.
- **일본어 해설:** 「一緒に行く人おらんくて困ってる」という表現は自然ではありません。正しい表現は「一緒に行く人がいないんだけど困ってる」です。『おらんくて』は『いないんだけど』に修正すべきであり、これは助詞の誤用です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[映画]
- matched_form: 映画
- reading: えいが
- meaning: movie, film
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5

[行く]
- matched_form: 行く
- reading: いく; ゆく
- meaning: to go
- level: N5

[人]
- matched_form: 人
- reading: ひと
- meaning: man, person
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_008] 〜たいです 희망 표현
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + たいです
- description_ko: 하고 싶은 일을 말할 때 동사의 ます형 어간에 たいです를 붙이는 경우가 많다.
- reference_examples: 食べたいです, 行きたいです
- possible_focus: 희망 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 희망 표현이 아닌 단순 서술문을 억지로 たい 형태로 해석하지 않는다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #265 (ID: 274)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `日本の文化に興味あるから、いつかきょとに行ってみたい。` |
| **서버 AI 최종 교정본** | **日本の文化に興味があるから、いつか日本に旅行したい。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문법적으로 완전히 틀렸다고 보기는 어렵지만, 더 자연스러운 표현으로 수정했습니다.
- **일본어 해설:** 文法的に完全な誤りとは言い切れませんが、より自然な表現に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[いつ]
- matched_form: いつ
- reading: いつ
- meaning: when
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_008] 〜たいです 희망 표현
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + たいです
- description_ko: 하고 싶은 일을 말할 때 동사의 ます형 어간에 たいです를 붙이는 경우가 많다.
- reference_examples: 食べたいです, 行きたいです
- possible_focus: 희망 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 희망 표현이 아닌 단순 서술문을 억지로 たい 형태로 해석하지 않는다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #266 (ID: 275)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `コーヒーを飲みながら、静カフェで本を読むのが好き。` |
| **서버 AI 최종 교정본** | **コーヒーを飲みながら、静カフェで本を読むのが好きです。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. '好き' 뒤에 'です'를 추가하면 더 자연스러운 표현이 됩니다. 그러나 학습자 문장으로서는 생략된 경우도 자연스러울 수 있으므로, 수정하지 않습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。'好き'の後に'です'を加えるとより自然になりますが、学習者の発話では省略された形も自然に聞こえるため、修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[コーヒー]
- matched_form: コーヒー
- reading: コーヒー
- meaning: coffee
- level: N5

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[読む]
- matched_form: 読む
- reading: よむ
- meaning: to read
- level: N5

[好き]
- matched_form: 好き
- reading: すき
- meaning: liking, fondness, love
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #267 (ID: 276)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `終電の時間確認しとかないと、帰れなくなるかも。` |
| **서버 AI 최종 교정본** | **終電の時間確認しとかないと、帰れなくなるかも。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5

[なる]
- matched_form: なる
- reading: なる
- meaning: to become
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

--- 

## 📌 발화 샘플 데이터 #268 (ID: 277)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `明日の会議は午後さんじはんからに変更になったので。` |
| **서버 AI 최종 교정본** | **明日の会議は午後三時からに変更になったので。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문맥상 사용된 조사가 적절하지 않아 더 자연스러운 조사로 수정했습니다.
- **일본어 해설:** 文脈上、使われている助詞が適切ではなかったため、より自然な助詞に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[明日]
- matched_form: 明日
- reading: あした
- meaning: tomorrow
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #269 (ID: 278)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `提出期限は今週の金曜日の午後五時までととなっております。` |
| **서버 AI 최종 교정본** | **提出期限は今週の金曜日の午後五時までととなっております。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 문제 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味において問題ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[今週]
- matched_form: 今週
- reading: こんしゅう
- meaning: this week
- level: N5

[金曜日]
- matched_form: 金曜日
- reading: きんようび
- meaning: Friday
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5

[五]
- matched_form: 五
- reading: ご
- meaning: five
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

--- 

## 📌 발화 샘플 데이터 #270 (ID: 279)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `今回のぽろじぇくとの予算案、今日中に確認してメールして。` |
| **서버 AI 최종 교정본** | **今回のポロジェクトの予算案、今日中に確認してメールします。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장의 자연스러운 표현을 위해 '確認してメールして'를 '確認してメールします'으로 수정했습니다. '今日中に'은 의미상 자연스럽지만, 'メールして'는 명령형으로 문맥상 부적절합니다. 명령형보다는 제안형 'メールします'이 더 자연스러운 표현입니다.
- **일본어 해설:** 文の自然な表現のために、「確認してメールして」という表現を「確認してメールします」と修正しました。「今日中に」は意味的には自然ですが、「メールして」は文脈上不自然です。命令形ではなく、提案形の「メールします」がより自然です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[今]
- matched_form: 今
- reading: いま
- meaning: now
- level: N5

[今日]
- matched_form: 今日
- reading: きょう
- meaning: today, this day
- level: N5

[中]
- matched_form: 中
- reading: なか
- meaning: inside, middle, among
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_003] 今日 + は
- rule_type: soft_reference
- level: N5
- pattern: 今日 + は
- description_ko: 今日를 문장의 화제로 사용할 때 は를 붙여 今日は 형태로 쓰는 경우가 있다.
- reference_examples: 今日は学校に行きました
- possible_focus: 화제 표현, は 사용 여부, 자연스러운 문장 흐름
- possible_error_types: unnatural_expression
- overcorrection_note: 今日 뒤에 は가 없다고 해서 항상 오류는 아니다. 의미가 자연스럽다면 교정보다는 더 자연스러운 표현 제안으로만 다룬다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[unnatural_expression] 어색한 표현
- description_ko: 문법적으로 완전히 틀렸다고 단정하기는 어렵지만, 학습자 문장으로서 더 자연스러운 표현이 있을 수 있는 경우이다.
- related_focus: 자연스러움, 화제 표현, 정중체
- reference_examples:
  - observed: 今日学校に行きました
    reference: 今日は学校に行きました
  - observed: これは何
    reference: これは何ですか
- overcorrection_note: 자연스러운 대안 제안과 오류 판정을 구분해야 한다. 의미가 통하고 회화적으로 자연스러우면 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #271 (ID: 280)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `資料の作成が終わったら、一回チェックして下さい。` |
| **서버 AI 최종 교정본** | **資料の作成が終わったら、一回チェックして下さい。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[一]
- matched_form: 一
- reading: いち
- meaning: one
- level: N5

[下さい]
- matched_form: 下さい
- reading: ください
- meaning: (with te-form verb) please do for me
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #272 (ID: 281)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `来月のスケジュール、調整が必要なとこあります。` |
| **서버 AI 최종 교정본** | **来月のスケジュール、調整が必要なところがあります。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미상 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、文法や意味上の問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[来月]
- matched_form: 来月
- reading: らいげつ
- meaning: next month
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #273 (ID: 282)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お手数かけますが、こっちの書類にサインお願いします。` |
| **서버 AI 최종 교정본** | **お手数ですが、こっちの書類にサインをお願いします。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미는 자연스럽지만, 'サイン'을 요청할 때 'を'를 생략하고 있습니다. 'サイン'을 요청할 경우 'を'를 붙여 더 자연스러운 표현으로 수정했습니다.
- **일본어 해설:** 文の意味は自然ですが、「サイン」を要求する場合、「を」を省略しています。より自然な表現として「を」を追加しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[こっち]
- matched_form: こっち
- reading: こっち
- meaning: this person; this direction; this side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #274 (ID: 283)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `駅から会社までは歩いてじゅうごふんくらいかかります。` |
| **서버 AI 최종 교정본** | **駅から会社までは歩いてじゅうごふんくらいかかります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[駅]
- matched_form: 駅
- reading: えき
- meaning: station
- level: N5

[会社]
- matched_form: 会社
- reading: かいしゃ
- meaning: company, corporation
- level: N5

[では]
- matched_form: では
- reading: では
- meaning: then, well, so
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

--- 

## 📌 발화 샘플 데이터 #275 (ID: 284)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `さっき送ったメールのてんぷふぁいる見てください。` |
| **서버 AI 최종 교정본** | **さっき送ったメールのテンプファイルを見てください。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미는 자연스럽지만, 'てんぷふぁいる'이 'テンプファイル'로 교정되어야 하며, 'を見てください'는 자연스러운 표현입니다. 'てんぷふぁいる'은 오류가 있는 발음이므로 교정하였습니다.
- **일본어 해설:** 文の意味は自然ですが、「てんぷふぁいる」は誤った発音であり、「テンプファイル」として修正しました。また、「を見てください」は自然な表現です。

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[overcorrection_risk] 과교정 위험
- description_ko: 정상적인 회화 표현, 인사, 단편 응답, 문맥상 가능한 생략 표현을 불필요하게 고칠 위험이 있는 경우이다.
- related_focus: 과교정 방지, 회화체, 단편 발화
- reference_examples:
  - observed: こんにちは
    reference: こんにちは
  - observed: 水ください
    reference: 水ください
- overcorrection_note: 정상 표현은 수정하지 않는다. 특히 greeting, fragment, soft_reference는 교정 대상이 아니라 참고 대상으로 둔다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #276 (ID: 285)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `本日の営業時間は午後八時で終了しました。` |
| **서버 AI 최종 교정본** | **本日の営業時間は午後八時で終了しました。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味と表現が正確であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[時間]
- matched_form: 時間
- reading: じかん
- meaning: time
- level: N5

[午後]
- matched_form: 午後
- reading: ごご
- meaning: afternoon, P.M.
- level: N5

[八]
- matched_form: 八
- reading: はち
- meaning: eight
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #277 (ID: 286)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新しいくらいあんととの打ち合わせは来週の水曜。` |
| **서버 AI 최종 교정본** | **新しいくらいのあんととの打ち合わせは来週の水曜日です。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 85.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '水曜'가 '水曜日'로 완성되어야 하며, 'あんととの'는 'あんととの'가 아니라 'あんととの'가 자연스러운 표현이지만, '打ち合わせ'와 '水曜'의 조합은 어색합니다. '水曜'는 '水曜日'로 완성되어야 하며, 조사 'を'가 생략되어 있어 문장 구조가 불분명합니다.
- **일본어 해설:** 文の「水曜」は「水曜日」として完成すべきであり、「あんととの」は自然な表現ですが、「打ち合わせ」と「水曜」の組み合わせは不自然です。また、「水曜」の後に「を」が省略されており、文の構造が不明です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5

[来週]
- matched_form: 来週
- reading: らいしゅう
- meaning: next week
- level: N5

[水]
- matched_form: 水
- reading: みず
- meaning: water
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_002] 名詞 + を + 食べる/飲む
- rule_type: reference
- level: N5
- pattern: 名詞 + を + 食べる/飲む
- description_ko: 먹거나 마시는 대상에는 조사 を를 붙이는 경우가 일반적이다.
- reference_examples: 水を飲みます, ご飯を食べます
- possible_focus: 목적어 표현, 조사 を 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확한 단편 발화는 오류로 단정하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_009] ください 요청 표현
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + を + ください
- description_ko: 무언가를 달라고 요청할 때 명사 뒤에 を를 붙이고 ください를 사용할 수 있다.
- reference_examples: 水をください, これをください
- possible_focus: 요청 표현, 조사 を 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 水ください처럼 회화에서 자연스럽게 쓰이는 생략 표현은 무조건 오류로 단정하지 않는다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[word_choice_error] 단어 선택 오류
- description_ko: 동사와 명사의 의미 조합이 어색하거나 다른 단어가 더 적절할 가능성이 있는 경우이다.
- related_focus: 단어 선택, 동사와 목적어의 의미 관계
- reference_examples:
  - observed: 水を食べます
    reference: 水を飲みます
  - observed: ラーメンを飲みます
    reference: ラーメンを食べます
- overcorrection_note: 비유적 표현이나 특수 문맥일 수 있으므로, 단어 조합만 보고 기계적으로 오류 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #278 (ID: 287)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ここをますぐ行って、二つ目の交差点を右に曲がると。` |
| **서버 AI 최종 교정본** | **ここをすぐ行って、二つ目の交差点を右に曲がると。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로도 올바릅니다. 교정이 필요하지 않습니다.
- **일본어 해설:** この文は自然で、文法的にも正しいです。修正は必要ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ここ]
- matched_form: ここ
- reading: ここ
- meaning: here, this place
- level: N5

[二つ]
- matched_form: 二つ
- reading: ふたつ
- meaning: two things
- level: N5

[目]
- matched_form: 目
- reading: め
- meaning: eye(s)
- level: N5

[交差点]
- matched_form: 交差点
- reading: こうさてん
- meaning: intersection
- level: N5

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #279 (ID: 288)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `横断歩道に渡ってから、左側に大きなビルが見えます。` |
| **서버 AI 최종 교정본** | **横断歩道に渡ってから、左側に大きなビルが見えます。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[横]
- matched_form: 横
- reading: よこ
- meaning: beside; side; width
- level: N5

[道]
- matched_form: 道
- reading: みち
- meaning: road, street; way, directions
- level: N5

[左]
- matched_form: 左
- reading: ひだり
- meaning: left hand side
- level: N5

[大きな]
- matched_form: 大きな
- reading: おおきな
- meaning: big
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #280 (ID: 289)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `しんじゅくえきの東口を出て、五分ほど歩いたとこ。` |
| **서버 AI 최종 교정본** | **しんじゅくえきの東口を出て、五分ほど歩いたところ。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 의미상 자연스럽지만, 'とこ'는 문법적으로 부정확하며 'ところ'로 교정해야 합니다. 'ところ'는 '그곳'을 의미하며, 장소를 나타내는 표현으로 더 자연스럽습니다.
- **일본어 해설:** 文の意味は自然ですが、「とこ」は文法的に不正確です。「ところ」は「その場所」を意味し、場所を表す表現としてより自然です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[東]
- matched_form: 東
- reading: ひがし
- meaning: east
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5

[五]
- matched_form: 五
- reading: ご
- meaning: five
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #281 (ID: 290)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `そのビルの地下にあるきさてんは、とても雰囲気が良い。` |
| **서버 AI 최종 교정본** | **そのビルの地下にあるきさてんは、とても雰囲気が良い。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[その]
- matched_form: その
- reading: その
- meaning: that
- level: N5

[下]
- matched_form: 下
- reading: した
- meaning: under, below, beneath
- level: N5

[とても]
- matched_form: とても
- reading: とても
- meaning: very (much), greatly, exceedingly
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #282 (ID: 291)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `信号を渡らないで、手前の角を左に曲がって。` |
| **서버 AI 최종 교정본** | **信号を渡らないで、手前の角を左に曲がって。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[前]
- matched_form: 前
- reading: まえ
- meaning: before, in front
- level: N5

[角]
- matched_form: 角
- reading: かど
- meaning: corner (e.g., desk, pavement)
- level: N5

[左]
- matched_form: 左
- reading: ひだり
- meaning: left hand side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #283 (ID: 292)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ホテルの向かい側に、にじゅうよんじ営業のコンビニがある。` |
| **서버 AI 최종 교정본** | **ホテルの向かい側に、にじゅうよんじ営業のコンビニがある。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[ホテル]
- matched_form: ホテル
- reading: ホテル
- meaning: hotel
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #284 (ID: 293)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `この道をずーーっと進むと、突き当たりに公園が見える。` |
| **서버 AI 최종 교정본** | **この道をずーーっと進むと、突き当たりに公園が見える。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[この]
- matched_form: この
- reading: この
- meaning: this
- level: N5

[道]
- matched_form: 道
- reading: みち
- meaning: road, street; way, directions
- level: N5

[公園]
- matched_form: 公園
- reading: こうえん
- meaning: a park
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #285 (ID: 294)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `階段上がって二階に行くと、右側が受付です。` |
| **서버 AI 최종 교정본** | **階段上がって二階に行くと、右側が受付です。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제 없음.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[階段]
- matched_form: 階段
- reading: かいだん
- meaning: stairs
- level: N5

[上]
- matched_form: 上
- reading: うえ
- meaning: above (up, top, etc.), over, on top of
- level: N5

[二]
- matched_form: 二
- reading: に
- meaning: two
- level: N5

[行く]
- matched_form: 行く
- reading: いく; ゆく
- meaning: to go
- level: N5

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #286 (ID: 295)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `北口の改札を出てすぐのところに、マップがあります。` |
| **서버 AI 최종 교정본** | **北口の改札を出てすぐのところに、マップがあります。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 오류가 없습니다.
- **일본어 해설:** 文は自然で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[北]
- matched_form: 北
- reading: きた
- meaning: north
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #287 (ID: 296)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `駐車場の入り口は、建物の裏側にありますので。` |
| **서버 AI 최종 교정본** | **駐車場の入り口は、建物の裏側にありますので。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[車]
- matched_form: 車
- reading: くるま
- meaning: car, vehicle
- level: N5

[口]
- matched_form: 口
- reading: くち
- meaning: job opening; mouth
- level: N5

[建物]
- matched_form: 建物
- reading: たてもの
- meaning: building
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_005] です/ます 정중체
- rule_type: style_reference
- level: N5
- pattern: です/ます
- description_ko: 정중하게 말할 때는 문장 끝에 です 또는 ます 형태를 사용하는 경우가 많다.
- reference_examples: 私は学生です, 学校に行きます
- possible_focus: 정중체, 문체 일관성
- possible_error_types: unnatural_expression
- overcorrection_note: 반말이나 단편 회화 표현을 무조건 です/ます형으로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #288 (ID: 297)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `としょかんに行って勉強したけど、集中できなかった。` |
| **서버 AI 최종 교정본** | **としょかんに行って勉強したけど、集中できなかった。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고 문법적으로 올바릅니다. 의미도 명확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で文法的に正しいです。意味も明確で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[勉強]
- matched_form: 勉強
- reading: べんきょう (する)
- meaning: study
- level: N5

[中]
- matched_form: 中
- reading: なか
- meaning: inside, middle, among
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 4 (keyword_match_count=2, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #289 (ID: 298)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `友達と一緒に美味しいおすしを食べに行った。` |
| **서버 AI 최종 교정본** | **友達と一緒に美味しいおすしを食べに行った。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語で、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[友達]
- matched_form: 友達
- reading: ともだち
- meaning: friend
- level: N5

[一緒]
- matched_form: 一緒
- reading: いっしょ
- meaning: together
- level: N5

[美味しい]
- matched_form: 美味しい
- reading: おいしい
- meaning: delicious, tasty
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #290 (ID: 299)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `週末に家族とえいがかんに行って映画を見た。` |
| **서버 AI 최종 교정본** | **週末に家族とえいがかんに行って映画を見た。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 문법과 의미 모두 문제 없습니다.
- **일본어 해설:** この文は自然な日本語で、文法や意味において問題ありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[家族]
- matched_form: 家族
- reading: かぞく
- meaning: family, members of a family
- level: N5

[映画]
- matched_form: 映画
- reading: えいが
- meaning: movie, film
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_001] 場所 + に/へ + 行く
- rule_type: reference
- level: N5
- pattern: 場所 + に/へ + 行く
- description_ko: 장소로 이동한다는 의미를 말할 때 장소 뒤에 조사 に 또는 へ를 붙이고 行く를 사용하는 경우가 많다.
- reference_examples: 学校に行きました, 会社へ行きます
- possible_focus: 장소 이동 표현, 조사 に/へ 사용 여부
- possible_error_types: particle_omission
- overcorrection_note: 장소 조사 생략이 항상 불가능한 것은 아니므로, 문맥상 자연스러운 생략인지 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #291 (ID: 300)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `先生に質問したら、親切に教えてくれた。` |
| **서버 AI 최종 교정본** | **先生に質問したら、親切に教えてくれた。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[先生]
- matched_form: 先生
- reading: せんせい
- meaning: teacher, professor; master; doctor
- level: N5

[質問]
- matched_form: 質問
- reading: しつもん
- meaning: question, inquiry
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #292 (ID: 301)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `びょういんの予約が十時だから、急いで行かないと。` |
| **서버 AI 최종 교정본** | **びょういんの予約が十時だから、急いで行かないと。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[十]
- matched_form: 十
- reading: (〜を) とお
- meaning: ten (~)
- level: N5

[ない]
- matched_form: ない
- reading: ない
- meaning: there isn't, doesn't have
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_007] ません 부정형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ません
- description_ko: 정중한 부정 표현은 동사의 ません 형태를 사용하는 경우가 많다.
- reference_examples: 食べません, 行きません
- possible_focus: 부정 표현, 동사 활용
- possible_error_types: verb_conjugation_error
- overcorrection_note: 반말 부정형과 정중체 부정형을 혼동하지 않도록 문체를 함께 확인해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #293 (ID: 302)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `飛行機のチケットをいんたーねっとで予約した。` |
| **서버 AI 최종 교정본** | **飛行機のチケットをいんたーねっとで予約した。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[飛行機]
- matched_form: 飛行機
- reading: ひこうき
- meaning: airplane
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #294 (ID: 303)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `昨日はたくさん歩いたから、足が疲れた。` |
| **서버 AI 최종 교정본** | **昨日はたくさん歩いたから、足が疲れた。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로도 올바릅니다. 의미도 명확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で、文法的に正しいです。意味も明確で、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[昨日]
- matched_form: 昨日
- reading: きのう
- meaning: yesterday
- level: N5

[足]
- matched_form: 足
- reading: あし
- meaning: foot; leg
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_006] ました 과거형
- rule_type: reference
- level: N5
- pattern: 동사ます형 어간 + ました
- description_ko: 과거에 한 일을 정중하게 말할 때 동사의 ました 형태를 사용하는 경우가 많다.
- reference_examples: 昨日学校に行きました, 昨日ご飯を食べました
- possible_focus: 과거 표현, 시제 일치
- possible_error_types: tense_error
- overcorrection_note: 과거 시간 표현이 명확할 때만 시제 오류 가능성을 검토한다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)

[tense_error] 시제 오류
- description_ko: 昨日, 先週 등 과거 시간 표현과 동사 시제가 맞지 않을 가능성이 있는 경우이다.
- related_focus: 시제, 과거 표현, ました
- reference_examples:
  - observed: 昨日学校に行きます
    reference: 昨日学校に行きました
  - observed: 昨日ご飯を食べます
    reference: 昨日ご飯を食べました
- overcorrection_note: 시간 표현이 실제로 과거를 의미하는지 확인해야 하며, 예문이나 인용문에서는 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #295 (ID: 304)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `毎日日本語の単語を五個ずつずつ覚えるようにしてる。` |
| **서버 AI 최종 교정본** | **毎日日本語の単語を五個ずつ覚えるようにしてる。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 단어를 '五個ずつ'로 반복해서 기억하는 것이 아니라, '五個ずつ'가 두 번 반복되어 있습니다. 'ずつ'는 이미 '五個'에 포함되어 있으므로 중복되어 있습니다. '五個ずつ'는 자연스럽지 않으며, '五個ずつ'를 한 번만 쓰는 것이 더 자연스럽습니다.
- **일본어 해설:** 「五個ずつ」が2回繰り返されています。すでに「五個」に「ずつ」が含まれているため、重複しています。自然な表現としては「五個ずつ」を1回だけ使うのが適切です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[毎日]
- matched_form: 毎日
- reading: まいにち
- meaning: every day
- level: N5

[本]
- matched_form: 本
- reading: ほん
- meaning: book
- level: N5

[五]
- matched_form: 五
- reading: ご
- meaning: five
- level: N5

[覚える]
- matched_form: 覚える
- reading: おぼえる
- meaning: to learn, to commit to memory, to remember, to memorize
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_004] Noun + が + 好き
- rule_type: soft_reference
- level: N5
- pattern: 名詞 + が + 好きです
- description_ko: 좋아하는 대상을 말할 때 대상 뒤에 が를 붙이고 好きです를 사용하는 경우가 기본적이다.
- reference_examples: 日本語が好きです, 映画が好きです
- possible_focus: 선호 표현, 조사 が 사용 여부
- possible_error_types: particle_omission, unnatural_expression
- overcorrection_note: 회화에서는 が가 생략되어도 자연스럽게 들릴 수 있으므로, 무조건 오류로 판단하지 않는다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)

[particle_omission] 조사 누락
- description_ko: 명사 뒤에 필요한 조사 は, が, を, に, へ 등이 생략되어 문장 구조가 불분명해질 수 있는 경우이다.
- related_focus: 조사, 문장 구조, 명사와 동사의 관계
- reference_examples:
  - observed: 学校行きます
    reference: 学校に行きます
  - observed: 水飲みます
    reference: 水を飲みます
- overcorrection_note: 회화체에서는 조사가 생략되는 경우가 있으므로, 의미가 명확하거나 단편 발화인 경우 무조건 오류로 단정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #296 (ID: 305)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `お茶を飲みながら、これからの計画について話した。` |
| **서버 AI 최종 교정본** | **お茶を飲みながら、これからの計画について話した。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 100.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스럽고, 문법적으로도 올바릅니다. 의미와 표현이 정확하며, 오류가 없습니다.
- **일본어 해설:** この文は自然で、文法的にも正しいです。意味と表現が正確であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[お茶]
- matched_form: お茶
- reading: おちゃ
- meaning: (green) tea
- level: N5

[これ]
- matched_form: これ
- reading: これ
- meaning: this one
- level: N5

[話]
- matched_form: 話
- reading: はなし
- meaning: talk (chat), story
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #297 (ID: 306)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `じてんしゃに乗って近くの公園まで行った。` |
| **서버 AI 최종 교정본** | **じてんしゃに乗って近くの公園まで行った。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[近く]
- matched_form: 近く
- reading: ちかく
- meaning: nearby; in the neighborhood
- level: N5

[公園]
- matched_form: 公園
- reading: こうえん
- meaning: a park
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #298 (ID: 307)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `東京特許許可局のこうちょうが、新しいプロジェクトを発表した。` |
| **서버 AI 최종 교정본** | **東京特許許可局のこうちょうが、新しいプロジェクトを発表した。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 오류가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、誤りはありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[東]
- matched_form: 東
- reading: ひがし
- meaning: east
- level: N5

[うち]
- matched_form: うち
- reading: うち
- meaning: home; house; my place
- level: N5

[新しい]
- matched_form: 新しい
- reading: あたらしい
- meaning: new
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 3 (keyword_match_count=2, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #299 (ID: 308)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `新人歌手の新春しゃんそんそーが、まもなく始まる。` |
| **서버 AI 최종 교정본** | **新しく歌手になった新春しゃんそんそーが、まもなく始まる。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 85.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '新人歌手の'이 '新しく歌手になった'으로 자연스럽게 바꾸는 것이 더 적절하지만, 주어가 '新人歌手'로 시작되는 경우 'の'가 필요하지 않으며, 'の'가 오류로 판단됩니다. 'の'를 제거하고 '新しく歌手になった'으로 바꾸면 문맥이 자연스럽습니다. 그러나 입력 문장에서 'の'가 오류로 판단되는 경우, 조사 오용이 발생합니다.
- **일본어 해설:** 文の「新人歌手の」は「の」が不適切であり、「新しく歌手になった」に修正すると自然な表現になります。この場合、「の」の誤用が生じているため、particle_misuseと判断します。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[人]
- matched_form: 人
- reading: ひと
- meaning: man, person
- level: N5

[歌]
- matched_form: 歌
- reading: うた
- meaning: a song
- level: N5

[手]
- matched_form: 手
- reading: て
- meaning: hand
- level: N5

[春]
- matched_form: 春
- reading: はる
- meaning: spring
- level: N5

[始まる]
- matched_form: 始まる
- reading: はじまる
- meaning: (something) begins
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #300 (ID: 309)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `隣の客はよく柿食う客だってさ。` |
| **서버 AI 최종 교정본** | **隣の客はよく柿を食う客だってさ。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문맥상 사용된 조사가 적절하지 않아 더 자연스러운 조사로 수정했습니다.
- **일본어 해설:** 文脈上、使われている助詞が適切ではなかったため、より自然な助詞に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[隣]
- matched_form: 隣
- reading: となり
- meaning: next to, next door to
- level: N5

[よく]
- matched_form: よく
- reading: よく
- meaning: frequently, often (much); well, skillfully
- level: N5
```

--- 

## 📌 발화 샘플 데이터 #301 (ID: 310)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `坊主が屏風にうまく坊主の絵を描いた。` |
| **서버 AI 최종 교정본** | **坊主が屏風にうまく坊主の絵を描いた。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 85.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '屏風に'는 '屏風'에 대해 '에'를 사용하는 것이 자연스럽지만, '坊主の絵'를 '描いた'라는 표현은 문맥상 어색합니다. '屏風'에 '坊主の絵'를 '描く' 것이 아니라, '坊主'가 '屏風'에 '絵'를 '描いた' 것이 더 자연스러운 표현입니다. 따라서 '坊主の絵'를 '屏風'에 '描いた'로 바꾸는 것이 적절합니다.
- **일본어 해설:** 文の「屏風にうまく坊主の絵を描いた」は、文脈上不自然です。「坊主が屏風に絵を描いた」という表現が自然です。したがって、「坊主の絵」を「屏風に」に移動させた方が自然です。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[風]
- matched_form: 風
- reading: かぜ
- meaning: wind, breeze
- level: N5

[絵]
- matched_form: 絵
- reading: え
- meaning: a painting; a picture; a drawing
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 4 (keyword_match_count=3, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #302 (ID: 311)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `黄パプリカ赤パプリカ青パプリカをたくさん買った。` |
| **서버 AI 최종 교정본** | **黄パプリカ赤パプリカ青パプリカをたくさん買った。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[赤]
- matched_form: 赤
- reading: あか
- meaning: red
- level: N5

[青]
- matched_form: 青
- reading: あお
- meaning: blue
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #303 (ID: 312)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ばすがすばくはつって三回言うの難しい。` |
| **서버 AI 최종 교정본** | **バスがすばくはつって三回言うのは難しい。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '言うの'가 '言うのは'로 수정되어야 하며, 'は' 조사가 빠져 있었습니다. 의미는 유지하면서 문법적으로 자연스러운 표현으로 조정했습니다.
- **일본어 해설:** 文の「言うの」は「言うのは」に修正し、文法的に自然な表現にしました。意味は変更せず、文法的な誤りを修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[三]
- matched_form: 三
- reading: さん
- meaning: three
- level: N5

[言う]
- matched_form: 言う
- reading: いう
- meaning: to say
- level: N5

[難しい]
- matched_form: 難しい
- reading: むずかしい
- meaning: difficult
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #304 (ID: 313)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `右目、みじみみ、右目と順番に触って。` |
| **서버 AI 최종 교정본** | **右目、みじみみ、右目と順番に触って。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 85.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 'みじみみ'는 자연스러운 표현이 아니며, '目'이 두 번 반복된 것으로 보입니다. '右目'과 '右目と順番に'는 반복되어 의미가 모호합니다. '右目'을 한 번만 사용하고, '右目と順番に'를 '右目を順番に'로 교정하는 것이 더 자연스러운 표현입니다.
- **일본어 해설:** 「みじみみ」という表現は自然ではありません。『目』が2回繰り返されています。『右目』を1回だけ使用し、『右目を順番に』とすることで意味が明確になります。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[右]
- matched_form: 右
- reading: みぎ
- meaning: right hand side
- level: N5

[目]
- matched_form: 目
- reading: め
- meaning: eye(s)
- level: N5
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #305 (ID: 314)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `こつそしょうしょうのために、毎日カルシウム飲んでる。` |
| **서버 AI 최종 교정본** | **こつそしょうしょうのために、毎日カルシウムを飲んでいます。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 92.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장에서 '飲んでる'은 자연스러운 표현이지만, 'カルシウム'을 목적어로 하기 위해 'を'가 필요합니다. 'を'가 빠져 있으면 문법적으로 부정확합니다. '飲んでる' → '飲んでいます'으로 시제를 자연스럽게 바꾸는 것이 더 적절합니다.
- **일본어 해설:** 文に「飲んでる」は自然な表現ですが、「カルシウム」を目的語として使うために「を」が必要です。「を」が欠けており、文法的に不自然です。文法的に自然な表現にするために「飲んでいます」に修正します。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[毎日]
- matched_form: 毎日
- reading: まいにち
- meaning: every day
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)
```

### ⚠️ 잠재적 오류 유형 검토 (Error Context)
```text
다음은 입력 문장과 관련 있을 수 있는 오류 유형 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 가능한 오류 유형을 판단하기 위한 참고 근거이다.
회화체 생략, 인사 표현, 단편 발화는 과교정하지 않도록 주의한다.

[particle_misuse] 조사 오용
- description_ko: 문맥상 다른 조사가 더 적절한데 잘못된 조사가 사용된 가능성이 있는 경우이다.
- related_focus: 조사 선택, 목적어, 이동 장소
- reference_examples:
  - observed: 水が飲みます
    reference: 水を飲みます
  - observed: 学校を行きます
    reference: 学校に行きます
- overcorrection_note: 조사 선택은 문맥에 따라 달라질 수 있으므로, 단순히 특정 조사가 보인다는 이유만으로 오류로 확정하지 않는다.
- retrieval_score: 2 (keyword_match_count=1, type_match_score=1)
```

--- 

## 📌 발화 샘플 데이터 #306 (ID: 315)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `ゆしゅつこうじょうの効率向上のための会議。` |
| **서버 AI 최종 교정본** | **ゆしゅつこうじょうの効率向上のための会議。** |
| **문장 적합성 여부** | ✅ 정상 문장 (오류 없음) |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 98.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 문장은 자연스러운 일본어로, 의미와 문법적으로 문제가 없습니다.
- **일본어 해설:** この文は自然な日本語であり、意味や文法的に問題はありません。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[上]
- matched_form: 上
- reading: うえ
- meaning: above (up, top, etc.), over, on top of
- level: N5
```

--- 

## 📌 발화 샘플 데이터 #307 (ID: 316)

| 구분 | 내용 |
| :--- | :--- |
| **라즈베리파이 STT 원문** | `あったかかったから上着脱いで散歩行った。` |
| **서버 AI 최종 교정본** | **あったかかったから上着を脱いで散歩に行った。** |
| **문장 적합성 여부** | ❌ 교정 필요 문장 |
| **심층 분석 수행 여부** | True |
| **AI 모델 확신도** | 95.0% |

### 💬 AI 정밀 피드백
- **한국어 해설:** 조사를 'を'로 바꾸어 자연스러운 문장을 만들었습니다. '上着脱いで'는 '上着を脱いで'로 바꾸어야 합니다.
- **일본어 해설:** 「上着脱いで」は「上着を脱いで」として、自然な表現に修正しました。

### 📖 어휘 및 읽기 참고 자료 (Vocab Context)
```text
다음은 입력 문장에서 검색된 단어 참고 자료이다.
이 자료는 단어 의미와 읽기 확인용이며, 오류 확정이나 교정 지시가 아니다.

[上着]
- matched_form: 上着
- reading: うわぎ
- meaning: coat, jacket
- level: N5

[散歩]
- matched_form: 散歩
- reading: さんぽ (する)
- meaning: walk, stroll
- level: N5
```

### 📐 문법 규칙 매칭 근거 (Grammar Context)
```text
다음은 입력 문장과 관련 있을 수 있는 문법 참고 자료이다.
이 자료는 오류 확정이나 교정 지시가 아니라, 판단을 위한 참고 근거이다.
soft_reference 또는 style_reference 규칙은 과교정하지 않도록 주의한다.

[grammar_011] 場所 + で + 動作する
- rule_type: reference
- level: N5
- pattern: 場所 + で + 動作する
- description_ko: 어떤 장소에서 동작이나 활동을 한다고 말할 때 장소 뒤에 조사 で를 붙이는 경우가 많다.
- reference_examples: 図書館で勉強しました, レストランで昼ご飯を食べました, 学校で日本語を勉強します
- possible_focus: 장소에서 하는 동작, 조사 で 사용 여부, 장소와 동작의 관계
- possible_error_types: particle_omission, particle_misuse
- overcorrection_note: 장소 뒤에 で가 없다고 해서 항상 오류는 아니다. 문맥상 장소에서 이루어진 동작인지 확인한 뒤 참고해야 한다.
- retrieval_score: 3 (keyword_match_count=1, type_match_score=2)

[grammar_010] 何/どこ/いつ + ですか 질문 표현
- rule_type: style_reference
- level: N5
- pattern: 의문사 + ですか
- description_ko: 정중한 질문문에서는 의문사와 함께 문장 끝에 ですか 또는 ますか를 사용하는 경우가 많다.
- reference_examples: これは何ですか, 学校はどこですか
- possible_focus: 질문 표현, 정중체 질문문
- possible_error_types: unnatural_expression
- overcorrection_note: 짧은 회화 질문이나 단편 질문을 무조건 ですか 형태로 바꾸면 과교정이 될 수 있다.
- retrieval_score: 1 (keyword_match_count=1, type_match_score=0)
```

--- 

