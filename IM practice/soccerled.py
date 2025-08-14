# 모의고사

T = int(input())


for tc in range(1, T+1):
    n, k = map(int, input().split())

    arr = [([0] * n) for _ in range(4)]
    
    count_on = 0

    for i in range(4):
        for j in range(n):
            for time in range(1, k+1):
                if (i+j+1) % time == 0:
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    
                    else:
                        arr[i][j] = 0
                        
            if arr[i][j] == 1:
                count_on += 1

    print(f"#{tc} {count_on}")