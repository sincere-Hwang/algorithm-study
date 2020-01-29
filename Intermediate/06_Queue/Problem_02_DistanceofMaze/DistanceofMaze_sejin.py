def isSafe(Point): # 범위 안, 예정 안된 곳
    return 0 <= Point[0] < N and 0 <= Point[1] < N and not distance[Point[0]][Point[1]]

def isRoad(Point):
    return isSafe(Point) and my_map[Point[0]][Point[1]] == 0

def isGoal(Point):
    return isSafe(Point) and my_map[Point[0]][Point[1]] == 3

def BFS():
    while Q:
        Start = Q.pop(0)
        for i in range(4):
            Next = (Start[0] + Move[i][0], Start[1] + Move[i][1])
            if isGoal(Next): # 도착지점 찾음
                return distance[Start[0]][Start[1]]
            elif isRoad(Next): # 길 찾음, distance 계산(방문 예정)
                Q.append(Next)
                distance[Next[0]][Next[1]] = distance[Start[0]][Start[1]] + 1
    return 0
    

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 2차원 리스트
    my_map = [list(map(int, input())) for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    
    # 시작점 찾기
    for r in range(N):
        for c in range(N):
            if my_map[r][c] == 2:
                Start = (r, c)

    # 상 하 좌 우
    Move = ((-1, 0), (1, 0), (0, -1), (0, 1))

    Q = [Start]            
    # 출력
    print('#{} {}'.format(test_case, BFS()))