# levenshtein-chatbot

이 프로젝트는 **레벤슈타인 거리(Levenshtein distance)** 를 활용하여 입력 문장과 가장 유사한 질문을 찾아, 그에 대응하는 답변을 제공하는 간단한 챗봇입니다. 기존의 TF-IDF + 코사인 유사도 기반 챗봇과 달리, 문자열 편집 거리를 이용해 유사도를 계산합니다.

---

## 📁 Files

- `ChatbotData.csv`: 질문(Q)과 답변(A)으로 구성된 학습용 데이터셋
- `levenshtein_chatbot.py`: 챗봇 본체 코드
- `README.md`: 프로젝트 개요 및 실행 방법 설명

---

## ▶️ How to Run

```bash
pip install python-Levenshtein pandas
python levenshtein_chatbot.py
