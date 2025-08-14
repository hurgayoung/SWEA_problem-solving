# 고대 유적 2

'''
N 행, M 열의 2차원 배열
구조물이 있는 곳은 1, 빈 땅은 0으로 표시
노이즈 고려할 것 (최소 크기는 1X2m)
가장 긴 구조물의 "길이" 출력
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    max_length = 0

    for r in range(N):
        length = 0
        for c in range(M):
            if arr[c][r] == 1:
                length += 1
            
                if max_length < length:
                    max_length = length
            else:
                length = 0 
       

    for c in range(M):
        length = 0
        for r in range(N):
            if arr[c][r] == 1:
                length += 1
                if max_length < length:
                    max_length = length

            else:
                length = 0 
    
    if max_length < 2:
        max_length = 0

    print(f"#{tc} {max_length}")