# 연월일 달력


T = int(input())

for tc in range(1, T+1):

    n = input() # '20220228'

    arr = []
    for i in n:
        arr.append(i) # arr -> ['2', '0', '2', '2', '0', '2', '2', '8']
        
    year = arr[0] + arr[1] + arr[2] + arr[3] # 2022
    month = arr[4] + arr[5] # 02
    day = arr[6] + arr[7] # 28

    # 월/일 조건을 만족하면 그림대로 출력, 아니면 -1
    if int(month) == 1 and 0 < int(day) <= 31:
            print(f"#{tc} {year}/{month}/{day}")
    
    if int(month) == 2 and 0 < int(day) <= 28:
            print(f"#{tc} {year}/{month}/{day}")

    if int(month) == 3 and 0 < int(day) <= 31:
            print(f"#{tc} {year}/{month}/{day}")
    
    if int(month) == 4 and 0 < int(day) <= 30:
            print(f"#{tc} {year}/{month}/{day}")
    
    if int(month) == 5 and 0 < int(day) <= 31:
            print(f"#{tc} {year}/{month}/{day}")
    
    if int(month) == 6 and 0 < int(day) <= 30:
            print(f"#{tc} {year}/{month}/{day}")
    
    if int(month) == 7 and 0 < int(day) <= 31:
            print(f"#{tc} {year}/{month}/{day}")
    
    if int(month) == 8 and 0 < int(day) <= 31:
            print(f"#{tc} {year}/{month}/{day}")

    if int(month) == 9 and 0 < int(day) <= 30:
            print(f"#{tc} {year}/{month}/{day}")

    if int(month) == 10 and 0 < int(day) <= 31:
            print(f"#{tc} {year}/{month}/{day}")

    if int(month) == 11 and 0 < int(day) <= 30:
            print(f"#{tc} {year}/{month}/{day}")
    
    if int(month) == 12 and 0 < int(day) <= 31:
            print(f"#{tc} {year}/{month}/{day}")

    if not printed:  # 한 번도 출력 안 됐으면 -1 출력
        print(f"#{tc} -1")