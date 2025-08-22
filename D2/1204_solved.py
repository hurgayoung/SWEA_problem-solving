# 최빈수 구하기
# input() : 한줄을 문자열로 가져오기


T = int(input()) # "10"

for tc in range(1, T+1):
    input() # 첫 줄의 테스트 케이스 번호 무시하기 "1"
    # 수학 성적 리스트로 입력받기
    scores = list(map(int, input().split())) # "41 85 ...."

    # zero_cnt = 0 # 0의 갯수 세기

    cnt = [0] * 101 # 길이가 101인 리스트 => 인덱스 0부터 100까지 있음
    # cnt[0] : 0
    # cnt[1] : 0
    # ...
    # cnt[100]: 0

    # for score in scores: # score: [41, 85, ...]
        # 카운팅 배열의 해당 숫자를 인덱스로 사용해서 카운트 늘려주기
        # cnt[score] += 1
        # print(score)
        # if score == 0:
            # zero_cnt += 1
    
    # 학생의 수가 1000명으로 고정
    for i in range(1000): # i: [0, 999]
        cnt[scores[i]] += 1

    
    # print(zero_cnt)
    # print(cnt) 

    max_cnt = 0 # 카운트 중에서 최대값(최소값으로 초기화)
    max_score = -1 # 최대값일 때의 점수 저장


    for score in range(101):
        if cnt[score] > max_cnt:
            max_cnt = cnt[score]
            max_score = score


    # print(max_score, max_cnt)
    print(f"#{tc} {max_score}")

    
    # 목표: 최빈수 구하기
    # 가장 많이 나온 수
    # 각 점수가 나온 개수를 세고, 그 개수들 중에서 가장 값이 큰 것 고르기
    # 카운팅 + 최대값 구하기

    # 0의 개수, 1의 개수, 2의 개수, .... , 100의 개수
    
    # 카운팅 배열 만들기
    # 카운팅 배열
    # 0의 개수, 1의 개수, 2의 개수, .... , 100의 개수 => 배열로 저장
    # arr[0] : 0의 개수
    # arr[1] : 1의 개수
    # ...
    # arr[100] : 100의 개수


    break
    # print(f"#{tc} {}")