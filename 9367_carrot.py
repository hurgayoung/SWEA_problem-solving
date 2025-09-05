
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))

    max_cnt = 1
    cnt = 1

    for i in range(len(C)-1):
        if C[i] < C[i+1]:
            cnt += 1
        
        else:
            if cnt > max_cnt:
                max_cnt = cnt # 직전까지 cnt 값 필요 시 갱신

            cnt = 1 # cnt 초기화

    if cnt > max_cnt:
        max_cnt = cnt
    
    print(f"#{tc} {max_cnt}")