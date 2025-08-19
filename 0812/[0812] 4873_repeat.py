T = int(input())

for tc in range(1, T+1):
    s = input().strip()
    
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    result = len(stack)

    print(f"#{tc} {result}")