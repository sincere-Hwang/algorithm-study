T = int(input())
for case in range(1, T+1):
    N = int(input())
    str_N = input()  # 인자값 문자열로 받음

    N_list = [0] * 10  # 변수 초기화
    index = 0
    max = 0

    for i in str_N:  # 문자열로 받은 숫자들 인덱스 받아서 증가
        N_list[int(i)] += 1

    for i in range(10):  # 지정한 맥스값보다 크거나 같으면 맥스 인덱스와 값 반환
        if N_list[i] >= max:
            max = N_list[i]
            index = i

    print(f'#{case} {index} {max}')
