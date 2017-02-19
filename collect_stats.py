from nba_py import game, team
import pandas as pd
import numpy as np

# Constants
game_id = '0021600849'
tID = '1610612738'

bs = game.Boxscore(game_id=game_id, season='2016-17', season_type='Regular Season', range_type='0', start_period='0', end_period='0', start_range='0', end_range='0')
df_total = bs.player_stats()
df_total = df_total[df_total['TEAM_CITY']=='Boston'.encode('utf-8')]
df_total.fillna(value=0)
# bsA = game.BoxscoreAdvanced(game_id=game_id, season='2016-17', season_type='Regular Season', range_type='0', start_period='0', end_period='0', start_range='0', end_range='0')
# print bsA.sql_players_advanced()

noGames = 5
for x in range(0,noGames+1):
	bs = game.Boxscore(game_id=game_id, season='2016-17', season_type='Regular Season', range_type='0', start_period='0', end_period='0', start_range='0', end_range='0')
	df = bs.player_stats()
	df = df[df['TEAM_CITY']=='Boston'.encode('utf-8')]
	df.fillna(value=0)
	oreb_gameRange = pd.concat([df_total,df]).groupby(['PLAYER_NAME'], as_index=False)['OREB'].sum()


# tDetails = team.TeamDetails(tID)
# tSeasons = team.TeamSeasons(tID, league_id='00', season_type='Regular Season', per_mode='PerGame')
# print tDetails.awards_championships()
# print tSeasons.info()

print oreb_gameRange