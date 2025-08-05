'''
0 ~ 9까지 적힌 N장의 카드
가장 "많은" 카드 -> 숫자명 & 개수 (장수가 같으면 큰 쪽 출력)
'''

# 카운팅 리스트 문제

# 테스트 케이스 출력
T = int(input())

# 카드 순회
for i in range(1, T + 1):

    N = int(input())
    ai = list(map(int, input().split()))
    
    # 가장 많은 카드의 장 수는 max_count, 숫자는 max_card
    max_count = 0
    max_card = None

    # 숫자 리스트를 순회하면서 일치하는 카드를 누적
    for card in ai:
        count = 0
        for compare_card in ai:
            if card == compare_card:
                count += 1

        if count > max_count:
            max_count = count
            max_card = card
        elif count == max_count:
            if card > max_card:
                max_card = card



    print(f"#{i} {max_card} {max_count}")






def counting_sort(DATA, TEMP, k):

    COUNTS = [0] * 10

    for i in range(len(DATA)):
        COUNTS[DATA[i]] += 1

    for i in range(1, 10):
        COUNTS[i] += COUNTS[i-1]

    for i in range (len(DATA)-1, -1, -1):
        COUNTS[DATA[i]] -= 1
        TEMP[COUNTS[DATA[i]]] = DATA[i]