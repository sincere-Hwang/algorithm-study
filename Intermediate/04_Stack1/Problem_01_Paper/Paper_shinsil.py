T = int(input())

def fact(N):
    return 1 if N == 0 else N*fact(N-1)
        
for test_case in range(1, T + 1):
    N = int(input())
    cnt = 0           #경우의 수 

    for n2 in range(N//20 + 1):     #20*20은 번호 2번 
        for n3 in range(N//20 + 1 - n2):     #10*20 두개 합친건 번호 3번
            n1 = (N-20*(n3+n2))//10          
            n = n1 + n2 + n3

            cnt += fact(n)//(fact(n1)*fact(n2)*fact(n3))  # 같은 것이 있는 순열 n!/(n1!*n2!*n3!)   
                                                          #0! == 1이므로 공식은 문제 없음
    print('#{} {}'.format(test_case, cnt))