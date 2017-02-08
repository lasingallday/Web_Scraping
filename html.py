# import urlllib2
import requests
import pandas as pd
from bs4 import BeautifulSoup

# url = 'http://nbviewer.ipython.org/github/chrisalbon/code_py/blob/master/beautiful_soup_scrape_table.ipynb'
url = 'http://stats.nba.com/'

# Scrape the HTML at the url
r = requests.get(url)

# Turn the HTML into a Beautiful Soup object
soup = BeautifulSoup(r.text, 'lxml')

print soup