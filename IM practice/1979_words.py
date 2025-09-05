# 어디에 단어가 들어갈 수 있을까


'''
흰색 칸 1, 검은색 칸 0
열순회, 행순회 하면서 cnt += 1
검은색으로 간다고 끝내지 말고 뒷부분도 고려
'''

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split()) for _ in range(N))]

    cnt = 0   # 최종 출력할 변수: 길이가 K인 자리의 수

    # 행 우선순회
    for r in range(N):
        length = 0
        for c in range(N):
            if arr[r][c] == 1:
                length += 1

            if arr[r][c] == 0:
                if length == K:
                    cnt += 1
                length = 0
    
        if length == K:
            cnt += 1 




    # 열 우선순회
    for c in range (N):
        length = 0
        for r in range(N):
            if arr[r][c] == 1:
                length += 1

                if length == K:
                    cnt += 1
                
            if arr[r][c] == 0:
                length = 0

    print(f"#{tc} {cnt}")




    # # 행 우선순회
    # for r in range(N):
    #     length = 0 # 길이가 K가 되는지 확인하는 단어의 길이
    #     for c in range(N):
    #         if arr[r][c] == 1:
    #             length += 1

    #         if arr[r][c] == 0:
    #             if length == K:
    #                 cnt += 1
    #             length = 0
        
    #     if length == K:
    #         cnt += 1
    

    # # 열 우선순회
    # for c in range(N):
    #         length = 0 # 길이가 K가 되는지 확인하는 단어의 길이
    #         for r in range(N):
    #             if arr[r][c] == 1:
    #                 length += 1
    #                 if arr[r][c] == 0:
    #                     if length == K:
    #                         cnt += 1
    #                     else:
    #                         break