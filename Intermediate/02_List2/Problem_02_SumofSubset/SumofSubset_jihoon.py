
TC = int(input())

for i in range(1, TC+1):
    N, K = map(int, input().split())
    A = [i for i in range(1, 13)]
    cnt = 0
    for j in range(1<<len(A)):
        tmp_list = list()
        for k in range(len(A)):
            if(j & (1<<k)):
                tmp_list.append(A[k])
        if(len(tmp_list) == N and sum(tmp_list) == K):
            cnt += 1


    print("#{} {}".format(i, cnt))
