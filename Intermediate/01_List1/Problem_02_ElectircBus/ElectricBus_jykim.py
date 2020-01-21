T = int(input())

    # K = 한번에 이동 가능한 정류장 개수
    # N = 정류장 개수
    # M = 충전소가 설치된 정류장 개수
for time in range(1, T+1) :

    K, N, M = map(int, input().split())
    charge_station = list(map(int, input().split())) 

    #0~N까지 충전소 체크
    charge_number = [0] * (N+1) #0~N까지 충전소 체크 list
    for station in charge_station :
        charge_number[station] += 1

    # 정차 횟수 찾기
    start = K; num = 0 #start : 정차할 정류장 // num = 정차 횟수
    while start < N :

        # 정차할 정류장 찾기
        for i in range(start, start-K, -1) : # ex>3, 2, 1 순으로 정차할 충전소가 있으면 정차횟수+1, 루프 break
            if charge_number[i] == 1 :
                start = i #정류장번호 = 충전소가 있는 정류장 번호
                num += 1
                break;

        if i == start-K+1 : #루프를 온전히 돌았을때엔 중간에 정차할 충전소가 없다고 판단 -> 정차횟수를 0으로 반환
            num = 0
            break;

        start += K 
    print("#{} {}".format(time, num))

