'''
공백으로 구분된 백만개의 정수
오름차순 정렬후 배열 A에 저장
A[500000] 출력
'''

# sort/sorted 사용 대신 버블 정렬로 오름차순 정렬

N = list(map(int, input().split()))

def bubble_sort(a, N):   # 정렬할 배열과 배열의 크기
    for i in range(N-1, 0, -1):   # 정렬할 구간의 끝
        for j in range(i):        # 비교할 원소 중 왼쪽 원소의 인덱스
            if a[j] > a[j + 1]:   # 왼쪽 원소가 더 크면
                a[j], a[j + 1] = a[j +1], a[j]  #오른쪽 원소와 교환

A = bubble_sort()

print(A[500000])