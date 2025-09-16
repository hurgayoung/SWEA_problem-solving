# 그래프의 표현 방법

"""
1      4
| \    |
|   \  | 
2 ---- 3

"""

from collections import deque


# 인접행렬
# 연결되어 있으면 1, 아니면 0
N = 4

# 인접리스트
# 연결되어있는 정점 번호를 리스트로 나타내는 것
adj_list = [[] for _ in range(N+1)] # 일단 비어있는 리스트를 N+ 1개 만든다.
adj_list[1] = [2, 3]
adj_list[2] = [1, 3]
adj_list[3] = [1, 2, 4]
adj_list[4] = [3]


visited = [False] * (N+1) # 방문처리 배열 만들기
q = deque() # 큐 만들고

visited[1] = True # 시작점 방문처리후
q.append(1) # 시작점 큐에 넣기

while q: # while문 안에서
    v = q.popleft() # 가장 앞에 있는 원소 꺼내기

    print(v)

    for u in adj_list[v]: # 그 원소의 인접 노드 중에서
        if not visited[u]: # 아직 방문하지 않은게 있으면
            visited[u] = True #방문처리후
            q.append(u) # 큐에 넣느다
