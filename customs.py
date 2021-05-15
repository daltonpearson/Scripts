from random import shuffle
import json
do_roles = True

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
team_1, team_2 = (players[:5], players[5:]) if not do_roles else (dict(list(zip(roles, players[:5]))), dict(list(zip(roles, players[5:]))))

print(f'Team 1: {json.dumps(team_1)}\nTeam 2: {json.dumps(team_2)}')
