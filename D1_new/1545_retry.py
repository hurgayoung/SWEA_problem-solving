#거꾸로 출력해보아요

# n = int(input())

# for i in range(n, -1, -1):
#     print(i, end = ' ')


'''

거꾸로 출력하려면 역방향으로 반복
range(n, -1, "-1")  =>  n부터 0까지 -1씩 감소하면서 i 생성

'''

# while문으로 풀기

# n = int(input())

# while n > -1:
#     print(n, end = ' ')
#     n -= 1


arr = [1,3,7,9]

arr2 = []
for i in range(len(arr)-1, -1, -1): # 3 2 1 0
    arr2.append(arr[i])

print(arr2)


'''
반복 가능한 자료열 순회
출력 방법 복습하기 필수
'''