# 스도쿠 숫자퍼즐

# 스도쿠 숫자퍼즐

T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    # 1. 행 검사
    for row in arr:
        if len(set(row)) != 9:
            result = 0
            break

    # 2. 열 검사
    if result:
        for c in range(9):
            col = [arr[r][c] for r in range(9)]
            if len(set(col)) != 9:
                result = 0
                break

    # 3. 3x3 박스 검사 (델타)
    if result:
        center = [1, 4, 7]
        dr = [-1, -1, -1,  0, 0, 0,  1, 1, 1]
        dc = [-1,  0,  1, -1, 0, 1, -1, 0, 1]

        for r in center:
            for c in center:
                block = []
                for k in range(9):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    block.append(arr[nr][nc])
                if len(set(block)) != 9:
                    result = 0
                    break
            if result == 0:
                break

    print(f"#{tc} {result}")





# T = int(input())
 
# for t in range(1, T+1):
#     sudoku = [list(map(str, input().split())) for _ in range(9)]
#     test = 1
#     for i in range(9):
#         col = set()           # 행 우선 순회
#         for j in range(9):
#             col.add(sudoku[i][j])
         
#         if len(col) != 9 :
#             test = 0
                 
#     for j in range(9):  
#         row = set()         # 열 우선 순회
#         for i in range(9): 
#             row.add(sudoku[i][j])
#         # print(len(row))
#         if len(row) != 9:
#                 test =0              
 
#     di = [0, 0, -1, 1] + [-1, 1, -1, 1]     
#     dj = [-1, 1, 0, 0] + [-1, -1, 1, 1]
 
#     center =[1, 4, 7]
#     for i in center:        # (1,1) (1,4) (1,7) (4,1) (4,4) (4,7) (7,1) (7,4) (7,7) 팔방탐색
#         for j in center:
#             box = set()
#             box.add(sudoku[i][j])
#             for d in range(8):
#                 ni = i + di[d]
#                 nj = j + dj[d]
                  
#                 box.add(sudoku[ni][nj])
                                
#             if len(box) != 9:
#                 test = 0 
               
#     print(f'#{t} {test}')











# # import sys
# # sys.stdin = open("input.txt")
 
# T = int(input())
# for tc in range(1, T+1):
#     arr = [list(map(int, input().split())) for _ in range(9)]
#     value = 1
 
#     # 검증 1
#     for r in range(9):
#         test_set = set()
#         for c in range(9):
#             test_set.add(arr[r][c])
#         if len(test_set) == 9:
#             pass
#         else:
#             value = 0
             
     
#     # 검증 2
#     for r in range(9):
#         test_set = set()
#         for c in range(9):
#             test_set.add(arr[c][r])
#         if len(test_set) == 9:
#             pass
#         else:
#             value = 0
             
 
#     # 검증 3
#     dr = [-1,-1,-1,0,0,1,1,1]
#     dc = [-1,0,1,-1,1,-1,0,1]
#     for r in [1,4,7]:
#         test_set = set()
#         for c in [1,4,7]:
#             test_set.add(arr[r][c])
#             for d in range(8):
#                 nr, nc = r + dr[d], c + dc[d]
#                 test_set.add(arr[nr][nc])
#             if len(test_set) == 9:
#                 pass
#             else:
#                 value = 0
                 
 
#     print(f'#{tc} {value}')