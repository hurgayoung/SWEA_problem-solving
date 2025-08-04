# 임의의 정수를 입력받아 모든 약수 구하기
# 단, 약수가 2개일 경우 소수임을 나타내기



# 리스트를 만들어서 append 하기

n = int(input())

divisors= [] # 빈 리스트 할당

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)

for d in divisors:
    print(f"{d}(은)는 {n}의 약수입니다.")



# append해서 1과 자기 자신만을 약수로 가지는지 확인하기
n = int(input())

divisors = []

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
        print(f"{i}(은)는 {n}의 약수입니다.")

if divisors == [1, n]:
    print(f"{n}(은)는 1과 {n}로만 나눌 수 있는 소수입니다.")


# len 길이로 소수인지 판별하기
n = int(input())

divisors = []  # 약수를 저장할 빈 리스트

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)  # 약수이면 리스트에 추가

# 약수 출력
for d in divisors:
    print(f"{d}(은)는 {n}의 약수입니다.")


# 약수가 2개이면 소수
if len(divisors) == 2:
    print(f"{n}(은)는 1과 {n}로만 나눌 수 있는 소수입니다.")
