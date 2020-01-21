T = int(input())
for i in range(T):
    K, N, M = map(int, input().split())        #정수형 변수 3개 입력
    
    charger = input().split(' ')
    charger.append(str(N))
    bus = 0
    cnt = 0
    while bus < N:                                         #for 다 안돌고 중간에 넘어가는 방법 좀 알려주세요...
        for j in range(M):                                  #충전소 리스트를 돌면서
            if int(charger[j+1]) - int(charger[j]) > K:  #충전소간 거리가 K이상 떨어진 경우
                bus = N
                cnt = 0
                break
            elif (int(charger[j+1])-bus > K):      #충전소와 버스의 거리가 K보다 커지는 충전소를 찾아서
                bus = int(charger[j])-1             #그 직전 충전소로 이동
                cnt += 1                              #충전 했으니까 cnt 증가
                break

        bus +=1

    print('#%d %d'%(i+1,cnt))


