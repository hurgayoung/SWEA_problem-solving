# 스위치 조작

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    switch_count = 0

    for i in range(N):
        if arr1[i] != arr2[i]:    # 위치값 다르면 스위치 조작
            for j in range(i, N): # i번부터 끝까지 스위치 상태가 변경
                f
            switch_count += 1

    print(f"#{tc} {switch_count}")