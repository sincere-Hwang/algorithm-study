T = int(input())
for i in range(T):
    N = int(input())
    tmp = int(input())
    a = []
    b = [0,0,0,0,0,0,0,0,0,0]                 #카운팅용 리스트

    for j in range(1,N+1):
        a.append(int(tmp%(10**j)/10**(j-1)))  #뒤집혀서 들어가지만 순서는 중요하지 않음                             
        
    a.sort()

    for j in range(N):
        b[a[j]] += 1

    idx_max = b[0]
    max_card = 0

    for j in range(10):
        if b[j] >= idx_max:
            max_card = j
            idx_max = b[j]

    print('#{} {} {}'.format(i+1,max_card,idx_max))
    