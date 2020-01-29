def FindMin(row):
    global my_sum, my_min
    # sum이 min을 넘을 때 버림
    if my_sum > my_min:
        return
    # 범위를 벗어나면 최소값 갱신
    if row == N:
        if my_sum < my_min:
            my_min = my_sum
            return
    
    for col in range(N):
        if not visited[col]:
            # 확장
            visited[col] = True
            my_sum += my_map[row][col]
            FindMin(row + 1)
            # 축소
            my_sum -= my_map[row][col]
            visited[col] = False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    my_map = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    my_sum, my_min = 0, N * 9
    FindMin(0)
    print('#{} {}'.format(test_case, my_min))