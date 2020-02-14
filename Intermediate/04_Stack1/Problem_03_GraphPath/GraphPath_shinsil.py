import sys
sys.stdin = open('그래프 경로_input.txt')

'''
        DFS(v)
    v 방문 
    visited[v] <- true
    do{
        if (v의 인접 정점중 방문 안한 w 찾기 )
        push(v)
        while(w){
            w방문
            visited[w] <- True
            push(w)
            v <- w
            v의 인접 정점중 방문 안 한 w 찾기

        }
        v <- pop(stack)

    }while(v)
    end DFS()     
'''

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    node = {}
    visited = []
    for i in range(E):
        tail, head = map(int, input().split())
        node[(tail - 1, head - 1)] = True

    for i in range(0, V):
        visited.append(False)

    S, G = map(int, input().split())
    stack = []
    v = S - 1
    w = v

    result = 0
    cnt = 0

    while 1:
        v = w
        visited[v] = True
        cnt += 1

        for h in range(V):
            if node.get((v, h)) == True and visited[h] != True:
                stack.append(v)
                w = h

                break
        else:
            if stack:
                w = stack.pop()
            else:
                break

        if v == G - 1:
            result = 1
            break

    print('#{} {}'.format(test_case, result))
