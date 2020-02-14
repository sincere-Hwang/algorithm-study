import sys
sys.stdin = open('반복문자 지우기_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    str = list(input())
    i = 1
    check = 0
    while len(str) > 1:
        if str[i] == str[i-1]:
            str.pop(i-1)
            str.pop(i-1)
            check = 1
        i += 1

        if i >= len(str):
            if check == 0:
                break
            i = 1
            check = 0

    print('#{} {}'.format(test_case, len(str)))