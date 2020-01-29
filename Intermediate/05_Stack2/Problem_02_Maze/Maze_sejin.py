def isRoad(Next):
    return canIgo(Next) and MyMap[Next[0]][Next[1]] == 0

def isGoal(Next):
    return canIgo(Next) and MyMap[Next[0]][Next[1]] == 3

def canIgo(Next):
    return 0 <= Next[0] < N and 0 <= Next[1] < N and Next not in Visited


def DFS(Start):
    global result
    Visited.append(Start)
    for i in range(4): # 상하좌우
        if not result:
            Next = (Start[0] + Move[i][0], Start[1] + Move[i][1])
            if isGoal(Next):
                result = 1
                return
            elif isRoad(Next):
                DFS(Next)  # 탐색

                
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 2차원 리스트 입력받음
    MyMap = [list(map(int, input())) for _ in range(N)]
    Visited = []
    
    # 시작지점 찾음
    for r in range(N):
        for c in range(N):
            if MyMap[r][c] == 2:
                Start = (r, c)
    
    # 상 하 좌 우
    Move = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    result = 0
    DFS(Start)
    print('#{} {}'.format(test_case, result))