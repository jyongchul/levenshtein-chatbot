# levenshtein-chatbot

이 프로젝트는 **레벤슈타인 거리(Levenshtein distance)** 를 기반으로 사용자의 질문과 가장 유사한 질문을 찾아 해당 답변을 제공하는 간단한 챗봇입니다.  
이는 기존 TF-IDF + Cosine Similarity 방식과 달리, **문자열 간 편집 거리**를 사용하여 질문 유사도를 판단합니다.

---

## 📁 Files

- `ChatbotData.csv`: 질문(Q)과 답변(A)으로 구성된 학습용 데이터셋  
  → 데이터 출처: [https://github.com/songys/Chatbot_data](https://github.com/songys/Chatbot_data)
- `levenshtein_chatbot.py`: 챗봇 본체 코드
- `README.md`: 프로젝트 개요 및 실행 방법 설명

---

## ▶️ How to Run

```bash
pip install python-Levenshtein pandas
python levenshtein_chatbot.py
