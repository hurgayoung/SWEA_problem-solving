# 중복 순열

path = []
N = 3
visited = [False] * 7  #방문 처리할 배열


def recur(cnt): #함수정의
    #종료조건
    if cnt == N:
        print(path)
        return

    #재귀호출
    for i in range(1, 7):
        if visited[i]:
            continue

        visited[i] = True
        path.append(i)
        recur(cnt+1)
        path.pop()
        visited[i] = False

recur(0) 