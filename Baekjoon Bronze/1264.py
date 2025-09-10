#1264 모음의 개수


arr = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']


while True: # 종료 조건을 만날 때까지 반복
    T = input() # How are you today?

    cnt = 0 # 모음 세기

    if T == '#': # #을 만나면 멈추기
        break

    else: # # 아닐 때 문자열 반복
        for i in T: # H, o, w, ...
            if i in arr: # H X o O w X
                cnt += 1

    
    print(f"{cnt}")