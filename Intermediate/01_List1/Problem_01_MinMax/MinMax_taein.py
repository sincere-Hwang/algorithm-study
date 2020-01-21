cases = int(input())
for case in range(1, cases+1):
    num = int(input())
    sort_num_list = sorted(list(map(int, input().split(" "))))
    length = len(sort_num_list)
    diff = sort_num_list[length-1]-sort_num_list[0]
    print(f'#{case} {diff}')
