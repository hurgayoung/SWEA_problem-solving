# N개의 정수가 들어있는 배열에서 이웃한 M개의 합
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력


T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    
    first_sum = sum(ai[:M])
    max_sum = first_sum
    min_sum = first_sum

    for a in range(1, N - M + 1):
        current_sum = sum(ai[a:a+M])
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < min_sum:
            min_sum = current_sum

    print(f'#{i} {max_sum - min_sum}')




# T = int(input())

# # 테스트케이스 반복
# for tc in range(1, T + 1):
#     N, M = list(map(int, input().split()))
#     arr = list(map(int, input().split()))

#     # for num in arr : 배열의 숫자를 반복
#     # 알고리즘 문제에서는 index를 가지고 생각해야 함

#     # 최대값을 구할 때는 최소값으로 초기화하고
#     # 최소값을 구할 때는 최대값으로 초기화한다


#     max_val = -9999999999
#     min_val = 9999999999

#     for i in range(0, N-M+1):
#         s = sum(arr[])
#         if s > max_val:
#             max_val = s
#         if s < min_val:
#             min_val = s
#     print(f'#{tc}' f'({max_val} - {min_val})')