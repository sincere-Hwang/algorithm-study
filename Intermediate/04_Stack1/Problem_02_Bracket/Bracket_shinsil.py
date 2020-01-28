T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    bracket = []
    cnt = 1

    for char in str1:
        if char == '{' or char == '(':
            bracket.append(char)
        elif not bracket and (char == '}' or char == ')'):
            cnt = 0
            break
        elif char == '}':
            if bracket[-1] == '{':
                bracket.pop()
            else:
                cnt = 0
                break
        elif char == ')':
            if bracket[-1] == '(':
                bracket.pop()
            else:
                cnt = 0
                break
    if bracket:
        cnt = 0

    print('#{} {}'.format(test_case, cnt))