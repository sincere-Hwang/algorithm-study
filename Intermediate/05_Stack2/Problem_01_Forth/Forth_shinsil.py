import sys
sys.stdin = open('Forth_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    string = list(input().split())
    stack = []
    for char in string:
        if char.isdigit():
            stack.append(int(char))
        elif char == '.':
            if len(stack) > 1:
                print('#{} error'.format(test_case))
                break
            print('#{} {}'.format(test_case, stack.pop()))
        elif len(stack) >= 2:
            a = stack.pop()
            b = stack.pop()

            if char == '+':
                stack.append(b + a)
            elif char == '-':
                stack.append(b - a)
            elif char == '*':
                stack.append(b * a)
            elif char == '/':
                stack.append(b // a)
        else:
                print('#{} error'.format(test_case))
                break
