def game(A, cntA, first_page, last_page, central_page) :
    for i in range(1000):
        if A > central_page:
            first_page = central_page
            central_page = int((first_page + last_page) / 2)
            cntA += 1
        elif A < central_page:
            last_page = central_page
            central_page = int((first_page + last_page) / 2)
            cntA += 1
        else:
            return(cntA)
            break;

T = int(input())

for time in range(1, T+1) :
    P, A, B = map(int, input().split())
    [Pa, Pb] = [A, B]


    first_page = 1
    last_page = P
    central_page = int((first_page + last_page) / 2)
    cntA, cntB = 0, 0

    ansA = game(A, cntA, first_page, last_page, central_page)
    ansB = game(B, cntB, first_page, last_page, central_page)

    if ansA < ansB :
        ans = 'A'
    elif ansA > ansB :
        ans = 'B'
    else :
        ans = 0

    print("#{} {}".format(time, ans))




