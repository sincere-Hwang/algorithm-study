T=int(input())

for i in range(T):
    N=int(input())
    a_str = input()
    
    a = a_str.split(' ')   #str -> list
    min = int(a[0])
    max = min

    for j in range(1,N):
        if int(a[j])<min:
            min = int(a[j])
        if int(a[j])>max:
            max = int(a[j])
    print ('#%d %d'%(i+1,max-min))
    #print('#{} {}'%(i,max-min))

