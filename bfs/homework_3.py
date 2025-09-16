# 주사위 눈의 합


path = []
N = 3
result = 0

def recur(cnt, total):
    # 종료조건
    global result

    if cnt == N:
        if total <= 10:
            result += 1
        return
    
    # 재귀호출
    for i in range(1, 7):
        path.append(i)
        recur(cnt+1, total+i)
        path.pop()
        
recur(0, 0)
print(result)