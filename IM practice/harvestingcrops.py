# SWEA 2805 농작물 수확하기

'''
N은 항상 홀수
수확은 정사각형 마름모 형태
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input().strip()))) for _ in range(N)]

    d = N // 2  # 중앙으로부터 떨어진 거리 (왼쪽과 오른쪽이 동일)
    total = 0

    for r in range(N):
        for c in range(d, N - d):  # d만큼 떨어진 곳부터 수확
            total += arr[r][c]
        if r < N // 2:
            d -= 1  # 위쪽 절반: 범위 점점 넓어짐
        else:
            d += 1  # 아래쪽 절반: 범위 점점 좁아짐

    print(f"#{tc} {total}")