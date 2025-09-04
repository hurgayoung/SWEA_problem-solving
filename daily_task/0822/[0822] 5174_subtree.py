# subtree

'''
이진 트리의 특성을 이용한 풀이
노드 N을 루트로 하는 서브 트리에 속한 노드의 개수 알아내기
'''

def f(root):
    global node_cnt

    # 카운트를 하나 늘리기
    node_cnt += 1

    # 왼쪽 자식이 있다면 왼쪽 자식을 루트 노드로 해서 탐색
    if lft_child[root] != 0:
        f(lft_child[root])
    # 오른쪽 자식이 있다면 오른쪽 자식을 루트 노드로 해서 탐색
    if rgt_child[root] != 0:
        f(rgt_child[root])


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())

    # E: 간선의 개수 -> 노드의 개수는 E+1개
    # N: 탐색을 시작할 노드의 번호

    lft_child = [0] * (E+2)
    rgt_child = [0] * (E+2)

    arr = list(map(int, input().split()))

    for i in range(E):
        parent = arr[i*2]
        child = arr[i*2+1]

        if lft_child[parent] == 0:
            lft_child[parent] = child
        else:
            rgt_child[parent] = child

    # 노드 개수 세기용 변수 초기화
    node_cnt = 0

    # 재귀 탐색 시작
    f(N)

    print(f"#{tc} {node_cnt}")