def favorite_path(N, heights):
    best_slope = float('inf')
    best_len = 0

    start = 0  # 오르막 시작 인덱스
    for i in range(1, N+1):
        # 배열 끝이거나 오르막 끊기면 구간 확정
        if i == N or heights[i] < heights[i-1]:
            length = i - start
            if length >= 2:  # 최소 길이 조건
                low = heights[start]
                high = heights[i-1]
                slope = (high - low) / length

                # 최적 갱신
                if slope < best_slope or length > best_len:
                    best_slope = slope
                    best_len = length
            start = i  # 새 구간 시작

    return best_len


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))
    ans = favorite_path(N, heights)
    print(f"#{tc} {ans}")