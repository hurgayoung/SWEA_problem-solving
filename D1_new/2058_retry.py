# 자릿수 구하기

'''
문자열은 순회가 가능하다!
'''

n = input() #"6789" 'abcd'

arr = []
for i in n: # '6', '7', '8', '9'
    arr.append(int(i)) # [6, 7, 8, 9]

total = sum(arr)

print(total)