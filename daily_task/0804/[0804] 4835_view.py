# 총 10개의 테스트케이스

for T in range(1, 11):

    # 건물의 높이를 H로 설정

    N = int(input())
    H = list(map(int, input().split()))

    # 건물을 하나씩 순회하며 기준 건물 중심으로 더 높은 건물이 있는지 확인
    # 색칠 칸을 result로 누적
    result = 0

    # 양 끝의 2칸을 제외
    for i in range(2, N - 2):

        # 기준이 되는 건물 i를 중심으로 왼쪽 2개, 오른쪽 2개씩 건물의 높이 측정
        next_level = H[i-2:i]+H[i+1:i+3]
        
        if H[i] > max(next_level):

            result += H[i] - max(next_level)
        


    print(f'#{T} {result}')





    # 들여쓰기 확인
    # 리스트 범위 지정 H[i-2:i] + H[i+1:i+3] 주의하기!
    # list(map(int, input().split()))
    # max, min 내장함수 사용법 익히기