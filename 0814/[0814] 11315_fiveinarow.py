# 오목 판정


'''
대각선 카운트 방식을 모르겠다.
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [input().strip() for _ in range(N)]

    count = 0

    # 가로
    for r in range(N):
        row = 0
        for c in range(N):
            if arr[r][c] == 'o':
                row += 1
            else:
                if row == 5:
                    count += 1
                row = 0
        if row == 5:
            count += 1

    # 세로
    for c in range(N):
        row = 0
        for r in range(N):
            if arr[r][c] == 'o':
                row += 1
            else:
                if row == 5:
                    count += 1
                row = 0
        if row == 5:
            count += 1

    # 대각선

  # ???

    if count >= 1:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")
