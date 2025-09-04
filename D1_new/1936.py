# 1대1 가위바위보

A, B = map(int, input().split())

if A > B:
    print("A")

elif A == 1 and B == 3:
    print("A")

else:
    print("B")