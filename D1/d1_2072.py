# 홀수만 더하기

T = int(input())

for t in range(1, T + 1):
    ai = list(map(int, input().split()))
    odd_sum = 0

    for i in ai:
        if i % 2 == 1:
            odd_sum = odd_sum + i


    print(f"#{t} {odd_sum}")