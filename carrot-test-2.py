arr = [1, 2, 3, 4, 3, 7, 8, 9, 4, 4, 5, 5, 3, 2, 4, 2, 4, 3, 2, 2, 1, 2, 7, 9]

# arr : 아주 긴 당근
# 길이가 4개씩 토막을 낸다.
# 토막 중에서 순증가하는 토막의 개수는?


# slice_arr = arr[0:len(arr)-1:4] # 처음부터 끝까지 4만큼 건너뛰기 -> 1,3,4,3,4,1

# for j in slice_arr: # 1,3,4,3,4,1
#     for i in arr:
#         new_arr = [] # 빈 리스트
#         new_arr.append(slice_arr[i] + arr[j])




# while start < N:
#     print(start)
#     inc_len = 1
#     for i in range(start, start + 3):
#         print(i, end=',')
#         if arr[i] < arr[i+1]:
#             inc_len += 1
#     print()
#     if inc_len == 4:
#         ans += 1
#     start += 4
# print(ans)

start = 0
ans = 0
N = len(arr)


for start in range(0, len(arr), 4): # start = 0, 4, 8, 12, 16, 20 => 시작하는 배열 내 인덱스
    inc_len = 1
    for i in range(start, start+3): # 구간 내 순증가 확인을 위한 범위 정하기 => i+1 때문에 구간 범위 조심!
        if arr[i] < arr[i+1]:
            inc_len += 1
    if inc_len == 4:
        ans += 1
print(ans)