# 단조

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    arr = list(map(int, input().split()))


    for i in range(N-2): 
        for j in range(i+1, N-1):
            num = arr[i] * arr[j]
            new_num = str(num)

            max_num = 0

            is_danzo = True
            for m in range(N):
                if new_num[m] > new_num[m+1]:
                    is_danzo = False
            
            if is_danzo  and num > max_num:
                max_num = num

        print(f"#{tc} {max_num}")