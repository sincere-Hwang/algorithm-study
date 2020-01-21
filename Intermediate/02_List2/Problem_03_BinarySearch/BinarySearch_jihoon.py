TC = int(input())


def binarysearch(st, ed, value, cnt):
    mid = (st + ed) // 2
    cnt += 1

    if(mid == value):
        a = cnt
        return a
    if(mid < value):
        return binarysearch(mid, ed, value, cnt)
    elif(mid > value):
        return binarysearch(st, mid, value, cnt)



for i in range(1, TC+1):
    P, A, B = map(int, input().split())
    A_st, B_st = 1, 1
    cnt_A, cnt_B = 0, 0
    cnt_A = binarysearch(A_st, P, A, cnt_A)
    cnt_B = binarysearch(B_st, P, B, cnt_B)

    result = 0
    if(cnt_A > cnt_B):
        result = 'B'
    elif(cnt_A == cnt_B):
        result = 0
    else:
        result = 'A'

    print('#{} {}'.format(i, result))


