T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())
    N_num = list(map(int, input().split()))

    min = 10000*M
    max = 0

    for i in range(N+1-M):
        sum_N = 0
        for j in range(M):
            sum_N += N_num[i+j]

        if sum_N <= min:
            min = sum_N
        if sum_N >= max:
            max = sum_N

    print(f'#{case} {max-min}')
