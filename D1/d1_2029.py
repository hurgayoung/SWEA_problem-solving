# 몫과 나머지 출력하기

T = int(input())

for t in range(1, T + 1):
    a, b = map(int, input().split())
    result_1 = a // b
    result_2 = a % b
    print(f"#{t} {result_1} {result_2}")