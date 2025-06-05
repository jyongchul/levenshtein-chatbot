# 필요한 라이브러리 불러오기
import pandas as pd                      # CSV 파일을 불러오기 위해 pandas 사용
import Levenshtein                      # 문자열 간의 편집 거리(레벤슈타인 거리)를 계산하기 위한 라이브러리

# 레벤슈타인 거리 기반 챗봇 클래스 정의
class LevenshteinChatBot:
    def __init__(self, filepath):
        # 생성자에서 질문과 답변 데이터를 로딩합니다.
        self.questions, self.answers = self.load_data(filepath)

    def load_data(self, filepath):
        """
        CSV 파일에서 질문(Q)과 답변(A) 데이터를 불러옵니다.
        """
        data = pd.read_csv(filepath)                # CSV 파일 읽기
        questions = data['Q'].tolist()              # 질문 열을 리스트로 추출
        answers = data['A'].tolist()                # 답변 열을 리스트로 추출
        return questions, answers

    def find_best_answer(self, input_sentence):
        """
        사용자 입력 문장과 학습 질문들 간의 레벤슈타인 거리를 계산하고,
        가장 유사한 질문의 인덱스를 찾아 해당 답변을 반환합니다.
        """
        distances = [
            Levenshtein.distance(input_sentence, q)
            for q in self.questions
        ]  # 각 질문과의 레벤슈타인 거리 계산

        best_match_index = distances.index(min(distances))  # 가장 짧은 거리(가장 유사한 질문)의 인덱스 찾기
        return self.answers[best_match_index]               # 해당 인덱스의 답변 반환

# 학습 데이터 파일 경로 지정
filepath = 'ChatbotData.csv'

# 챗봇 인스턴스 생성
chatbot = LevenshteinChatBot(filepath)

# 사용자와의 대화 루프 시작
while True:
    input_sentence = input('You: ')                  # 사용자 입력 받기
    if input_sentence.lower() == '종료':             # '종료' 입력 시 종료
        break
    response = chatbot.find_best_answer(input_sentence)  # 가장 유사한 질문의 답변 찾기
    print('Chatbot:', response)                      # 챗봇의 응답 출력
