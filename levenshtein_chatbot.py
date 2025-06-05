import pandas as pd
import Levenshtein  # pip install python-Levenshtein

class LevenshteinChatBot:
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)

    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()
        answers = data['A'].tolist()
        return questions, answers

    def find_best_answer(self, input_sentence):
        distances = [Levenshtein.distance(input_sentence, q) for q in self.questions]
        best_match_index = distances.index(min(distances))
        return self.answers[best_match_index]

# CSV 파일 경로 지정
filepath = 'ChatbotData.csv'

# 챗봇 인스턴스 생성
chatbot = LevenshteinChatBot(filepath)

# 대화 루프
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_best_answer(input_sentence)
    print('Chatbot:', response)
