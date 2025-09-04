T = int(input())

for tc in range(1, T+1):
    str1 = input().strip()
    str2 = input().strip()

    char_set = set(str1)   # str1의 문자 집합
    arr = list(str2)       # str2를 리스트로 변환

    cnt = {c: 0 for c in char_set}  # 딕셔너리 초기화

    # str2에 있는 글자 세기
    for ch in arr:
        if ch in cnt:       # str1에 있는 글자인 경우만
            cnt[ch] += 1

    print(f"#{tc} {max(cnt.values())}")