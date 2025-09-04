# Flatten

for T in range(1, 11):

    N = int(input()) # 진행할 덤프 숫자 

    # 상자의 높이를 리스트로 받기
    box_height = list(map(int, input().split()))

    


    # 덤프하는 평탄화 과정
    def dump(N ,box_height):
        for _ in range(N):
            # 현재 상자 최고점, 최저점 찾기
            max_height = max(box_height)
            min_height = min(box_height)

            box_height[box_height.index(max_height)] = max_height -1
            box_height[box_height.index(min_height)] = min_height +1

            
            # result = max_height - min_height
            result = max(box_height) - min(box_height)
        return result
    

    # 높이 차 반환
    print(f"#{T} {dump(N, box_height)}")