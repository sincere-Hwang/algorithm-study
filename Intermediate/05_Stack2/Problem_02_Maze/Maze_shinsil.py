import sys
sys.stdin = open('미로_input.txt')

def isWall(x,y):
    if x < 0 or y < 0 or x >= N or y >= N:
        return True
    return False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [0 for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        data[i] = list(map(int, input()))
        if 2 in data[i]:
            y = i
            for j in range(N):
                if data[i][j] == 2:
                    x = j

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    result = 0

    v = [x, y]
    w = []

    while v:

        visited[y][x] = 1

        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]

            if not isWall(testX, testY) and visited[testY][testX] == 0:
                if data[testY][testX] == 0 or data[testY][testX] == 3:
                    w.append((testX, testY))

        if w:
            v = w.pop()
            x = v[0]
            y = v[1]
            if data[y][x] == 3:
                result = 1
                break
        else:
            v = None

    print('#{} {}'.format(tc,result))