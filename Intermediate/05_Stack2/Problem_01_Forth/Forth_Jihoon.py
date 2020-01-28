TC = int(input())

for test_case in range(1, TC+1):
    string = list(input().split())
    # print(string)
    stack_list = []
    for i in string:
        # print(stack_list)
        if(i == '.'):
            if (len(stack_list) == 1):
                value = stack_list.pop()
            else:
                value = 'error'
                break

        # print(stack_list)
        elif (i == '+' or i == '-' or i == '/' or i == '*'):
            if(len(stack_list) <= 1):
                value = 'error'
                break
            else:
                if(i == '+'):
                    result = int(stack_list.pop(-1)) + int(stack_list.pop(-1))
                elif(i == '-'):
                    result = int(stack_list.pop(-2)) - int(stack_list.pop(-1))
                elif (i == '*'):
                    result = int(stack_list.pop(-1)) * int(stack_list.pop(-1))
                elif(i == '/'):
                    result = int(stack_list.pop(-2)) // int(stack_list.pop(-1))
                stack_list.append(result)
        else:
            stack_list.append(i)

    if(len(stack_list)):
        value = 'error'




    print("#{} {}".format(test_case, value))