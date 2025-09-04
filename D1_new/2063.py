# 중간값 찾기

N = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(arr)

print(arr2[N//2])