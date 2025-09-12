# 연속적으로 값이 커지는 가장 긴 구간을 찾음

arr = [
    [1, 2, 3],
    [3, 7, 8],
    [4, 4, 5],
    [3, 2, 4],
    [4, 3, 2]
]

# 위 1차원 리스트 중에서 순증가하는 것의 개수는?

# for r in range(5):     # 행 나중 순회
#     cnt = 0            # 순증가하는 리스트의 개수
#     for c in range(3): # 열 우선 순회
        
#             cnt += 1   # 카운트 하나 올리기
    
#     print({cnt})



ans = 0
N = len(arr)
for nums in arr:
    print(nums)
    cnt = 1
    for i in range(len(nums) -1):
        if nums[i] < nums[i+1]:
            cnt += 1
    if cnt == len(nums):
        ans += 1
print(ans)