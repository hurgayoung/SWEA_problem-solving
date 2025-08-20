# 수도요금경쟁

T = int(input())

for tc in range(1, T+1):
    # 변수 한 번에 정수형으로 입력받기
    P, Q, R, S, W = map(int, input().split())


    # 회사 A
    payment_A = P * W
    
    # 회사 B
    if W <= R:
        payment_B = Q
    else:
        payment_B = Q + S * (W-R)

    # 요금이 더 저렴한 회사 고르기
    min_price = min(payment_A, payment_B)

    print (f"#{tc} {min_price}")