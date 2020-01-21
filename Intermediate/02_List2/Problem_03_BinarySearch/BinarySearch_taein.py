T = int(input())

for case in range(1, T+1):
    P, A, B = map(int, input().split())
    l = [1, 1]
    r = [P, P]
    count = [0, 0]
    while A != int((l[0]+r[0])/2):
        count[0] += 1
        middle = int((l[0]+r[0])/2)
        if middle > A:
            r[0] = middle
        elif middle < A:
            l[0] = middle

    while B != int((l[1]+r[1])/2):
        count[1] += 1
        middle = int((l[1]+r[1])/2)
        if middle > B:
            r[1] = middle
        elif middle < B:
            l[1] = middle

    if count[0] < count[1]:
        print('#{} A'.format(case))
    elif count[0] > count[1]:
        print('#{} B'.format(case))
    else:
        print('#{} 0'.format(case))
