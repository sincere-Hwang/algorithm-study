TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    cnt = [1, 3]
    N //= 10
    # print(N)
    for i in range(2, N):
        cnt.append(cnt[i - 1] + cnt[i - 2] * 2)

    print("#{} {}".format(test_case, cnt[N-1]))