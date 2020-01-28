TC = int(input())

for i in range(1, TC + 1):
    str1 = input()
    str2 = input()
    ex = False
    if (str1 in str2):
        ex = True

    if (ex):
        print("#{} 1".format(i))
    else:
        print("#{} 0".format(i))
