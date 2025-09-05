# 수원구단 축구장 LED

'''
n열(가로) & 4행(세로는 고정!)
i열 & j행 => (i+j+1)이 k의 배수면 변화
픽셀 1(ON), 0(OFF)
구하는 것 = 1(ON) 상태의 픽셀 개수
'''


T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())

    arr = [[0]*n for _ in range(4)]
    count = 0

    for i in range(4): # 세로 순회
        for j in range(n): # 가로 순회
            for time in range(1, k+1):
                if (i+j+1) % time == 0:
                    if arr[i][j] == 1: # 1을 0으로 바꾸기
                        arr[i][j] = 0

                    elif (i+j+1) % time == 0 and arr[i][j] == 0: # 0을 1로 바꾸기
                        arr[i][j] = 1 #count 세기

            if arr[i][j] == 1:
                count += 1

    print(f"#{tc} {count}")