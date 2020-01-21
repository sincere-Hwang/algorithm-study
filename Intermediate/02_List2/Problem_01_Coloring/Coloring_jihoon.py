TC = int(input())

for i in range(1, TC + 1):
    color_map = [[0 for _ in range(10)] for _ in range(10)]


    N = int(input())
    cnt = 0
    for _ in range(N):
        st_x, st_y, ed_x, ed_y, clr = map(int, input().split())


        for x in range(st_x, ed_x+1):
            for y in range(st_y, ed_y+1):
                color_map[y][x] += clr

    for x in range(10):
        for y in range(10):
             if(color_map[y][x] == 3):
                    cnt += 1

    print('#{} {}'.format(i, cnt))

