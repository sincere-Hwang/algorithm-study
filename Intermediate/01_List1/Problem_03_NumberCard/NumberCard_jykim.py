for_num = int(input())
for i in range(for_num):
    num = int(input())
    lists = input()

    cnts = []
    for j in lists:
        cnt = lists.count(j)
        cnts.append(cnt)

    max_cnt = max(cnts)

    idx = cnts.index(max_cnt)

    if [max_cnt for i in range(len(cnts))] == cnts :
        idx = lists.index(max(lists))

    print('#{} {} {}'.format(i+1, lists[idx], max_cnt):1


