arr = [[0]*5 for _ in range(5)]



l = 2
for r in range(5):
    print(f"== r: {r} ==")
    for c in range(0+l, 5-l):
        print(c, end=' ')
        arr[r][c] = 1
    print()
    if r < 2:
        l -= 1
    else:
        l += 1

for r in range(5):
    print(arr[r])