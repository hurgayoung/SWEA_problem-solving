# 우주 괴물

'''
0은 빈칸, 1은 벽, 2는 괴물
괴물의 광선은 상하좌우로 발사, 벽에 막히면 안전지대

전체 0의 개수에서 외계인의 광선이 닿은 0의 개수를 빼는 방식으로 구하기
'''


T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    zero_count = 0
    # 배열 내 0의 전체 개수 구하기
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                zero_count += 1
                

            # 광선이 닿은 0의 개수 구하기
            
            if arr[r][c] == 2:

                # 좌표가 2인 경우 상하좌우(+) 탐색
                laser_count = 0
                for d in range(4):
                    for n in range(1, N):
                        nr = r + dr[d] * n
                        nc = c + dc[d] * n
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 1:
                                break
                            
                            if arr[nr][nc] == 0:
                                laser_count += 1
            
                
    safe_zone = zero_count - laser_count


    print(f"#{tc} {safe_zone}")