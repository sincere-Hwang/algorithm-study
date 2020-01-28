T = int(input())

def binary_search(l, r, val, cnt):
    c = int((l + r)/2)
    cnt +=1

    if c == val:
        return cnt
    elif c > val:
        return binary_search(l, c, val, cnt)
    elif c < val:
        return binary_search(c, r, val, cnt)

for test_case in range(1, T + 1):
    cnt_A = 0; cnt_B = 0
    P, Pa, Pb = map(int,input().split())
    cnt_A = binary_search(1, P, Pa, cnt_A)
    cnt_B = binary_search(1, P, Pb, cnt_B)

    # 변수 A,B로 바꿔서 이 밑에 print 줄이기 
    if cnt_A == cnt_B:
        print('#{} 0'.format(test_case))
    elif cnt_A > cnt_B:
        print('#{} B'.format(test_case))
    else :
        print('#{} A'.format(test_case))