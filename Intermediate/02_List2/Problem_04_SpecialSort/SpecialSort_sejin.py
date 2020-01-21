T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    result_lst = []
    for i in range(10):  # 10개만 출력
        max_num, min_num = num_lst[0], num_lst[0]  # 첫 항을 최대 최소로 설정
        idx = 0
        if i % 2 == 0:  # 최대값의 index 검출
            for j in range(len(num_lst)):
                if num_lst[j] >= max_num:
                    max_num = num_lst[j]
                    idx = j
        else:  # 최소값값의 index 검출
            for j in range(len(num_lst)):
                if num_lst[j] <= min_num:
                    min_num = num_lst[j]
                    idx = j
                    
        result_lst.append(num_lst.pop(idx))  # num_lst.pop -> result_lst

    print('#{} '.format(test_case) + ' '.join(map(str, result_lst)))