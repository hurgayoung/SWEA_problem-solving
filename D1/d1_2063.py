# 중간값 찾기

N = int(input())

nums = list(map(int, input().split()))

nums.sort()

median = nums[N //2]

print(median)