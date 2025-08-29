'''
문제 📄
주어진 문자열이 회문(Palindrome)인지 판별하는 코드를 작성하세요.

회문은 앞뒤로 읽었을 때 동일한 단어나 구문을 의미합니다. 이 문제에서는 알파벳만을 대상으로 하고, 대소문자 및 공백을 구분하지 않습니다. 숫자는 입력값에 포함되지 않는다고 가정합니다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어집니다.
각 테스트 케이스는 하나의 문자열 text로 구성됩니다.

출력
각 테스트 케이스에 대해 is_palindrome 함수의 결과(True 또는 False)를 출력하세요.

- input -
3
level
samsungssafy
Racecar
A man a plan a canal Panama
Hello Worlds

- output -

True
False
True
True
False

'''


def is_palindrome(txt):
    for i in range(n//2): # 문자열 반만 반복
        if txt[i] != txt[n -1-i]: # 앞에서부터 i번째, 뒤에서부터 i번째 글자 검사
            return False # 다르다면 False 출력

    return True # 같다면 True 출력

for tc in range(5):
    txt = input()
    n = len(txt) # 문자열 길이
    print(is_palindrome(txt))
    

# for tc in range(3):
#     txt = input() # Racecar
#     txt1 = txt.lower()  # racecar
#     if txt1 == txt1[::-1]:  # racecar == racecar
#         palindrome = True   # !
#     else:
#         palindrome = False
#     print(palindrome)