T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [i for i in map(int, input().split())] # 자연수 리스트
    for _ in range(M):
        lst.append(lst.pop(0)) # 회전
    print('#{} {}'.format(test_case, lst[0]))