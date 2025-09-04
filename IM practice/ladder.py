arr = [list(map(int, input().split())) for _ in range(10)]

'''
1 0 0 1 0 0 1 0 0 1
1 0 0 1 0 0 1 0 0 1
1 0 0 1 0 0 1 0 0 1
1 0 0 1 0 0 1 0 0 1
1 0 0 1 1 1 1 0 0 1
1 0 0 0 0 0 1 0 0 1
1 0 0 0 0 0 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 0 0 0 0 0 0 0 2
'''

start_r, start_c = -1, -1

for r in range(10):
    for c in range(10):
        if arr[r][c] == 2:
            start_r, start_c = r, c

r, c = start_r, start_c

while r >= 0:
    print(r,c)
    if c-1 >= 0 and arr[r][c-1] == 1:
        print("왼쪽에 1을 찾았어요")
        while c-1 >= 0 and arr[r][c-1] == 1:
            c -= 1

    elif c+1 < 10 and arr[r][c+1] == 1:
        print("오른쪽에 1을 찾았어요")
        while c+1 < 10 and arr[r][c+1] == 1:
            c += 1

    r -= 1

print(c)