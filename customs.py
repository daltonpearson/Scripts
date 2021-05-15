from random import shuffle
import json

roles = [
    'Top',
    'Jun',
    'Mid',
    'Sup',
    'Bot',
]
players = [
    'Salty',
    'Cam',
    'Curt',
    'Dan',
    'Deric',
    'Nat',
    'Bryn',
    'Jamie',
    'Justin',
    'Graham',
]

shuffle(players)
team_1, team_2 = dict(list(zip(roles, players[:5]))), dict(list(zip(roles, players[5:])))

print('Team 1:')
[print(f'   - {player} ({role})') for role, player in team_1.items()]
print('\nTeam 2:')
[print(f'   - {player} ({role})') for role, player in team_2.items()]