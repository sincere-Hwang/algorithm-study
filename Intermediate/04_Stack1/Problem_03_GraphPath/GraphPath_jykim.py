T = int(input())

for time in range(1, T+1) :
    # V = number of node
    # E = number of path
    V, E = map(int, input().split())

    # node_list, v_list : for DP_dict
    # node_list = 1~V nodes
    # v_list = empty list for each node(to save path)
    node_list = list(range(1, V+1))
    v_list = [[] for i in range(V)]
    DP_dict = dict(zip(node_list, v_list)) # DP_dict = graph path 


    for e in range(E) : # add nodes to DP_dict
        node1, node2 = map(int, input().split())
        DP_dict[node1].append(node2)
        # DP_dict[node2].append(node1) # 방향성존재(단방향으로만 저장)

    start_node, end_node = map(int, input().split())
    check_list = [start_node] # save path
    visited_list = [] # save visited nodes

    ans = 0
    while True :
        if end_node in visited_list : # for answer
            ans = 1
            break

        if check_list == [] : # empty check_list = 모든 경로를 다 방문했다는 뜻
            break             # 이경우 ans = 0으로 반환

        node = check_list.pop()
        if node not in visited_list :
            visited_list.append(node)

    print("#{} {}".format(time, ans))
