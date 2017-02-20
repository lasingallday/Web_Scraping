# import urlllib2
import requests
import pandas as pd
from bs4 import BeautifulSoup

-----------------------------------------------------------
for _get_json/self.json/json_inp,
self._endpoint = self.'boxscoretraditionalv2'
params={'GameID': game_id,
		'Season': season,
		'SeasonType': season_type,
		'RangeType': range_type,
		'StartPeriod': start_period,
		'EndPeriod': end_period,
		'StartRange': start_range,
		'EndRange': end_range}

for player_stats function, _api_scrape(self.json, 0/1/2)
-----------------------------------------------------------
in _api_scrape,
headers = json_inp['resultSets'][ndx]['headers']
values = json_inp['resultSets'][ndx]['rowSet']
get, DataFrame(values, columns=headers)
-----------------------------------------------------------

# url = 'http://nbviewer.ipython.org/github/chrisalbon/code_py/blob/master/beautiful_soup_scrape_table.ipynb'
url = 'http://stats.nba.com/'

# Scrape the HTML at the url
r = requests.get(url)

# Turn the HTML into a Beautiful Soup object
soup = BeautifulSoup(r.text, 'lxml')

print soup