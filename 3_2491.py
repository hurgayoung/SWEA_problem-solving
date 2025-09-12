# 2941 수열

'''
N개의 숫자 (0~9)
연속해서 크거나 같은/작거나 같은 수열 => 가장 길이가 긴 것 찾기
for문을 순회하면서 각 수열 세고, 마지막에 길이 비교하기
'''

# N = int(input())
# arr = list(map(int, input().split()))

# bigger_cnt = 1
# smaller_cnt = 1


# for i in range(N-1): # 0, 1, 2, 3, ..., 7 => i=7까지만 다음 원소랑 비교 가능 (0~8)


#     # 1. 같은 값 포함 연속해서 커지는 수열 만들기
    
#     if arr[i] <= arr[i+1]:    # 1 < 2 를 만족하므로
#         bigger_cnt += 1  # bigger_cnt = 0




#     # 2. 같은 값 포함 연속해서 작아지는 수열 만들기
    
#     if arr[i] >= arr[i+1]:     # 1 > 2 를 만족하지 않으므로
#         smaller_cnt += 1  # smaller_cnt = 0 (아무것도 추가하지 않음)


# if bigger_cnt < 3 and smaller_cnt < 3: # 두 길이 모두 3보다 작을 때 
#     print("2")

# elif bigger_cnt >= 3 and smaller_cnt >= 3 and bigger_cnt > smaller_cnt: # 연속증가배열 길이가 더 클 때
#     print(bigger_cnt)

# elif bigger_cnt >= 3 and smaller_cnt >= 3 and bigger_cnt < smaller_cnt: # 연속감소배열 길이가 더 클 때
#     print(smaller_cnt)

# elif bigger_cnt >= 3 and smaller_cnt >= 3 and bigger_cnt == smaller_cnt: # 두 길이가 동일할 때
#     print(smaller_cnt)






def find_arr_len(arr, N): 
    mx_len = 1   # 최종 최댓값
    inc = 1      # 연속 증가 길이
    dec = 1      # 연속 감소 길이

    for i in range(N-1):
        # 증가 구간 체크
        if arr[i] <= arr[i+1]:
            inc += 1
        else:
            inc = 1

        # 감소 구간 체크
        if arr[i] >= arr[i+1]:
            dec += 1
        else:
            dec = 1
        
        # 현재까지 최대 길이 갱신
        mx_len = max(mx_len, inc, dec)


    return mx_len


# 입력 처리
N = int(input())
arr = list(map(int, input().split()))

ans = find_arr_len(arr, N)
print(ans)