# 어디에 단어가 들어갈 수 있을까
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0  # 단어가 들어갈 수 있는 횟수의 총합 

    for r in range(N):
        word_length = 0  # 단어의 길이

        for c in range(N):
            # 행 우선 순회 & 탐색
            if arr[c][r] == 1:
                word_length += 1

            else:
                if word_length == K:
                    cnt += 1
                word_length = 0
            
            
        if word_length == K:
            cnt += 1       


    for c in range(N):
        word_length = 0
        for r in range(N):
            # 열 우선 순회 & 탐색
            if arr[c][r] == 1:
                word_length += 1

            else:
                if word_length == K:
                    cnt += 1
                word_length = 0
        

        if word_length == K:
            cnt += 1       


    print(f"#{tc} {cnt}")