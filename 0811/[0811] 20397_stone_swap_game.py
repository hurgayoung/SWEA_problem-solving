# 돌 뒤집기 게임

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    stones = list(input())
    i, j = map(int, input().split())

    for i in stones:
        range(1, j)