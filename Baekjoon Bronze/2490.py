# 2490 윷놀이

'''
배 = 0 또는 등 = 1 -> 도개걸윷모 결정
한 줄에 4개 입력받아서 결정, 순서는 상관 x, 개수로 확인
입력은 3줄! for문으로 반복하면서 각 줄별로 출력
반복하는 0의 개수로 판단
A 도 0111
B 개 0011
C 걸 0001
D 윷 0000
E 모 1111
'''


for i in range(3): #012
    arr = list(map(int, input().split())) # 입력값 각 줄 [0,1,0,1]
   
    cnt = 0 # 0의 개수로 도개걸윷모 판별하기
    for j in arr:
        if j == 0: # 순회해서 0을 만나면
            cnt += 1

    if cnt == 1:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    elif cnt == 4:
        print('D')
    elif cnt == 0:
        print('E')