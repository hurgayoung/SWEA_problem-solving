# 평균값 구하기

T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int, input().split()))

    sum_num = 0

    for n in numbers:
        sum_num += n
    
    avr_num = round(sum_num / 10)


    print(f"#{t} {avr_num}")