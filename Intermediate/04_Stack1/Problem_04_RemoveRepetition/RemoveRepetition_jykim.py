T = int(input())
# 전체적으로 bracket 문제와 비슷한 알고리즘
for time in range(1, T+1) :
    input_str = input()

    sample_list = []
    for ch in input_str :
        if sample_list == [] :
            sample_list.append(ch)

        else :
            if sample_list[-1] == ch :
                sample_list.pop()
            else :
                sample_list.append(ch)

    ans = len(sample_list)

    print("#{} {}".format(time, ans))


