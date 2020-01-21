T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    
    bus = 0  #버스 시작위치
    charge = 0  #충전횟수
    
    #bus_stop 초기화
    bus_stop = [0] * N
    #bus_stop 입력받기
    for i in map(int, input().split()):
        bus_stop[i] = 1
    
    while(bus + K < N):
        for j in range(K,-1,-1): #멀리서부터
            if j == 0:  #경우의 수가 없을 때
                charge = 0
                bus += N #탈출
            elif bus_stop[bus + j] == 1: #충전소 찾았을 때
                bus += j
                charge += 1
                break
                
    print('#{} {}'.format(test_case, charge))