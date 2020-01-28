T = int(input())

for test_case in range(1, T + 1):
    str2 = list(input())
    str1 = list(input())
    n1 = len(str1)
    n2 = len(str2) - 1   #str2의 마지막 idx

    check = 0
    i = n2

    while i in range(n2, n1):
        if str1[i] != str2[n2] and str1[i] not in str2:
            i += (n2)
        elif str1[i] != str2[n2] and str1[i] in str2:
            for j in range(n2, -1,-1):
                if str1[i] == str2[j]:
                    i += (n2 - j)
                    break
        elif str1[i] == str2[n2]:
            for j in range(n2, -1,-1):
                if str1[i] != str2[j]:
                    break
                i -= 1
            else:
                check = 1
                break

    print('#{} {}'.format(test_case, check))