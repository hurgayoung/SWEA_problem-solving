
# 방향 설정: + 모양 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 방향 설정: x 모양 (대각선 ↘ ↙ ↖ ↗)
dr2 = [1, 1, -1, -1]
dc2 = [1, -1, 1, -1]

T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0  # 최대 파리 수 초기화

    # + 모양 탐색
    for r in range(N):
        for c in range(N):
            total = arr[r][c]  # 중심 포함
            for d in range(4):
                for m in range(1, M):
                    nr = r + dr[d] * m
                    nc = c + dc[d] * m
                    if 0 <= nr < N and 0 <= nc < N:
                        total += arr[nr][nc]
            if total > max_val:
                max_val = total

    # x 모양 탐색
    for r in range(N):
        for c in range(N):
            total = arr[r][c]  # 중심 포함
            for d in range(4):
                for m in range(1, M):
                    nr = r + dr2[d] * m
                    nc = c + dc2[d] * m
                    if 0 <= nr < N and 0 <= nc < N:
                        total += arr[nr][nc]
            if total > max_val:
                max_val = total

    # 테스트 케이스 번호와 함께 출력
    print(f"#{tc} {max_val}")


