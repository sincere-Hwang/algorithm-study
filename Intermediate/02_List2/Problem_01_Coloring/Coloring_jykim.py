T = int(input())

for time in range(1, T+1) :

    N = int(input()) # N : 칠할 영역의 개수

    # input_lists : 2 2 4 4 1
    # (2, 2) -> 시작 좌표, (4, 4) -> 끝좌표
    # 1 -> color_index // 1(red), 2(blue)
    input_lists = []
    for n in range(N) :
        input_list = list(map(int, input().split()))
        input_lists.append(input_list)

    # color_matrix : red면 해당 좌표를 color_matrix[0]에 추가, blue면 color_matrix[1]에 추가
    color_matrix = [[] for i in range(2)]
    for n in range(N) :
        color_index = input_lists[n][4]
        x1 = input_lists[n][0]; x2 = input_lists[n][2];
        y1 = input_lists[n][1]; y2 = input_lists[n][3];

        # 이부분 좀더 간단하게 만들고 싶어요..
        temp_list = [(i, j) for i in range(x1, x2 + 1) for j in range(y1, y2 + 1)]

        if color_index == 1 :
            color_matrix[0] += temp_list
        else :
            color_matrix[1] += temp_list



    #ans_matrix = red와 blue의 교집합
    ans_matrix = list(set(color_matrix[0]) & set(color_matrix[1]))

    print("#{} {}".format(time, len(ans_matrix)))
