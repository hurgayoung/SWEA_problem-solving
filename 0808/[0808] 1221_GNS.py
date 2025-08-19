T = int(input())

words_order = ["ZRO", "ONE", "TWO", "THR", "FOR",
               "FIV", "SIX", "SVN", "EGT", "NIN"]

word_to_num = {w: i for i, w in enumerate(words_order)}

for tc in range(T):
    # 테스트 케이스의 길이 정수형으로 입력받기
    tc, n = input().split()
    n = int(n)

    words = input().split()

    counts = [0]* 10

    for w in words:
        counts[word_to_num[w]] += 1

    result = []
    for i in range(10):
        result.extend([words_order[i]] * counts[i])
        

    print(f"{tc}")
    print(" ".join(result))