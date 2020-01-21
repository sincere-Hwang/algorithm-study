T = int(input())

for case in range(1, T+1):
    N = int(input())
    count = 0
    color_box = [[0 for num in range(10)] for num2 in range(10)]
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if color == 1:
                    if color_box[i][j] == 3:
                        continue

                    elif color_box[i][j] == 2:
                        color_box[i][j] = 3
                        count += 1

                    else:
                        color_box[i][j] = 1

                else:
                    if color_box[i][j] == 3:
                        continue

                    elif color_box[i][j] == 1:
                        color_box[i][j] = 3
                        count += 1

                    else:
                        color_box[i][j] = 2

    print(f'#{case} {count}')
