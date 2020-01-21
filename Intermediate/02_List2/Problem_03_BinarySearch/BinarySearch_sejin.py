def BS(page, target):  # 이진 탐색
    l = 1
    r = page
    cnt = 0
    while(r - l > 1): # 두 장 이하로 남으면 탈출
        c = (l+r)//2  # int((l+r)/2)와 같음
        cnt += 1  # 번째 시도
        if target < c:
            r = c
        elif target > c:
            l = c
        else:  # target == c
            break
    if l + 1 == r:  # 두 장 남은 경우
        cnt += 1 # 찾음
    return cnt


T = int(input())

for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    cnt_a = BS(P, Pa)
    cnt_b = BS(P, Pb)
    
    result = 0
    if cnt_a < cnt_b:
        result = 'A'
    elif cnt_a > cnt_b:
        result = 'B'
        
    print('#{} {}'.format(test_case, result))