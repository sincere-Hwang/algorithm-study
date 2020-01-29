T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = {}  # 딕셔너리
    for i in str1:
        result[i] = str2.count(i)
    print('#{} {}'.format(test_case, max(result.values())))