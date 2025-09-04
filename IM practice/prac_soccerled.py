T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = [[0] * N for _ in range(4)]

    cnt = 0

    for i in range(4):
        for j in range(N):
            for time in range(1, K+1):
                if (i+j+1) % time == 0 and arr[i][j] == 0:
                    arr[i][j] = 1

                elif (i+j+1) % time == 0 and arr[i][j] == 1:
                    arr[i][j] = 0
            
            if arr[i][j] == 1:
                cnt += 1       

    print(f"#{tc} {cnt}")