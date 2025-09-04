# 연월일 달력


T = int(input())

for tc in range(1, T+1):

    n = input()  # '20220228'

    arr = []
    for i in n:
        arr.append(i)

    year = arr[0] + arr[1] + arr[2] + arr[3]  # 2022
    month = arr[4] + arr[5]  # 02
    day = arr[6] + arr[7]    # 28

    if int(month) == 1 and 0 < int(day) <= 31:
        print(f"#{tc} {year}/{month}/{day}")

    elif int(month) == 2 and 0 < int(day) <= 28:
        print(f"#{tc} {year}/{month}/{day}")

    elif int(month) == 3 and 0 < int(day) <= 31:
        print(f"#{tc} {year}/{month}/{day}")

    elif int(month) == 4 and 0 < int(day) <= 30:
        print(f"#{tc} {year}/{month}/{day}")

    elif int(month) == 5 and 0 < int(day) <= 31:
        print(f"#{tc} {year}/{month}/{day}")

    elif int(month) == 6 and 0 < int(day) <= 30:
        print(f"#{tc} {year}/{month}/{day}")

    elif int(month) == 7 and 0 < int(day) <= 31:
        print(f"#{tc} {year}/{month}/{day}")

    elif int(month) == 8 and 0 < int(day) <= 31:
        print(f"#{tc} {year}/{month}/{day}")

    elif int(month) == 9 and 0 < int(day) <= 30:
        print(f"#{tc} {year}/{month}/{day}")
        
    elif int(month) == 10 and 0 < int(day) <= 31:
        print(f"#{tc} {year}/{month}/{day}")

    elif int(month) == 11 and 0 < int(day) <= 30:
        print(f"#{tc} {year}/{month}/{day}")

    elif int(month) == 12 and 0 < int(day) <= 31:
        print(f"#{tc} {year}/{month}/{day}")

    else:
        print(f"#{tc} -1")


        '''
        if → if / elif / else 체인으로 변경

        원래 코드는 if들을 전부 독립적으로 써서, 조건이 여러 개 걸리면 여러 번 출력될 수 있었음.

        바꾼 코드는 첫 번째로 맞는 조건만 실행되도록 elif로 이어줌.

        else의 귀속 위치 수정

        원래는 else가 **마지막 if (month == 12)**에 붙어 있어서 “12월이 아니면 -1”이 출력되는 버그가 있었음.

        바꾼 코드는 if/elif **체인의 마지막 else**로 두어서, 어느 월 조건에도 안 맞을 때만 -1이 출력됨.

        '''


        # T = int(input())

        # for tc in range(1, T+1):
        # n = input().strip()  # '20220228'

        # year = n[:4]   # '2022'
        # month = n[4:6] # '02'
        # day = n[6:]    # '28'

        # # 월별 최대 일수 (윤년 고려 X)
        # month_days = {
        #         1: 31, 2: 28, 3: 31, 4: 30,
        #         5: 31, 6: 30, 7: 31, 8: 31,
        #         9: 30, 10: 31, 11: 30, 12: 31
        # }

        # m = int(month)
        # d = int(day)

        # # 유효한 월인지, 유효한 일인지 검사
        # if m in month_days and 1 <= d <= month_days[m]:
        #         print(f"#{tc} {year}/{month}/{day}")
        # else:
        #         print(f"#{tc} -1")
