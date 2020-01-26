# find_palindrome : 회문을 찾는 함수
def find_palindrome(N, M, input_data):
    test_string = "" # 회문이면 정답으로 반환, 아니면 다른 문자들 반환예정
    ans_index = 0 # ans_index = 0 : 배열 뒤집어서 다시 함수 call, ans_index = 1 : 답 반환, 다음단계로 안넘어감
    for i in range(N):
        for j in range(N - M + 1):
            if input_data[i][j] == input_data[i][j + M - 1]:

                test_string = input_data[i][j:j + M]

                if test_string == test_string[::-1]:
                    ans_index = 1
                    break;

        if ans_index == 1: break;
    return (test_string, ans_index)


T = int(input())
for time in range(1, T+1) :
# --- 입력 단계 ---------------------------------------------------------------------------------

    # N : NxN 문자 배열
    # M : 회문 길이
    N, M = map(int, input().split())

    input_data = [] #입력 문자값들(2차원 배열)
    for j in range(N):
        temp = input() #temp : 문자 한줄
        input_data.append(temp)

#--- 회문 여부 확인 ------------------------------------------------------------------------------

    # ans_index = 0 : 배열 뒤집어서 다시 함수 call, ans_index = 1 : 답 반환, 다음단계로 안넘어감
    ans, ans_index = find_palindrome(N, M, input_data)

    if ans_index == 0: #만약 윗단계에서 회문인 문자가 없다면
        # input_data 뒤집기
        column_list = list(map(list, zip(*input_data))) #인터넷 보고 참고 *이 뭔가요
        ans, ans_index = find_palindrome(N, M, column_list) #뒤집은 리스트에서 회문 찾기
        ans = ''.join(ans) # 뒤집을때 리스트 형식(['a', 'b'])으로 나눠져서 합치는 과정

    print("#{} {}".format(time, ans))
