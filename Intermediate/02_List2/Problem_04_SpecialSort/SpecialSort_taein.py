T = int(input())

for case in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    i = 0

    while i < len(a):
        if i % 2 != 0:
            min_num = i
            for j in range(i+1, len(a)):
                if a[min_num] > a[j]:
                    min_num = j
            a[i], a[min_num] = a[min_num], a[i]
        else:
            max_num = i
            for j in range(i+1, len(a)):
                if a[max_num] < a[j]:
                    max_num = j
            a[i], a[max_num] = a[max_num], a[i]
        i += 1

    result = f"#{case} "
    for st in a[:10]:
        result += str(st) + " "
    print(result)
