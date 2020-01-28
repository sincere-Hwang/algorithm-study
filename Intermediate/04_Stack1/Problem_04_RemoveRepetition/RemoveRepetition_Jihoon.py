

TC = int(input())

for test_case in range(1, TC+1):
    string = list(input())
    # print(string)
    st = 0

    while(True):
        if(st + 1 >= len(string)):
            break
        elif(string[st] == string[st+1]):
            string.pop(st)
            string.pop(st)
            if (st):
                st = st - 1
                # print(string)
                # print(string[st], st)
        else:
            st += 1

    print("#{} {}".format(test_case, len(string)))

