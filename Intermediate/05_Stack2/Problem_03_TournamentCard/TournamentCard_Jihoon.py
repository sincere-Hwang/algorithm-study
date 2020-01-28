def cmp(front, end):
    if(card_N[front-1] == 1 and card_N[end-1] == 2):
        return end
    elif(card_N[front-1] == 2 and card_N[end-1] == 3):
        return end
    elif(card_N[front-1] == 3 and card_N[end-1] == 1):
        return end
    else:
        return front

def game_group(st, ed):
    if(st == ed):
        return st

    mid = (st + ed) // 2
    front_group = game_group(st, mid)
    end_group = game_group(mid+1, ed)
    return cmp(front_group, end_group)


TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    card_N = list(map(int, input().split()))
    result = game_group(1,N)
    print('#{} {}'.format(test_case, result))