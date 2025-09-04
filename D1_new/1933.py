# 간단한 N의 약수

N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i, end=' ')



'''
i가 N의 약수라는 것은
N % i == 0
'''