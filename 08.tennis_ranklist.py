import math

num_tournament = int(input())
start_num_point_leaderboard = int(input())

tournament_w = 2000
tournament_f = 1200
tournament_sf = 720

result = 0
tournament = start_num_point_leaderboard
total_result = 0
counter_won_tournament = 0
percent_won_tournament = 0

for i in range(1, num_tournament+1):
    reach_tournament_stage = input()
    if reach_tournament_stage == "F":
        result = tournament + tournament_f
        total_result += tournament_f
        tournament = result
        result = 0
    elif reach_tournament_stage == "SF":
        result = tournament + tournament_sf
        total_result += tournament_sf
        tournament = result
        result = 0
    else:
        result = tournament + tournament_w
        counter_won_tournament += 1
        total_result += tournament_w
        tournament = result
        result = 0

percent_won_tournament = (counter_won_tournament/num_tournament) * 100

print(f"Final points: {tournament}")
print(f"Average points: {math.floor(total_result/num_tournament)}")
print(f"{percent_won_tournament: .2f}%")
