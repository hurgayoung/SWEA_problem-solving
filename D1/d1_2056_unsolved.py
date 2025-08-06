# 연월일 달력

T = int(input())

for t in range(1, T + 1):

    Y, M, D = list(map(int, input().split()))

    Y = list[0:4]
    M = list[4:6]
    D = list[6:]

print(f"{t} {Y} / {M} / {D}")
