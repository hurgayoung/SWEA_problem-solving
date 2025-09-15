# 4435 중간계 전쟁

'''
종족별/군대별 점수
전투에 참여한 각 종족의 점수를 합한 뒤 비교

전투 개수가 주어져 반복하며 전투 번호+문구 출력
'''

T = int(input())

for tc in range(1, T+1):
    arr1 = (list(map(int, input().split()))) # 간달프 군대에 참여한 종족의 수
    arr2 = (list(map(int, input().split()))) # 사우론 군대에 참여한 종족의 수 
    

    gandalps = [1, 2, 3, 3, 4, 10]
    sauron = [1, 2, 2, 2, 3, 5, 10]

    sum_gandalps = 0
    sum_sauron = 0

    for i in range(len(arr1)):
        i = arr1[i] * gandalps[i]
        sum_gandalps += i
    
    for j in range(len(arr2)):
        j = arr2[j] * sauron[j]
        sum_sauron += j

    if sum_gandalps > sum_sauron:
        print(f"Battle {tc}: Good triumphs over Evil")

    elif sum_gandalps < sum_sauron:
        print(f"Battle {tc}: Evil eradicates all trace of Good")
    

    elif sum_gandalps == sum_sauron:
        print(f"Battle {tc}: No victor on this battle field")
    