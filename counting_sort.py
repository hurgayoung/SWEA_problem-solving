# DATA
# COUNT
# TEMP

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_m = arr[0]
    for m in arr:
        if max_m < m:
            max_m = m
    
    counts = [0] * (max_m+1)
    
    TEMP = [0] * len(arr)
    
    for i in range(len(arr)):
        counts[arr[i]] += 1

    for i in range(1, max_m+1):
        counts[i] += counts[i-1]

    for i in range(N-1, -1, -1):
        counts[i] - 1

