T = int(input())

for i in range(T):
    N,M = map(int, input().split())
    a = list(map(int, input().split()))

    for j in range(N-M+1):
        tmp = 0
        for k in range(M):
            tmp += a[j+k]
        
        if j == 0:
            min = tmp
            max = min
        
        if tmp<min:
            min = tmp
        if tmp>max:
            max = tmp
    print('#{} {}'.format(i+1,max-min))