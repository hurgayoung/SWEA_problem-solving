# 1285 아름이의 돌 던지기

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = map(int, input().split())

    for i in arr:

    # 절댓값으로 오름차순 정렬
        print(sorted(abs(i)))

    # 가장 첫번째 값과 던진 사람의 수(인원 수 구하기 편할 것 같음)