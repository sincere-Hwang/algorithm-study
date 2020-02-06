def IsEnd(row, colm) :
    if Array[row][colm] == 3 : return True
    return False

def IsPath(row, colm) :
    if (row < 0 or colm < 0 or row >= N or colm >= N or
       Array[row][colm] == 1 or (row, colm) in Visit):
        return False

    return True

def Maze2(row, colm) :

    Queue = [StartNode]
    Floor = [0]

    ans = 0
    while Queue:
        # 1. 현재 노드는 Queue.pop(0) / 현재 층수 = Floor.pop(0)
        NowNode = Queue.pop(0)
        NowFloor = Floor.pop(0)

        # 2-1. 현재 노드가 EndNode이면 해당 층수-1 반환 / 루프탈출
        if IsEnd(*NowNode):
            ans = NowFloor-1; break
        # 2-2. 현재 노드가 EndNode 가 아니면
        else:
            # 3. Queue에 연결된 노드 append / Floor은 현재 층수 + 1
            for delta in range(4):
                NewRow = NowNode[0] + dy[delta]
                NewColm = NowNode[1] + dx[delta]

                if IsPath(NewRow, NewColm):
                    Queue.append((NewRow, NewColm))
                    Visit.append((NewRow, NewColm))
                    Floor.append(NowFloor + 1)


    return ans


T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    Array = [list(map(int, input())) for i in range(N)]

    for row in range(N) :
        for colm in range(N) :
            if Array[row][colm] == 2 :
                StartNode = (row, colm)

    # print(StartNode)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    Visit = []
    ans = Maze2(*StartNode)
    print("#{} {}".format(tc, ans))





