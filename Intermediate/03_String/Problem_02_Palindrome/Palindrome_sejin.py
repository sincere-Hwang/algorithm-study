T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    result = []
    
    #테이블 입력
    str_table = []
    for _ in range(N):
        str_table.append(input())
        
    #가로줄 탐색
    for r in range(N):
        for c in range(N - M + 1):
            # 슬라이싱 활용한 회문검출
            if str_table[r][c : c + M] == str_table[r][c : c + M][ : : -1]:
                result.append(str_table[r][c : c + M])
    
    #세로줄 탐색
    for r in range(N - M + 1):
        for c in range(N):
            col_lst = []  # 세로줄
            for i in range(M):  # 세로줄 입력
                col_lst.append(str_table[r+i][c])
            if col_lst == col_lst[ : : -1]:  # 세로줄이 회문이면
                result.append(''.join(col_lst))
                
    print('#{} {}'.format(test_case, result[0]))