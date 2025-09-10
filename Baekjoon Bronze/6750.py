# 6750 Rotating letters

str = input() # 문자열 입력

arr = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']

cnt = 0

for i in str:  # 문자열 순회
    if i in arr: # 리스트 안에 있으면
        cnt += 1
    
if cnt == len(str):
    print('YES')
else:
    print('NO')