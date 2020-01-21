T = int(input())

for i in range(1, T+1):
    N = int(input())
    llist = list(map(int, input().split()))
    special_sort = [0] * 10
    for j in range(5):
        special_sort[2 * j] = max(llist)
        llist.remove(max(llist))


    for j in range(1, 6):
        special_sort[2 * j - 1] = min(llist)
        llist.remove(min(llist))


    print("#{} ".format(i), end='')

    for j in range(len(special_sort)):
        if(j < len(special_sort) - 1):
            print('{} '.format(special_sort[j]), end='')
        else:
            print('{}'.format(special_sort[j]))

