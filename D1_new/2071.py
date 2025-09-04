# 평균값 구하기

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    sum = 0

    for i in arr:
        sum += i

    avg = sum / len(arr)

    print(f"{tc} {avg:.0f}")
