# 오르막길 오르기]
'''
오르막길은 이전 위치보다 "크거나 같은" 경우 이어진다고 판단
경사도 = (최고높이 A - 최저높이 B) / 경로길이 C
 

순증가 세다가 초기화

경사도가 같은 경우, 오르막 길이가 긴 경로의 길이 출력
오르막이 없는 경우, 0을 출력
최소 오르막 길이는 2

경사도의 최솟값 구하기!

'''


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