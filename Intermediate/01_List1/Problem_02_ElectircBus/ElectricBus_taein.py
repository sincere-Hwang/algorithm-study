T = int(input())
for case in range(1, T+1):
    K, N, M = map(int, input().split())  # K 이동할 수 있는 거리, N 총 정류장수, M 충전소 갯수
    M_list = map(int, input().split())

    station = [0] * (N+1)  # 변수 초기화
    position = 0
    charge = 0

    for i in M_list:  # 정류하는 station 값 할당
        station[i] = 1

    while position + K < N:  # 못풀어서 세진님 코드 참조한 부분
        for j in range(K, -1, -1):  # 받은 K인자 최대부터 역으로 사용하는 range 코드 사용
            if j == 0:
                charge = 0
                position = N
            elif station[position + j] == 1:  # station의 인덱스에 포지션을 더하는 코드 활용
                charge += 1
                position += j
                break

    print(f'#{case} {charge}')
