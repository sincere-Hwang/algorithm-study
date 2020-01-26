# T = time
T = int(input())

for time in range(1, T+1) :

    # str1 = comparing string
    str1 = input()
    # str2 = compared string
    str2 = input()
    
    ans = 0

    if str1 in str2 :
        ans = 1

    print("#{} {}".format(time, ans))


