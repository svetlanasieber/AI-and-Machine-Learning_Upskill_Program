from math import floor
tournament_count = int(input())
starting_points = int(input())
total_points = 0
percentage_wins = 0
for _ in range(tournament_count):
    finish = input()
    if finish == 'W':
        total_points += 2000
        percentage_wins += (len(finish) / tournament_count) * 100
    elif finish == 'F':
        total_points += 1200
    elif finish == 'SF':
        total_points += 720
final_points = total_points + starting_points
print(f'Final points: {final_points}')
print(f'Average points: {floor(total_points / tournament_count)}')
print(f"{percentage_wins:.2f}%")
