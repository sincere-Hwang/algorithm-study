T = int(input())

for i in range(T):
    cardNumber = int(input())
    N = list(map(int, input()))
    mymax = N.count(N[0])
    x = 0

    for j in range(1, len(N)):
        if(N.count(N[j]) == mymax):
            mymax = N.count(N[j])
            x = max(x, N[j])
        elif(N.count(N[j]) >  mymax):
            mymax = N.count(N[j])
            x = N[j]


    print("#{} {} {}".format(i+1, x, mymax))