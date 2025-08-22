# 1285 아름이의 돌 던지기

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    new_arr = []

    for i in range(N):
        if arr[i] >= 0:
            new_arr.append(arr[i])
        else:
            new_arr.append(0-arr[i])
    
    min_val = min(new_arr)

    cnt = 0
    for j in new_arr:
        if j == min_val:
            cnt += 1

    print(f"#{tc} {min_val} {cnt}")

