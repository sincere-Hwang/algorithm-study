def Game(start_idx, end_idx):
    if start_idx == end_idx:  # 부전승
        return start_idx
    
    man1 = Game(start_idx, (start_idx+end_idx)//2)
    man2 = Game((start_idx+end_idx)//2+1, end_idx)
        
    # 가위바위보
    if (cards[man2] == 1 and cards[man1] == 3 or
        cards[man2] == 2 and cards[man1] == 1 or
        cards[man2] == 3 and cards[man1] == 2
    ): # 뒷사람이 이김
        return man2
    else: # 앞사람이 이김
        return man1
            
        
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, (('0 ' + input())).split()))  # card[0] 안씀
    print('#{} {}'.format(test_case, Game(1, N)))