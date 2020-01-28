TC = int(input())

for i in range(1, TC+1):
    str1 = set(input())
    str_1 = list(str1)
    str2 = list(input())
    max = 0
    for k in range(len(str1)):
        for j in str_1[k]:
            cnt = str2.count(j)
            if(cnt >= max):
                max = cnt


    print("#{} {}".format(i, max))

