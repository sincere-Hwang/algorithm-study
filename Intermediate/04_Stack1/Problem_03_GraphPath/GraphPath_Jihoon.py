
def find_route(graph, st, ed, chk):
    chk[st] = 1
    # print(chk, st)
    # print(graph)
    for i in range(1, len(graph)):
        if(graph[st][i] == 1 and chk[i] == 0):
            if(ed == i):
                # print(st ,i)
                return True
            else:
                # print(st, i)
                value = find_route(graph, i, ed, chk)
                if(value == False):
                    chk[i] = 0
                else:
                    return value
    return False

TC = int(input())

for test_case in range(1, TC+1):
    V, E = map(int, input().split())
    map_list = [[0 for _ in range(V+1)]for _ in range (V+1)]
    chk = [0 for _ in range (V+1)]
    for i in range(E):
        st, ed = map(int, input().split())
        map_list[st][ed] = 1
    # print(map_list)
    st, ed = map(int, input().split())
    value = find_route(map_list, st, ed, chk)
    print('#{} {}'.format(test_case, int(value)))