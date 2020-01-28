def find_exit(stx, sty, edx, edy):
    if(stx == edx and sty == edy):
        return True

    for i in range(4):
        x = stx + dx[i]
        y = sty + dy[i]
        if(x < N and y < N and x >=0 and y>=0):
            if(chk[y][x] == 0 and (map_list[y][x] == '0' or map_list[y][x] == '3')):
                chk[y][x] = 1
                # print('[{},{}]'.format(y, x))
                value = find_exit(x, y, edx, edy)
                if(value == True):
                    return True
                chk[y][x] = 0
                # print('[{},{}]'.format(y, x))
    return False

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    map_list = [list(input()) for _ in range(N)]
    chk = [[0 for _ in range(N)] for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # print(chk)
    # for i in range(N):
    #     print(map_list[i])
    for y in range(N):
        for x in range(N):
            if(map_list[y][x] == '2'):
                stx = x
                sty = y
            elif(map_list[y][x] == '3'):
                edx = x
                edy = y
    chk[sty][stx] = 1
    # print('[{},{}], [{},{}]'.format(sty, stx, edy, edx))
    a = find_exit(stx, sty, edx, edy)
    print("#{} {}".format(test_case, int(a)))