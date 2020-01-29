def BFS():
    while Q: # 큐가 빌 때 까지
        Start = Q.pop(0)
        for Next in range(V + 1):
            if node_map[Start][Next] and not distance[Next]:
                distance[Next] = distance[Start] + 1
                if Next == G:
                    return distance[G]
                else:
                    Q.append(Next)
    return 0 # 연결 안 됨

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    node_map = [[0] * (V + 1) for _ in range(V + 1)] # 0번 노드 안 씀
    for _ in range(E): # node_map 입력
        n1, n2 = map(int, input().split())
        node_map[n1][n2] = 1
        node_map[n2][n1] = 1
    S, G = map(int, input().split())
    Q = [S]
    distance = [0] * (V + 1) # 거리 표시 및 방문 여부 확인
    print('#{} {}'.format(test_case, BFS()))