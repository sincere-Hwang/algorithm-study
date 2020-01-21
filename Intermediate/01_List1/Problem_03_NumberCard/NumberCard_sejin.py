T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 쓰이지 않음
    num_list = list(map(int,input()))

    max_num = -1
    max_cnt = 0
    for i in range(10):
        if num_list.count(i) >= max_cnt:
            max_cnt = num_list.count(i)
            max_num = i
            
    print('#{} {} {}'.format(test_case, max_num, max_cnt))