# 새로운 불면증 치료법

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 0~9까지 중복을 피하기 위한 set 사용하기
    nums_set = set()

    # 어디까지 반복해야 할지 모르기 때문에 while문 사용하기
    i = 1

    while len(nums_set) < 10: # 탈출 조건(길이 10)을 충족하기 전까지 반복하기
        for j in str(N*i): # N의 배수를 문자열로 받기
            nums_set.add(j) # 문자열 순회로 빈 집합에 원소(0~9) 더하기
        
        if len(nums_set) == 10: # 탈출 조건 만족 시 그만두기
            break
        i += 1


    print(f"#{tc} {i*N}")