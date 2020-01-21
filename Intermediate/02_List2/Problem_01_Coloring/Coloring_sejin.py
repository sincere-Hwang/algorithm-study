T = int(input())

for test_case in range(1, T + 1):
    #palette = [[0] * 10] * 10 # 이렇게하면 Error~!! // palette[0]~palette[9]가 같은 객체로 생성
    # 팔레트 초기화 ( 0: 흰색, 1: 빨강, 2: 파랑, 3: 보라 )
    palette = [[0 for _ in range(10)] for _ in range(10)]  
    result = 0
    N = int(input())
    
    for i in range(N):
        #2 2 4 4 1
        r1, c1, r2, c2, color = map(int, input().split())
        
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if color == 1:  # 빨강 색칠
                    if palette[r][c] == 0:  # 흰->빨
                        palette[r][c] = 1
                    elif palette[r][c] == 2:  # 파->보
                        palette[r][c] = 3
                        result += 1
                else:  # 파랑 색칠
                    if palette[r][c] == 0:  # 흰->파
                        palette[r][c] = 2
                    elif palette[r][c] == 1:  # 빨->보
                        palette[r][c] = 3
                        result += 1
                    
    print('#{} {}'.format(test_case, result))