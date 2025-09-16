# makeset



def find(a): 
    global parents
    if parents[a] == a:
        return a

    parents[a] = find(parents[a])
    return find(parents[a])


def union(a, b):
    aRoot = find(a)
    bRoot = find(b)

    if aRoot != bRoot:
        parents[bRoot] = aRoot

    

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))