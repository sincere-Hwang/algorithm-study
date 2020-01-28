TC = int(input())

for test_case in range(1, TC+1):
    test_str = list(input())
    stack_list = []
    for i in test_str:
        if(i == '(' or i == '{'):
            stack_list.append(i)
            # print(stack_list)
        elif not(len(stack_list)):
            if(i == ')' or i == '}'):
                stack_list.append(i)
                break
        elif(len(stack_list)):
            if((i == ')' and stack_list[-1] == '(') or (i == '}' and stack_list[-1] == '{')):
                stack_list.pop()
            elif((i == ')' and stack_list[-1] != '(') or (i == '}' and stack_list[-1] != '{')):
                break


    if not(len(stack_list)):
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))

