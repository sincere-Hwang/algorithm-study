T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    lst = []
    result = 1  # 정상이라 가정
    for c in str1:
        if c == '(' or c == '{':
            lst.append(c)
        elif c == ')' or c == '}':
            # 닫는 기호가 먼저 나올 때
            if len(lst) == 0:
                result = 0
                break
            # 짝이 안맞을 때
            elif c == ')' and lst.pop() != '(':
                result = 0
                break
            elif c == '}' and lst.pop() != '{':
                result = 0
                break
    if len(lst):  # 리스트에 남아있으면
        result = 0
        
    print('#{} {}'.format(test_case, result))