# 입력받은 정수를 1차원 배열에 저장

N = int(input())
arr = list(map(int, input().split()))


# 배열 원소의 합 s 계산하기

s = 0
for i in range(N):
    s += arr[i]


# 배열 원소 중 최댓값 찾기 max_v

max_v = arr[0]
for i in range(1, N):
    if max_v < arr[i]:
        max_v = arr[i]


# 배열 원소 중 최댓값의 인덱스 찾기 max_idx

max_idx =0
for i in range(1, N):
    if arr[max_idx] <= arr[i]:
        max_idx = i


#찾는 값이 배열에 있으면 해당 원소의 인덱스, 없으면 -1을 넣기

N, V = map(int, input().split())
arr = list(map(int, input().split()))


# 배열 원소의 최댓값의 마지막 인덱스를 찾는 코드

idx = -1
for i in range(1, N):
    if arr[i] == V:
        idx = i
        break