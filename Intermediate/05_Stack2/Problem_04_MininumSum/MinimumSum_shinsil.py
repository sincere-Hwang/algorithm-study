import sys
sys.stdin = open('배열 최소 합_input.txt')

def dfs(y):
    global min
    global sum
    if sum > min:
        return
    if y == N:
        if sum < min:
            min = sum
    else:
        for x in range(N):
            if x not in visited:
                visited.append(x)
                sum += data[y][x]

                dfs(y + 1)
                sum -= data[y][x]
                visited.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    min = float('inf')

    for start in range(N):
        sum = data[0][start]
        visited = [start]
        dfs(1)
    print('#{} {}'.format(tc, min))