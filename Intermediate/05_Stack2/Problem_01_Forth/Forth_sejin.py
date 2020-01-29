T = int(input())
for test_case in range(1, T + 1):
    inputList = input().split()
    MyList = []
    try:
        for i in inputList:
            if i == '.':
                result = MyList.pop()
                if len(MyList) != 0:
                    result = 'error'
                break
            elif i == '+':
                MyList.append(MyList.pop(-2) + MyList.pop())
            elif i == '-':
                MyList.append(MyList.pop(-2) - MyList.pop())
            elif i == '*':
                MyList.append(MyList.pop(-2) * MyList.pop())
            elif i == '/':
                MyList.append(MyList.pop(-2) // MyList.pop())
            else:  # 숫자는 int형으로 변환
                MyList.append(int(i))
                
    except:  # 에러
        result = 'error'
        
    print('#{} {}'.format(test_case, result))