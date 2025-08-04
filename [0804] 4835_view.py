# 총 10개의 테스트케이스

for T in range(1, 11):

    N = int(input())
    H = list(map(int, input().split()))
    result = 0

    for i in range(2, N - 2):
        next_level = H[i-2:i]+H[i+1:i+3]

        if H[i] > max(next_level):

            result += H[i] - max(next_level)
        


    print(f'#{T} {result}')





    # 들여쓰기 확인
    # 리스트 범위 지정 H[i-2:i] + H[i+1:i+3] 주의하기!
    # list(map(int, input().split()))
    # max, min 내장함수 사용법 익히기