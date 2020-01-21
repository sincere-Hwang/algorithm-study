T = int(input())  # 테스트 케이스 개수
A = [i for i in range(1, 13)]  # 집합 A

for case in range(1, T+1):
    N, K = map(int, input().split())  # N개의 원소, K 부분 원소의 합
    cnt = 0  # 갯수 카운터
    for i in range(1 << len(A)):  # 2**12개의 부분집합
        sub_A = []  # 부분집합을 담을 리스트
        for j in range(len(A)):  # j탐색
            if i & (1 << j):  # i에서 j번째 비트 1인지 확인
                sub_A.append(A[j])  # 비트 1인 애들이 부분집합의 수이기 때문에 추가
        if len(sub_A) == N and sum(sub_A) == K:  # 부분집합의 길이가 N이면서 합이 K인 값이라면 cnt 증가
            cnt += 1
    print(f'#{case} {cnt}')

    # bit = [0, 0, 0, 0]
    # for i in range(2):
    #     bit[0] = i
    #     for j in range(2):
    #         bit[1] = j
    #         for k in range(2):
    #             bit[2] = k
    #             for l in range(2):
    #                 bit[3] = l
    #                 print(bit)

    # arr = [3, 6, 7, 1, 5, 4]
    # n = len(arr)

    # for i in range(1 << n):
    #     for j in range(n):
    #         if i & (1 << j):
    #             print(arr[j], end=",")
    #         print()
