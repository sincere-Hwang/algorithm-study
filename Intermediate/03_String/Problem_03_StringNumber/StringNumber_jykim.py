T = int(input())

for time in range(1, T+1) : 
    str1 = input()
    str2 = input()
    
    ans_dict = {}
    for i in str1 :
        ans_dict[i] = str2.count(i)
    
    ans = max(ans_dict.values())
    print("#{} {}".format(time, ans))
