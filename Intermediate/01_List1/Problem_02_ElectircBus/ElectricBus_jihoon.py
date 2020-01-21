

T = int(input())

for i in range(1, T+1):
    K, N, M = map(int, input().split())
    stationNum = list(map(int, input().split()))
    chargeStation = [0] * (N + 1)
    for j in stationNum:
        chargeStation[j] = 1

    # print(chargeStation)
    st, x, cnt = 0, K, 0  

    while (st < N):
        if((st+x) >= N ):  
            break
        elif(chargeStation[st+x] == 1): 
            cnt +=1
            st += x
            x = K
        else:
            x -= 1     
            if(x == 0):
                cnt =0   
                break
    print('#{} {}'.format(i, cnt))

