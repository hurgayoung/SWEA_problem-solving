# 그래프의 표현 방법

"""
1      4
| \    |
|   \  | 
2 ---- 3

"""



# 인접행렬
# 연결되어 있으면 1, 아니면 0
N = 4
adj = [[0]*(N+1) for _ in range(N+1)]
print(adj)

adj[1][2] = adj[2][1] = 1
adj[2][3] = adj[3][2] = 1
adj[1][3] = adj[3][1] = 1
adj[3][4] = adj[4][3] = 1

print(adj)


# BFS 탐색
# 그래프 탐색: 모든 정점을 한번씩 방문하는 것
# 그래프에서는 사이클이 발생할 수 있으므로, 방문처리가 꼭 필요
# 시작점: 1


visited = [False] * (N+1)
q = [] # 큐: FIFO 자료구조

# 시작점을 방문 처리 후 큐에 집어 넣는다.
visited[1] = True
q.append(1)

while q: # 큐에 원소가 있다면
    v = q.pop(0) # 가장 앞의 원소를 꺼낸다.

    print(f"현재 탐색중인 정점: {v}")

    # 현재 탐색 정점 : v
    # v의 인접 노드 중에서 아직 방문하지 않은 노드가 있다면 방문처리 후 큐에 넣는다.
    for i in range(1, N+1):
        if adj[v][i] == 1: # v와 i가 연결되어 있다(i는 v의 인접 정점)
            if not visited[i]:
                visited[i] = True # 방문처리
                q.append(i)