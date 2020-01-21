T = int(input()) # 1<= T <= 50


for i in range(1, T+1) :
    N = int(input()) # 5 <= N <= 1000
    # 1<= ai <= 1000000
    ai = list(map(int, input().split(' ')))
    ans = max(ai) - min(ai)
    print("#{0} {1}".format(i, ans))




