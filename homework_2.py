# 중복 순열과 순열 구현하기
'''
N개의 주사위를 던져 나올 수 있는 모든 중복 순열과 순열 출력
N은 2이고, Type는 1이므로 중복 순열을 출력합니다
'''


path = []
N = int(input())

def recur(cnt):
    if cnt == N:
        print(*path)
        return
    
    for i in range(1, 7):
        path.append(i)
        recur(cnt+1)
        path.pop()


recur(0)