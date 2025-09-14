# 단조

'''
단조 -> 각 숫자의 자릿수가 단순하게 증가하는 수
Ai Aj를 곱해주기 위해 순회를 2번 -> Ai Aj 곱한 값
곱한 값 문자열로 변환
단조인지 확인
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = -1

    for i in range(N-1):
        for j in range(i+1, N):

            num = arr[i] * arr[j]
            new_num = str(num)
            
            is_danzo = True
            for k in range(len(new_num)-1):
                if new_num[k] > new_num[k+1]:
                    is_danzo = False

            if is_danzo and max_num < num:
                max_num = num
    
    print(f"#{tc} {max_num}")