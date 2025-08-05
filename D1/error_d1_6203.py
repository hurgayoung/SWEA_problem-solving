class Student:
    def __init__(self, korean, english, math):
        self.korean = korean
        self.english = english
        self.math = math

    def get_total_score(self):
        return self.korean + self.english + self.math


# 입력값을 한 줄에 입력받기
input_str = input("국어, 영어, 수학 점수를 입력하세요 (예: 89,90,100): ")
korean, english, math = map(int, input_str.split(','))

# Student 객체 생성
student = Student(korean, english, math)

# 총점 출력
print("총점:", student.get_total_score())