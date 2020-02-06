T = int(input())

for tc in range(1, T+1) :

    # V = Node 개수, E = 간선정보 개수
    V, E = map(int, input().split())

    # 초기 딕셔너리 생성
    Nodes = range(1, V+1)
    Info = [[] for i in range(V)]
    NodesInfo = dict(zip(Nodes, Info))

    # 딕셔너리에 간선 정보 저장
    for e in range(E) :
        Node1, Node2 = map(int, input().split())
        NodesInfo[Node1].append(Node2)
        NodesInfo[Node2].append(Node1)

    # 시작노드, 끝노드 저장
    StartNode, EndNode = map(int, input().split())


    #------------------------------------------
    # BFS로 최단경로 구하기
    # - 층수 : 시작노드에서 끝노드까지 도달할때 필요한 거리

    #              1 <- 시작 노드
    #             4  3
    # 끝 노드 ->  6   2
    #                  5

    # 6의 층수 : 2층 -> 1에서 6까지 두개의 간선을 지남
    #------------------------------------------


    Queue = [StartNode]
    Floor = [0] * (V+1)
    Floor[StartNode] = 0
    while Queue :
        # 1. 현재 노드는 Queue.pop(0) /
        NowNode = Queue.pop(0)

        # 2-1. 현재 노드가 EndNode 이면 해당 층수 반환 / 루프탈출
        if NowNode == EndNode : break
        # 2-2. 현재 노드가 EndNode 가 아니면
        else :
            # 3. Queue에 연결된 노드 append -> Floor 값으로 방문여부 체크 (Floor값이 0이면 방문 x)
            for node in NodesInfo[NowNode] :
                if not Floor[node] :
                    Queue.append(node)

                # 4. 각각의 노드엔 Floor[NowNode] + 1 를 저장 (층수 증가)
                    Floor[node] = Floor[NowNode] + 1

    print("#{} {}".format(tc, Floor[EndNode]))



