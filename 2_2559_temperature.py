# 수열

'''
연속하는 며칠 동안의 온도의 합이 가장 큰지?
몇 번 순회하는지는 정해져있으니까 for 문으로 반복 -> 연속 날짜만큼 인접한 배열 원소 더하기
'''

N, K = map(int, input().split())       # N은 전체 개수, K는 연속하는 날짜의 수
arr = list(map(int, input().split()))  # arr은 매일 측정한 온도

max_tem_sum = 0

for i in range(N-K+1):
    tem_sum = 0 # 온도의 합

    for j in range(K):
        tem_sum += arr[i+j]
        if tem_sum > max_tem_sum:
            max_tem_sum = tem_sum
            

print(max_tem_sum)