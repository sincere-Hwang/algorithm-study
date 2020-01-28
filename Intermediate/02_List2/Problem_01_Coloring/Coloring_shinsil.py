T = int(input())

for test_case in range(1, T + 1):
    N=int(input())
    a = [[0]*10 for k in range(10)]                                               
    cnt = 0

    for n in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                if a[i][j] != color:
                    if a[i][j] < 3:
                        a[i][j] += color
                    if a[i][j] == 3:
                        cnt += 1
                
    print('#{} {}'.format(test_case, cnt))