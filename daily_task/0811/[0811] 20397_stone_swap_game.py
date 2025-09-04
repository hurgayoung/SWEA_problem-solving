# 돌 뒤집기 게임

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))   # 초기 돌들의 상태

    for _ in range(M): # 뒤집기 횟수만큼 반복
        i, j = map(int, input().split())
        i -= 1  # arr 인덱스는 0부터 시작하므로 값을 맞추기 위해 1을 빼줌

        for jj in range(1, j+1):  # 주어진 j 값의 범위만큼 반복
            if i - jj < 0 or i + jj >= N: # 주어진 범위를 벗어나는 경우 뒤집기 중지
                break

            if arr[i - jj] == arr[i + jj]: # 중심 돌 i 기준 양쪽의 돌 색이 일치한다면
                if arr[i - jj] == 1 and arr[i + jj] == 1: # 둘 다 1이면 0으로 바꿈
                    arr[i - jj] = 0
                    arr[i + jj] = 0
                else: # 둘 다 0이면 1로 바꿈
                    arr[i - jj] = 1
                    arr[i + jj] = 1
            else: # 중심 돌 i 기준 양쪽의 돌 색이 다르다면 놔두기
                pass

    print(f"#{tc}", *arr)