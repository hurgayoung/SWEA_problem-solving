# arr = [[0]*5 for _ in range(5)]
N = 5
arr = [
    [1, 3, 3, 6, 7],
    [8, 13, 9, 12, 8],
    [4, 16, 11, 12, 6],
    [2, 4, 1, 23, 2],
    [9, 13, 4, 7, 3]
]

M = 4

# R = 3
# C = 0

for R in range(N-M+1):
    for C in range(N-M+1):

        sum = 0
        for r in range(R, R+M):
            for c in range(C, C+M):
                sum += arr[r][c]

        print(R, C, sum)