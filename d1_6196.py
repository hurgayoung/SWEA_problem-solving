'''
1~9 사이의 정수 a를 입력받아 a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.
'''

# 문자열로 입력
a = input()

# 문자열을 반복
result = int(a) + int(a*2) + int(a*3) + int(a*4)
print(result)