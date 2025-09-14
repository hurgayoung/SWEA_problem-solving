# 연속적으로 값이 커지는 가장 긴 구간을 찾음

arr = [
    [1, 2, 3],
    [3, 7, 8],
    [4, 4, 5],
    [3, 2, 4],
    [4, 3, 2]
]

# 위 1차원 리스트 중에서 순증가하는 것의 개수는?

ans = 0

for nums in arr:
    cnt = 1 # 기본 1
    # 순증가 검사 
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            cnt += 1
    if cnt == len(nums): # cnt가 행의 길이와 같다면 = 모든 인접 쌍이 증가했다면 
        ans += 1
print(ans)