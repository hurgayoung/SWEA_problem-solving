'''
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
'''

#  1 <= T <= 50
#  5 <= N <= 1000
#  print('#T', 답)

# 첫 줄에 테스트 케이스 수 -> 3
# 각 케이스의 첫 줄에 양수의 개수 N -> 5, 5, 10

T = int(input())

for i in range(1, T+1):
    N = int(input())
    ai= list(map(int, input().split()))

    max_num = ai[0]
    for a in ai:
        if max_num < a:
            max_num = a

    min_num = ai[0]
    for b in ai:
        if min_num > b:
            min_num = b
    
    c = max_num - min_num

    


   # print('N:', N ,'리스트',ai)

    print(f'#{i} {c}')



# T = int(input())

# for Test_case in range(1,T+1):
#     N = int(input())
#     ai = list(map(int,input().split()))
#     max_ai = 0
#     min_ai = ai[0]
#     total = 0
#     for i in range(N) :
#         if ai[i] > max_ai :
#             max_ai = ai[i]
#         if ai[i] <= min_ai :
#             min_ai = ai[i]
#     total = max_ai - min_ai
#     print(f'#{Test_case} {total}')