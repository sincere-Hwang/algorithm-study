T = int(input())


for time in range(1, T+1) :
    # N = 정수의 개수
    N = int(input())

    # 정수 리스트
    ai = list(map(int, input().split()))

    ans = []

    for i in range(N) :

        if i % 2 == 0 :
            max_value = ai.pop(ai.index(max(ai)))
            ans.append(max_value)

        else : # i % 2 == 1
            min_value = ai.pop(ai.index(min(ai)))
            ans.append(min_value)

    # print하기 위한 작업
    ans = list(map(str, ans[:10]))
    print('#{} {}'.format(time, ' '.join(ans)))


