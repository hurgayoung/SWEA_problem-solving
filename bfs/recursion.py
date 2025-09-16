# 중복 순열
# [0, 1, 2] 3개의 카드가 존재 -> 2개를 뽑는다.

path = []   # used, visited... --> 뽑은 카드들을 저장

# 기저조건(종료조건) : 2개의 카드를 모두 뽑았다면 종료
#  - 시작점 : 0개의 카드를 고른 상태부터 시작
# 다음 재귀호출 구조 : [0, 1, 2] 카드 중 하나를 고른다.


def recur(cnt):
    if cnt == 3:
        print(*path)
        return

    for num in range(1, 7):
        path.append(num)
        recur(cnt + 1)
        path.pop()

    # 카드 0, 1, 2 중 하나를 선택
    path.append(0)
    recur(cnt + 1)  # 하나 선택했으니 다음 선택으로 이동
    path.pop()
    
    path.append(1)
    recur(cnt + 1)
    path.pop()
    
    path.append(2)
    recur(cnt + 1)
    path.pop()

recur(0)




# 단순하게 작성하면 약 1,000번 정도 깊이에서 제한이 걸린다
    # maximum recursion depth exceeded
# 대부분 종료 조건과 함께 활용됨
#  - 자연스럽게 다음 재귀호출을 하지 않도록 구성

# 파라미터 n : 누적값
def KFC(n):
    if n == 3:  # 종료조건(기저조건 - base case) : 3
        return
    
    print(n, end=' ')
    KFC(n + 1)
    KFC(n + 1)
    print(n, end=' ')


KFC(0)  # 시작점 : 0