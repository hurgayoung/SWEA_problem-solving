# 1945. 간단한 소인수분해


T = int(input())
primes = [2, 3, 5, 7, 11] # 나눌 소수

for tc in range(1, T + 1):
    N = int(input())
    counts = [] # 소수로 나눈 몫

    for p in primes:
        cnt = 0
        while N % p == 0: # 소수를 순회하며 N이 소수로 나누어 떨어질 때
            N //= p
            cnt += 1
        counts.append(cnt)

    print(f"#{tc}", *counts)
