# 더블더블

n = int(input())
i = 1

for _ in range(n+1):
    print(i, end = ' ')
    i *= 2


'''
for, while문 사용할 때는 아래에서 들여쓰기 된 블록 전체가 반복대상!

for문의 경우 i*=2 할 때마다 print하겠다는 뜻이고,
while문의 경우 i*=2 후 count+=1 할 때마다 print하겠다는 뜻
'''


# count = 0

# while count <= n:
#     print(i)
#     i *= 2
#     count += 1