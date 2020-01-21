nums = [i for i in range(1,13)]  # 1~12 리스트

# 부분집합 리스트 구하기
lst = [] 
for i in range(1 << len(nums)):  # 경우의 수 :  2^len(nums)
    sub_lst = []  # 부분집합
    for j in range(len(nums)):
        if i & (1 << j):  # 부분집합 만들기
            sub_lst.append(nums[j])
    lst.append(sub_lst)  # 리스트에 부분집합 추가
    
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0
    
    for m in lst:  # 모든 부분집합 중
        if len(m) == N and sum(m) == K:  # 길이 N, 합 K 일 때
            result += 1
    
    print('#{} {}'.format(test_case, result))