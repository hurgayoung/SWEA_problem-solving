# 당근

'''
연속으로 커지는 당근의 개수가 최대 얼마인지
구간의 최소 길이는 1
수확한 당근의 크기들을 순회하면서 연속으로 커지는 것만 카운트
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 수확한 당근의 개수
    C = list(map(int, input().split())) # 수확한 당근의 크기

    cnt = 1 # 최소 길이 1
    max_cnt = 1

    for i in range(N-1):
        if C[i] < C[i+1]:
            cnt += 1
    
        else:
            if cnt > max_cnt:
                max_cnt = cnt # 업데이트
            cnt = 1
    
    if cnt > max_cnt:
        max_cnt = cnt

    
    print(f"#{tc} {max_cnt}")