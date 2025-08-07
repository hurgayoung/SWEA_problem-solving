'''
A = {1, 2, 3, ... , 12}
N = 부분집합 원소의 개수
K = 부분집합 원소의 합

N, K 를 만족하는 부분집합 개수 출력
해당 부분집합이 없으면 0을 출력
'''

T = int(input())

A = [i for i in range(1, 13)]  # 집합 A = {1, 2, ..., 12}
n = len(A)

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    count = 0  # 조건 만족하는 부분집합 수

    for i in range(1 << n):  # 모든 부분집합을 탐색
        subset = []
        for j in range(n):
            if i & (1 << j):  # j번째 원소가 포함된 경우
                subset.append(A[j])
        # 조건 검사
        if len(subset) == N and sum(subset) == K:
            count += 1

    print(f"#{tc} {count}")