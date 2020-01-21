T = int(input())

for test_case in range(1, T + 1):
    cnt = int(input())
    num_lst = list(map(int, input().split()))
    print('#{} {}'.format(test_case, max(num_lst) - min(num_lst)))