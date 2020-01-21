T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))
    
    min_sum = max_sum = sum(num_lst[0 : M])  # 첫 부분집합을 최대/최소로 설정
    
    for i in range(N - M + 1):
        temp_sum = 0  # 부분합 초기화
        for j in range(M):  # 부분합 계산
            temp_sum += num_lst[i + j]
        
        #최대값 최소값 갱신
        if min_sum > temp_sum:
            min_sum = temp_sum
        if max_sum < temp_sum:
            max_sum = temp_sum
    
    print('#{} {}'.format(test_case, max_sum - min_sum))
