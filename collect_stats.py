from nba_py import game, team
import pandas as pd
import numpy as np

# Constants
game_id = '0021600849'
tID = '1610612738'

bs = game.Boxscore(game_id=game_id, season='2016-17', season_type='Regular Season', range_type='0', start_period='0', end_period='0', start_range='0', end_range='0')
print bs.player_stats()
# bsA = game.BoxscoreAdvanced(game_id=game_id, season='2016-17', season_type='Regular Season', range_type='0', start_period='0', end_period='0', start_range='0', end_range='0')
# print bsA.sql_players_advanced()

# tDetails = team.TeamDetails(tID)
# tSeasons = team.TeamSeasons(tID, league_id='00', season_type='Regular Season', per_mode='PerGame')
# print tDetails.awards_championships()
# print tSeasons.info()

columns = ['A','B']
df = pd.DataFrame(index=range(0,4), columns = columns)
df = df.fillna(0)
print df