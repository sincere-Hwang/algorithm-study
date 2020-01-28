T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    cnt_list = []
    
    for char in str1:
        cnt = 0
        for i in range(len(str2)):
            if char == str2[i]:
                cnt += 1
        cnt_list.append(cnt)

    print('#{} {}'.format(test_case, max(cnt_list)))
