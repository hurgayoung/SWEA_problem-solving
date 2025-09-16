'''
1부터 6까지 사용하는 중복순열을 출력하는 코드를 재귀호출로 구현
'''

path = []

def recur(cnt):

    #종료 조건
    if cnt == 3:
        print(path)
        return
    

    # 재귀 호출
    for i in range(1, 7):
        path.append(i)
        recur(cnt+1)
        path.pop()

recur(0)