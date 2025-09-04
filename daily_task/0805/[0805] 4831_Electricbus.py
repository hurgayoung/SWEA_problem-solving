# 전기버스

'''
K: 최대 이동 거리

N: 도착 정류장 번호

M: 충전기 개수

Charge_list: 충전기 위치 리스트
'''

T = int(input())

for Test_case in range(1, T + 1):
    K, N, M = map(int, input().split())  # 최대 이동수, 도착 정류장, 충전기 개수
    Charge_list = list(map(int, input().split()))  # 충전기 위치

    Charge_list_convert = [0] * (N + 1)
    for j in range(M):
        Charge_list_convert[Charge_list[j]] = 1  # 해당 위치에 충전기 표시

    min_charge = 0 
    bus = 0
    

    # 가장 멀리 갈 수 있는 위치부터 역순으로 충전기가 있는 곳을 찾음
    while bus + K < N:
        for findcharge in range(K - 1, -1, -1):
            # 충전기를 찾은 경우 -> 그곳으로 이동하여 충전 횟수 + 1
            position = bus + findcharge + 1
            if position <= N and Charge_list_convert[position] == 1:
                min_charge += 1
                bus = position
                break
            # 충전기를 찾지 못한 경우
            else:
                min_charge = 0
                break

    print(f'#{Test_case} {min_charge}')