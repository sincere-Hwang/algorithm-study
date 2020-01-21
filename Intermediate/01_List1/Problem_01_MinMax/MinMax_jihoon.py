T = int(input())

for i in range(1, T+1):

    N = int(input())
    num = list(map(int, input().split()))
    result = max(num) - min(num)
    print("#{} {}".format(i, result))