# 연속한 1의 개수

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    text = list(input())

    max_length = 0
    count = 0

    for char in text:
        if char == '1':
            count = count + 1
            if count > max_length:
                max_length = count
        else:
            count = 0 
    
    print(f"#{tc} {max_length}")