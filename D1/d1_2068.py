# 최대수 구하기

T = int(input())

for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    max_num = max(nums)

    print(f"#{t} {max_num}")

