# 증가하는 사탕 수열

'''
모든 상자에 1개 이상의 사탕이 있어야 함 -> 사탕을 먹어 없애서 0이 되는 경우 피하기 -> 1이 되면 멈추기

조건 만족 못하는 경우 고려 ("-1" 출력해야 하는 경우)

조건 실행 가능 여부를 확인하고,
가능하다면 조건 만족까지 순회하면서 최솟값 출력하기
'''

T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())  # 사탕 개수 비교, 조건 순회를 위해 원소를 각각 입력받기


    eaten_candy = 0 # 먹은 사탕의 개수

    #1. B < C 만들기 : B에서 하나 줄이고, 카운팅 하나 늘리고
    while B >= C:
        B -= 1
        eaten_candy += 1

    #2. A < B 만들기 : A에서 하나 줄이고, 카운팅 하나 늘리고
    while A >= B:
        A -= 1
        eaten_candy += 1

    # -1 출력은 언제하지?
    if A < 1:
        print(f"#{tc} -1")        
    else:
        print(f"#{tc} {eaten_candy}")