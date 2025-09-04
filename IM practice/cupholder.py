# 컵홀더

'''
- 양 끝 좌석에 앉은 사람들은 항상 컵홀더 보장됨
- LL을 S와 동일하게 인식하고, 연속된 LL의 경우 하나 빼주기

구하는 값: 컵홀더에 컵을 꽂을 수 있는 최대 '사람'의 '수'
'''

N = int(input())  # 좌석의 수 N개 입력
arr = list(map(int, input().split()))  # 좌석 정보 입력

cup_holer_succeed = (N-1) + 2

for i in arr:
    if arr[i] == 'LL' and arr[i+1] == 'LL':
        cup_holer_succeed -= 1


print(f"{cup_holer_succeed}")