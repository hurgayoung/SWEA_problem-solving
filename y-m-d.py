# 2056. 연월일 달력
"""
입력
5
22220228
20150002
01010101
20140230
11111111

출력
5
22220228
#1 2222/02/28
20150002
#2 -1
01010101
#3 0101/01/01
20140230
#4 -1
11111111
#5 1111/11/11
"""

# 1. 리스트에 담아서 풀이
t = int(input())
for tc in range(1, t + 1):
    date = input()  # 20250221
    y = int(date[0:4])  # 2025
    m = int(date[4:6])  # 2
    d = int(date[6:8])  # 21
    day = [
        0,
        31,
        28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31,
    ]  # 인덱스 순서에 12개월 맞추기 위해 맨앞에 0 추가

    if (
        1 <= m <= 12 and 0 <= d <= day[m]
    ):  # 인덱스 순서에 담긴 월-마지막일 값을 가져와서 검사에 적용함.
        print(f"#{tc} {y:04d}/{m:02d}/{d:02d}")  #
    else:
        print(f"#{tc} -1")


# 2. 딕셔너리로 풀이
t = int(input())
for tc in range(1, t + 1):
    date = input()
    y = int(date[0:4])
    m = int(date[4:6])
    d = int(date[6:8])

    m_dict = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    if (
        1 <= m <= 12 and 1 <= d <= m_dict[m]
    ):  # 딕셔너리이름[키값] :키값으로 value값 가져오기!!!
        print(f"#{tc} {y:04d}/{m:02d}/{d:02d}")
    else:
        print(f"#{tc} -1")


####################################################

# 3. if else elif문으로 풀이

# T = int(input())
# for tc in range(1, T + 1):
#     arr = input()
#     y = int(arr[0:4])
#     m = int(arr[4:6])
#     d = int(arr[6:8])
#     if m >= 13 or m <= 0:
#         print(-1)
#     else:
#         if m == 1 and not (1 <= d <= 31):
#             print(f"#{tc} -1")
#         elif m == 2 and not (1 <= d <= 28):
#             print(f"#{tc} -1")
#         elif m == 3 and not (1 <= d <= 31):
#             print(f"#{tc} -1")
#         elif m == 4 and not (1 <= d <= 30):
#             print(f"#{tc} -1")
#         elif m == 5 and not (1 <= d <= 31):
#             print(f"#{tc} -1")
#         elif m == 6 and not (1 <= d <= 30):
#             print(f"#{tc} -1")
#         elif m == 7 and not (1 <= d <= 31):
#             print(f"#{tc} -1")
#         elif m == 8 and not (1 <= d <= 31):
#             print(f"#{tc} -1")
#         elif m == 9 and not (1 <= d <= 30):
#             print(f"#{tc} -1")
#         elif m == 10 and not (1 <= d <= 31):
#             print(f"#{tc} -1")
#         elif m == 11 and not (1 <= d <= 30):
#             print(f"#{tc} -1")
#         elif m == 12 and not (1 <= d <= 31):
#             print(f"#{tc} -1")

#         else:
#             print(f"#{tc} {y:04d}/{m:02d}/{d:02d}")  # 정수일 때만 사용 가능


###########################################################

# if else elif문으로 풀이 (2)

# T = int(input())
# for tc in range(1, T + 1):
#     arr = input()
#     y = int(arr[0:4])
#     m = int(arr[4:6])
#     d = int(arr[6:8])
#     if m >= 13 or m <= 0:
#         print(f"#{tc} -1")
#     else:
#         if m == 1:
#             if not (1 <= d <= 31):
#                 print(f"#{tc} -1")
#                 continue
#         elif m == 2:
#             if not (1 <= d <= 28):
#                 print(f"#{tc} -1")
#                 continue
#         elif m == 3:
#             if not (1 <= d <= 31):
#                 print(f"#{tc} -1")
#                 continue
#         elif m == 4:
#             if not (1 <= d <= 30):
#                 print(f"#{tc} -1")
#                 continue
#         elif m == 5:
#             if not (1 <= d <= 31):
#                 print(f"#{tc}-1")
#                 continue
#         elif m == 6:
#             if not (1 <= d <= 30):
#                 print(f"#{tc} -1")
#                 continue
#         elif m == 7:
#             if not (1 <= d <= 31):
#                 print(f"#{tc} -1")
#                 continue
#         elif m == 8:
#             if not (1 <= d <= 31):
#                 print(f"#{tc} -1")
#                 continue
#         elif m == 9:
#             if not (1 <= d <= 30):
#                 print(f"#{tc} -1")
#                 continue
#         elif m == 10:
#             if not (1 <= d <= 31):
#                 print(f"#{tc} -1")
#                 continue
#         elif m == 11:
#             if not (1 <= d <= 30):
#                 print(f"#{tc} -1")
#                 continue
#         elif m == 12:
#             if not (1 <= d <= 31):
#                 print(f"#{tc} -1")
#                 continue
#         # else:
#         print(f"#{tc} {arr[:4]}/{arr[4:6]}/{arr[6:8]}")


##########################################################

# T = int(input())

# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# for tc in range(1, T + 1):
#     date = input()

#     year = date[:4]
#     month = int(date[4:6])
#     day = int(date[6:8])

#     if 1 <= month <= 12:
#         if 1 <= day <= month_days[month]:
#             print(f"#{tc} {year}/{date[4:6]}/{date[6:8]}")
#         else:
#             print(f"#{tc} -1")
#     else:
#         print(f"#{tc} -1")
