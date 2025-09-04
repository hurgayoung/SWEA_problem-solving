# 피자 굽기

from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheeses  = list(map(int, input().split()))
    nums = list(range(1, M+1))

    # (피자번호, 치즈의양)
    # cheeses = [7 2 5 6 3]
    # nums = [1 2 3 4 5]
    # pizzas = [(1, 7), (2, 2), (3, 6), (4, 5), (5, 3)]
    pizzas = list(zip(nums, cheeses))

    q = deque() # 화덕의 큐
    # 화덕의 크기는 N이므로 일단 앞의 N개의 피자를 화덕에 집어넣는다.

    for _ in range(N):
        q.append(pizzas.pop(0))

    # 종료조건: 최후의 피자 1개가 남으면 됨 ~ 목표 상태
    # 반복: 2개 이상이라면 계속 반복 ~ 목표에 다다르지 못한 상태

    while len(q) > 1: # 화덕에 피자가 2개 이상이라면 반복한다
        # 화덕에서 피자 꺼내기(맨앞 피자는 이미 화덕을 한바퀴 돈 상태)
        # 꺼낸 피자는 치즈를 2로 나눠주면 됨
        num, cheese = q.popleft()
        cheese //= 2 # 치즈를 반으로 줄여준다

        if cheese == 0 and pizzas: # 만약에 치즈가 0이 되고, 아직 화덕에 넣지 않은 피자가 남아있다면
            q.append(pizzas.pop(0))
        elif cheese > 0:
            q.append((num, cheese))

    
    # while문이 끝났다면 len(q) > 1 == False이면 긑
    #                  len(q) <= 1이 되었다는 뜻 
    # 최후의 피자 1개가 남음

    # 최후의 피자 1개를 꺼낸다
    num, cheese = q.popleft()

    print(f"#{tc} {num}") # 최후의 피자 번호를 출력