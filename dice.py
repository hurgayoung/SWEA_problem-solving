# 주사위 3개를 던져서 합이 10 이하인 케이스의 수

'''
주사위 (1~6) x 3개  => 합이 10 이하인 중복순열 출력
주사위 던지는 횟수가 재귀함수의 인자여야 할 것 같아요
중복순열!

'''

# path = []

# def recur(cnt):

#     # 종료조건
#     if cnt == 3: # 주사위 세 번 굴리면 종료
        
#         for j in path: # [1, 1, 1]
#             sum += j # 3 

#         if sum <= 10:
#             print(path)
        
#         return
    

#     # 재귀호출
#     for i in range(1, 7):
#         path.append(i)
        
#         recur(cnt+1)

#         path.pop()


# recur(1)



path = []
result = 0

N = 3 # 주사위 3번 굴리기

def recur(cnt, total):
    global result

    # 종료 조건
    if cnt == N:
        if total >= 10:
            result += 1

        return

    # 재귀 호출
    for i in range(1, 7):
        path.append(i)
        recur(cnt+1, total+i)
        path.pop()

recur(0,0)
print(result)












'''
기본코드
'''
# path = []

# def recur(cnt):

#     # 종료 조건
#     if cnt == 3:
#         print(*path)
#         return

#     # 재귀 호출
#     for i in range(1, 7):
#         path.append(i)

#         recur(cnt+1)

#         path.pop()


# recur(0)