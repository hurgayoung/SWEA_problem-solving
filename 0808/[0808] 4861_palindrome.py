T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [input().strip() for _ in range(N)]
    
    found = ""  # 회문 저장

    # 가로 검사
    for i in range(N):
        for j in range(N - M + 1):
            word = board[i][j:j+M]
            if word == word[::-1]:
                found = word
                break
        if found:
            break

    # 세로 검사
    if not found:
        for j in range(N):
            for i in range(N - M + 1):
                word = "".join(board[i+k][j] for k in range(M))
                if word == word[::-1]:
                    found = word
                    break
            if found:
                break

    print(f"#{tc} {found}")
