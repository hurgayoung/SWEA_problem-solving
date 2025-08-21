# 공과 잡초

T = int(input())

for tc in range(1, T+1):
    str = input().strip()
    
    min_cnt = 0

    for i in str:
        if i == '(':
            min_cnt += 1
        elif i == ')':
            min_cnt += 1
        elif '()' in str:
            min_cnt -= 1



    print(f"#{tc} {min_cnt}")