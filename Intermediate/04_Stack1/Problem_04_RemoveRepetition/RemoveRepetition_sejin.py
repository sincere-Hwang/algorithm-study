T = int(input())

for test_case in range(1, T + 1):
    Str = input()
    List = []
    for c in Str:
        if len(List) == 0:
            List.append(c)
        elif c != List[-1]:
            List.append(c)
        else:  # 중복일 때
            List.pop()
            
    print('#{} {}'.format(test_case, len(List)))