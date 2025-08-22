# 새로운 불면증 치료법

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    i = 0
    num_set = set()

    while len(num_set) < 10:
        i = i + 1
        for j in str(N * i):  # 10, j = 1, 0
            num_set.add(j)

        if len(num_set) == 10:
            break

    print(f"#{tc} {i}")