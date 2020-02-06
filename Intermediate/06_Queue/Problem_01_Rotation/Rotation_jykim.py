T = int(input())

for tc in range(1, T+1) : 
    N, M = map(int, input().split())
    
    array = list(map(int, input().split()))
    
    for i in range(M) : 
        num = array.pop(0)
        array.append(num)
        
    print("#{} {}".format(tc, array[0]))
