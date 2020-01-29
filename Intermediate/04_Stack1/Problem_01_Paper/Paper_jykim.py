def Paper(x):
    if x == 0 :
        return 1
    elif x < 0 :
        return 0
    return Paper(x-10) + Paper(x-20) *2


T = int(input())

for time in range(1, T+1) :
    N = int(input())

    ans = Paper(N)

    print("#{} {}".format(time, ans))    


