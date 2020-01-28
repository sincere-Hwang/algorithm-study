T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    b = ''
    
    print('#{} '.format(test_case), end='')
    
    for i in range(N-1):
        max = min = a[i]
        for j in range(i+1, N):
            if (a[j]<min):
                min = a[j]
                min_ = j
            if (a[j]>max):
                max = a[j]
                max_ = j
        if (i%2):
            a[i], a[min_] = a[min_], a[i]
        else:
            a[i], a[max_] = a[max_], a[i]
            
    for i in range(10):
        print(a[i],end=' ')
    print()

    