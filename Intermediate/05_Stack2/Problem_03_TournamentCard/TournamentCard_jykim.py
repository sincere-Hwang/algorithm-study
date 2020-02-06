# 팀쪼개기
def teamsplit(teams) :

    team1 = teams[ : (len(teams)-1) // 2 + 1]
    team2 = teams[(len(teams)-1) // 2 + 1 : ]

    return team1, team2

# 승리자 판별
def victory(battle) :

    if len(battle) == 1:
        return battle.pop()

    else :

        per1, per2 = battle #per = person

        if per1[1] == per2[1] : return per1 # if same card

        # battle 1. per2 victory
        elif (per1[1] == 1 and per2[1] == 2) or (per1[1] == 2 and per2[1] == 3) or (per1[1] == 3 and per2[1]) == 1 :
            return per2

        # battle 2. per1 victory
        else : return per1


def tournament(teams) :

    # 한팀의 인원이 3명 이상이면 1명 또는 2명으로 쪼개기
    if len(teams) >= 3 :
        team1, team2 = teamsplit(teams)
        vic1 = tournament(team1)
        vic2 = tournament(team2)

        # 승리자들끼리 새로운 팀으로 묶기
        new_team = [vic1, vic2]
        return victory(new_team)
    else :
        return victory(teams)


T = int(input()) + 1

for tc in range(1, T) : 

    N = int(input())
    persons = list(map(int, input().split()))
    teams = [(index, card) for index, card in enumerate(persons)]
    # print(team)
    
    ans = tournament(teams)[0] + 1
    print("#{} {}".format(tc, ans))
