#2789 유학 금지

'''
입력받은 내용 일부 삭제
CAMBRIDE 에 포함된 알파벳 지우기
입력받은 문자열(리스트) 순회하면서 캠브릿지 포함된 단어
빈 리스트 만들어서 캠브릿지 아닌 단어 append
'''

T = input()  #LOVA

word = [] # 빈 리스트
arr = ['C', 'A', 'M', 'B','R','I','D','G','E']


for i in T: # i = L, O, V, A
    if i not in arr: # i가 arr에 없으면
        word.append(i) # word에 i를 추가 ['K', 'J']


# word = ['K','J']
for i in word:
    print(i, end = '')
print()