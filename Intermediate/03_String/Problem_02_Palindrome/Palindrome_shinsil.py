T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    ls = []                 #str을 담는 리스트
    Palindrome = ''         #회문을 저장하는 곳
    
    # 아이디어 1. 이차원 리스트를 만들어서 zip을 사용해 Trans (가로 slicing만 하면 됨)
    # 아이디어 2. 가로로 회문 탐색 세로로 회문 탐색 (내가 사용한 코드)
    #             -> 세로 Palindrome 에 저장해서 출력할 때 
    #                for문 대신 zip 사용 가능. 다음번에 적용해보기 
    # 다음번엔 다양한 방법으로 시도해보자. 

    for i in range(N):
        ls.append(input())
    
    for k in range(N):
        for i in range(N - M + 1):    #0부터 N-M까지 
            #가로로 회문 탐색
            for j in range(M//2):
                if ls[k][i+j] != ls[k][i+M-j-1]:
                    break
            else: 
                Palindrome = ls[k][i: i+M]
                break
            #세로로 회문 탐색
            for j in range(M//2):
                if ls[j+i][k] != ls[i+M-j-1][k]:
                    break
            else: 
                for l in range(M):
                    Palindrome += ls[l+i][k]
                break

    print('#{} {}'.format(test_case, Palindrome))