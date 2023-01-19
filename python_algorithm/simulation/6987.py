# 월드컴 풀이
import sys

# back_tracking 통한 해결
def is_possible(possibles, my_team, enemy_team, match_count):
    possible = False
    # match_count 가 15 번째 라면 모든 매칭을 해본 것이 됨
    if match_count == 15:
        return True
    # my_team 이 이기는 경우
    if possibles[0][my_team] > 0 and possibles[2][enemy_team] > 0:
        # 매칭의 결과를 반영 후
        possibles[0][my_team] -= 1
        possibles[2][enemy_team] -= 1
        # my_team 이 붙을 수 있는 모든 상대와 붙지 않은 경우 다음 팀과 붙음
        if enemy_team + 1 < 6:
            possible = is_possible(possibles, my_team, enemy_team + 1, match_count + 1)
        # my_team 이 붙을 수 있는 모든 상대와 붙지 않은 경우 다음 팀과 붙음
        else:
            possible = is_possible(possibles, my_team + 1, my_team + 2, match_count + 1)
        # 매칭의 결과를 미반영 상태로 돌림
        possibles[0][my_team] += 1
        possibles[2][enemy_team] += 1
    # 모든 게임을 다 매칭 해본 경우 True 를 반환하고 끝냄
    if possible:
        return True
    # my_team 비기는 경우
    if possibles[1][my_team] > 0 and possibles[1][enemy_team] > 0:
        possibles[1][my_team] -= 1
        possibles[1][enemy_team] -= 1
        if enemy_team + 1 < 6:
            possible = is_possible(possibles, my_team, enemy_team + 1, match_count + 1)
        else:
            possible = is_possible(possibles, my_team + 1, my_team + 2, match_count + 1)
        possibles[1][my_team] += 1
        possibles[1][enemy_team] += 1

    if possible:
        return True

    # my_team 이 지는 경우
    if possibles[2][my_team] > 0 and possibles[0][enemy_team] > 0:
        possibles[2][my_team] -= 1
        possibles[0][enemy_team] -= 1
        if enemy_team + 1 < 6:
            possible = is_possible(possibles, my_team, enemy_team + 1, match_count + 1)
        else:
            possible = is_possible(possibles, my_team + 1, my_team + 2, match_count + 1)
        possibles[2][my_team] += 1
        possibles[0][enemy_team] += 1

    if possible:
        return True

# solution
def is_solution():
    # 총 게임 결과를 6번 받음
    results = list(map(int, sys.stdin.readline().split()))
    team = [[0] * 6 for _ in range(3)]
    # team[0][team구분]:승리, team[1][team구분]:무승부, team[2][team구분]: 패배
    for i in range(0, 18, 3):
        if sum(results[i:i + 3]) != 5:
            print(0)
            return
        team[0][i // 3] = results[i]
        team[1][i // 3] = results[i + 1]
        team[2][i // 3] = results[i + 2]
    # 가능한지 판단하는 백트래킹 사용
    if is_possible(team, 0, 1, 0):
        print(1)
    else:
        print(0)


# 4번을 입력 받음
for _ in range(4):
    is_solution()
