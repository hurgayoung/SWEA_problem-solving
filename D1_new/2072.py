# 홀수만 더하기

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    
    odd_sum = 0

    for i in arr:
        if i%2!=0:
            odd_sum += i

    print(f"#{tc} {odd_sum}")