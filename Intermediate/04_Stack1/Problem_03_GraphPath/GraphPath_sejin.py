def DFS(START):
    visited[START] = True
    result = 0
    if START in my_map: # NEXT 있으면
        for NEXT in my_map[START]:
            if not visited[NEXT]:
                if NEXT == G:
                    return 1 # Goal
                elif not result: # 결과가 안났다면 계속 탐색
                    result += DFS(NEXT)
    return result

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    
    my_map = {} # dictionary
    visited = [False for _ in range(V + 1)]
    result = 0
    
    for _ in range(E):
        Start, End = map(int, input().split())
        if Start not in my_map:
            my_map[Start] = [End]
        else:
            my_map[Start].append(End)
        
    S, G = map(int, input().split())
    print('#{} {}'.format(test_case, DFS(S)))