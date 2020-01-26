T = int(input())

bracket_open = ['(', '{', '[']
bracket_close = [')', '}', ']']

for time in range(1, T + 1):
    input_str = input() # test case
    check_list = [] #bracket test list

    for ch in input_str:  
        if ch in bracket_open: # bracket_open에 대해서 먼저 검사
            bracket_index = bracket_open.index(ch)
            check_list.append(bracket_index) # check_list엔 bracket_open, close의 인덱스값만 저장
            									       # bracket_open은 append만

        if ch in bracket_close: # bracket_close에 대해서 검사
            bracket_index = bracket_close.index(ch)
            if check_list == []: # check_list가 비어있으면 append
                check_list.append(bracket_index)
            else:
                if check_list[-1] == bracket_index: # check_list의 마지막 항목이 bracket_open의 인덱스 값과 일치하면
                    check_list.pop() # pop
                else:
                    check_list.append(bracket_index)

    if check_list != []: 
        ans = 0

    else:
        ans = 1

    print("#{} {}".format(time, ans))







