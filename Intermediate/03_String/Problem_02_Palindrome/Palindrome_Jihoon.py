
TC = int(input())

for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    a_list = []
    tmp_list = []
    result_list = []

    for i in range(N):
        a_list.append(list(input()))

    for y in range(N):
        for x in range(0, N-M+1):
            tmp_list = a_list[y][x : x+M]
            value = True
            for i in range(M//2):
                if(tmp_list[i] != tmp_list[-1-i]):
                    value = False

            if(value):
                result_list = tmp_list


    if not(len(result_list)):
        a_list = list(map(list , zip(*a_list)))
        for y in range(N):
            for x in range(0, N - M + 1):
                tmp_list = a_list[y][x: x + M]
                value = True
                for i in range(M // 2):
                    if (tmp_list[i] != tmp_list[-1 - i]):
                        value = False

                if (value):
                    result_list = tmp_list

    print('#{} {}'.format(test_case, ''.join(result_list)))