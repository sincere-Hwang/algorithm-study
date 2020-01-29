def FindCase(x):  # x == 현재 위치
    if x > width:  # 범위를 벗어나면 버림
        return 0
    elif x == width:  # 끝까지 오면 1 리턴
        return 1
    return FindCase(x + 10) + FindCase(x + 20) * 2

#테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    width = int(input())
    print('#{} {}'.format(test_case, FindCase(0)))