A = list(range(1, 13)) # 1~12까지의 숫자를 원소로 가진 집합
T = int(input())
n = len(A) # 집합 리스트 A의 길이

for time in range(1, T + 1) :

    # 입력값
    # N = 부분집합 원소의 수
    # K = 부분 집합의 합
    N , K = map(int, input().split())

    # 부분집합 원소의 합이 가장 작을때 : 1~N을 부분집합의 원소로 가질때
    # 1에서 N까지의 합이 K보다 크면 조건을 만족하는 case 개수 = 0
    if sum(range(1, N+1)) > K :
        ans = 0

    # 1에서 N까지의 합이 K와 같으면 조건을 만족하는 case 개수 = 1
    elif sum(range(1, N+1)) == K :
        ans = 1

    # 그 외의 case에 대해 아래의 알고리즘을 통해 평가
    else :

        # 부분집합 구하는 알고리즘 - 비트연산자 활용
        check_list = []
        # 1~ 2^n까지 -> 부분집합 개수동안
        for i in range(1 << n):
            subset = [] # 부분집합 추가를 위한 임시리스트
            for j in range(n):

                    # i $ 2^j >= 1이면 (ex 3(11) & 1(01) = 11(True))
                    if i & (1 << j):
                    	subset.append(A[j]) # 임시리스트에 원소 추가

            #임시리스트의 길이가 N과 같으면 부분집합 체크리스트에 추가
            if len(subset) == N :
                check_list.append(subset)

        #check list의 각 원소(부분집합)의 합을 저장
        for i in range(len(check_list)) :
            check_list[i] = sum(check_list[i])

        #부분집합의 합과 K의 일치 개수를 ans에 저장
        ans = check_list.count(K)

    print('#{} {}'.format(time, ans))
