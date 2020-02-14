import sys
sys.stdin = open('토너먼트 카드게임_input.txt')

T = int(input())

def game(a, b):        #idx를 입력으로 받음
    if arr[a] == 1:
        if arr[b] == 1 or arr[b] == 3:
            return a
        elif arr[b] == 2:
            return b
    elif arr[a] == 2:
        if arr[b] == 1 or arr[b] == 2:
            return a
        elif arr[b] == 3:
            return b
    else:
        if arr[b] == 2 or arr[b] == 3:
            return a
        elif arr[b] == 1:
            return b

def card_game(a):

    n = len(a)

    if n == 2:
        return game(a[0], a[1])
    elif n == 1:
        return a[0]
    else:
        n = n // 2 + (n % 2)
        return game(card_game(a[0:n]), card_game(a[n:]))

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    idx = [i for i in range(N)]
    print('#{} {}'.format(tc, card_game(idx) + 1))