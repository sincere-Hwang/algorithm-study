T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    lsls = []    #부분집합 하나하나를 임시저장 (조건 만족되면 lsls를 lslsls에 넣음)
    lslsls = []   #조건을 만족하는 집합을 저장하는 집합

    for i in range(1<<12):             
        for j in range(12):                
            if i&(1<<j):                     
                lsls.append(arr[j])
        if len(lsls) == N and sum(lsls) == K:
            lslsls.append(lsls)
        lsls = []

    print('#{} {}'.format(test_case, len(lslsls)))