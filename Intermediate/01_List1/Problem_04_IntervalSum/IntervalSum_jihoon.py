T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    intNum = list(map(int, input().split()))
    mymax, mymin = 0, 987654321

    for j in range(0, N-M+1):

        mysum = 0
        for k in range(0, M):
            mysum += intNum[j + k]
        # print(mysum)

        if(mysum > mymax):
            mymax = mysum
        if(mysum < mymin):
            mymin = mysum

    result = mymax - mymin
    print("#{} {}".format(i, result))