'''
stack 문제

아래 코드는 스택의 기본 연산을 구현한 코드지만, 오류가 존재합니다. 존재하는 모든 오류들에 대해 오류의 이유를 설명하고 올바르게 수정하세요. 
stack = [0]


stack.append(10)
stack.append(20)
stack.append(30)


popped_element = stack.pop(0)
'''

stack = [] # 빈 스택을 만드려면 [0]이 아니라 이렇게 나타내야 해요

stack.append(10)
stack.append(20)
stack.append(30)


popped_element = stack.pop()

'''
queue 문제

아래는 한 콜센터의 상담원 연결 대기열을 큐(Queue) 자료구조로 나타낸 것입니다. 다음 순서대로 고객이 연결되거나 대기열에 추가되었을 때, 최종적으로 대기열에 남은 고객들의 순서를 서술하세요.

이현서 고객이 대기열에 진입(Enqueue)

방승재 고객이 대기열에 진입(Enqueue)

허가영 고객이 대기열에 진입(Enqueue)

첫 번째 고객이 상담원과 연결(Dequeue)

정민선 고객이 대기열에 진입(Enqueue)

두 번째 고객이 상담원과 연결(Dequeue)

'''

# 허가영, 정민선