# 백준 1110 더하기 사이클

'''
사이클 -> 두 자리 수의 각 자리숫자  
입력받은 N의 사이클 "길이" 구하기
'''




# N = 26

# while 0 <= N < 10:  # N이 10보다 작을 때
#     a = str[0] + str[N] #"01"
#     b = int(str[a][0] + str[a][1]) # 1
        


# while 10 <= N:  # N이 10보다 크거나 같을 때
#     a = N // 10 #5
#     b = N % 10  #5
#     c = a + b   #10, 5

#     if c < 10:
#         c = str[0] + str[c]
    

#     d = str[c][1] #"0"
#     e = str[b] + d #"50"
    
#     N = int(e) #50


N = int(input())
length = 0 
c = ''
d = N
while c != str(N): # 조건은 떠오르면 쓰겠다
    if 0 <= d < 10: #N: 1
        a = str(0) + str(d) # '01'
        
    else: # N: 55 -> '55'
        a = str()

    b = int(a[0]) + int(a[1]) #10

    if b < 10:
        b = str(0) + str(b) #"0b"
    
    else:
        b = str(b) #"10"
    
    c = a[1] + b[1] # "50", "11"

    length += 1

    d = int(c)

print(length)
    