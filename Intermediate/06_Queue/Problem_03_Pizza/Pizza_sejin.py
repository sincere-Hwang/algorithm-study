def NewPizza():
    if Pizza:
        return Pizza.pop(0)
    else:
        return None

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    
    # 대기중인 피자
    Pizza = [[i, C[i-1]] for i in range(1, 1 + M)]
    
    # 오븐
    #Oven = [None for _ in range(N)] # 빈 오븐부터 시작
    Oven = [Pizza.pop(0) for _ in range(N)] # 피자 채우고 시작
    
    # 피자랑 오븐이 비면 종료
    while Pizza or Oven.count(None) < N:
        plate = Oven.pop(0)
        if plate == None: # 빈 플레이트면 피자 채움
            Oven.append(NewPizza())
        else:
            plate[1] //= 2 # 치즈 녹음
            if plate[1] == 0: # 치즈가 다 녹으면 서빙 후 피자 채움
                serving = plate[0]
                Oven.append(NewPizza())
            else: # 치즈 안녹으면
                Oven.append(plate)  # 다시 넣음
        #print(Oven, plate) # 중간 과정 확인

    print('#{} {}'.format(test_case, serving))