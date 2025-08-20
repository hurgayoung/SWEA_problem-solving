# 회전

from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 입력받은 N개의 자연수로 큐 생성
    q = deque() # 큐 생성 
    q.extend(arr) # arr의 수를 모두 큐에 삽입
    
    for _ in range(N):
        num = q.popleft()   # dequeue: popleft
        q.append(num)       # enqueue: append

    print(f"{tc} {q.popleft}")