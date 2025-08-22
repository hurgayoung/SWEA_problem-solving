# 1945 간단한 소인수분해

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    if N % 2 == 0:
        a = N // 2
    elif N % 3 == 0:
        b = N // 3
    elif N % 5 == 0:
        c = N // 5
    elif N % 7 == 0:
        d = N // 7
    elif N % 11 == 0:
        e = N // 11


    
    print(f"#{tc} {a} {b} {c} {d} {e}")