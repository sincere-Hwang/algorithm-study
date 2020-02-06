def Maze() :

    # VisitPoint = 방문한 위치
    # CheckNode = 현재 위치


    while VisitPoint :
        # print(CheckNode)
        CheckNode = VisitPoint.pop() # 현재 위치
        Nlist[CheckNode[0]][CheckNode[1]] = 1 # 방문한 노드 = 1


    # --- 주변 노드 체크 --------------------------------------------------
        for i in range(4) :
            # x = row, y = colm
            x, y = CheckNode[0] + dx[i], CheckNode[1] + dy[i] # CheckNode의 주변 노드

            # boundary 넘으면 패스
            if x < 0 or y < 0 or x >= N or y >= N : continue
            # 주변에 3이 있으면 return 1
            elif Nlist[x][y] == 3 : return 1
            elif Nlist[x][y] == 0 : VisitPoint.append((x, y))

    return 0


T = int(input())
for tc in range(1, T+1) :
    N = int(input())

    Nlist = [list(map(int, input())) for i in range(N)]

    for row in range(N) :
            for colm in range(N) :
                if Nlist[row][colm] == 2 :
                    VisitPoint = [(row, colm)] # start node


    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]


    ans = Maze()
    print("#{} {}".format(tc, ans))


