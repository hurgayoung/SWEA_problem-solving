T = int(input())  # 테스트 케이스 수 입력

# 재귀 함수 정의
def f(idx, sum):
    """
    idx : 현재 선택해야 하는 행 번호
    sum : 지금까지 선택한 수들의 합
    """
    global min_sum  # 최소합을 갱신하기 위해 전역변수 사용

    # 기저조건: 모든 행을 선택했으면 현재 합과 최소합 비교
    if idx == N:
        if sum < min_sum:
            min_sum = sum  # 최소합 갱신
        return

    # 현재 행(idx)에서 열을 선택
    for i in range(N):
        if not visited[i]:  # 해당 열을 아직 선택하지 않았다면
            visited[i] = True  # 선택 표시
            f(idx + 1, sum + arr[idx][i])  # 다음 행 선택 재귀 호출
            visited[i] = False  # 백트래킹: 선택 초기화

# 각 테스트 케이스 처리
for tc in range(1, T+1):
    N = int(input())  # NxN 배열 크기 입력
    arr = [list(map(int, input().split())) for _ in range(N)]  # 배열 입력

    visited = [False] * N  # 각 열 선택 여부 표시
    min_sum = float('inf')  # 최소합 초기화

    f(0, 0)  # 0번째 행에서 숫자 선택 시작, 초기 합은 0

    print(f"#{tc} {min_sum}")  # 결과 출력
