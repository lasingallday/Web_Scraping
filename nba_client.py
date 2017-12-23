import urllib.request
from bs4 import BeautifulSoup as BS
from selenium import webdriver
import re
import string
import os


MONTH_ID = '2'
URL = 'http://stats.nba.com/schedule/#!?Month=' + MONTH_ID + '&PD=N'
url_gamemonth = r"/Users/jif/Downloads/NBA.com_Stats _ League Schedule.htm"
# save_path = os.path.expanduser('~/Miscellaneous/')
game_ids = []

# Time can be set to gameday or gamemonth.
# If printing for time = gamemonth, save file as a file_gamemonth.txt.
def get_htmls_info(time = 'gamemonth', url_gameday = r'/Users/jif/Downloads/NBA.com_Stats _ League Scoreboard By Day.htm'):
    # This reduces the file size by a factor of 10.
    if (time=='gamemonth'):
        page = open(url_gamemonth)
        soup = BS(page.read(),"lxml")
        tree = soup.find_all('a')
    elif (time=='gameday'):
        page = open(url_gameday)
        soup = BS(page.read(),"lxml")
        tree = soup.find_all('script')
    return tree

# when storing game_id, I also need to store team, and maintain the order.
def get_days_gameids(time = 'gamemonth', file_gameday = r'/Users/jif/Miscellaneous/SpecificMonth_gamedays/11_24_2017_index.html_gameday.txt'):
    # file_gameday = 'file_' + time + '.txt'
    save_path = os.path.expanduser('~/Miscellaneous/')
    dates = []
    specificMonth_gamedays_list = []

    with open(file_gameday,'r') as ins:
        for line in ins:
            if (time=='gamemonth'):
                temp_time = re.findall('scores/11/\d\d/2017', line)
            elif (time=='gameday'):
                temp_time = re.findall('"GAME_ID":"\d\d\d\d\d\d\d\d\d\d"', line)
                temp_hometeam = re.findall('"HOME_TEAM_ID":\d\d\d\d\d\d\d\d\d\d', line)
                temp_visitingteam = re.findall('"VISITOR_TEAM_ID":\d\d\d\d\d\d\d\d\d\d', line)
            if temp_time:
                if (time=='gamemonth'):
                    dates.append(temp_time)
                elif (time=='gameday'):
                    game_ids.append(temp_time)
                    return game_ids
                # print(temp_time)
            if temp_hometeam:
                if (time=='gameday'):
                    # I have to be sure to store the correct game_id, home_team_id, and visitor_team_id triples
        # This removes the leading and trailing brackets.
        if (time=='gamemonth'):
            dates = ''.join(str(v) for v in dates)
            dates = dates.lstrip('[')
            dates = dates.rstrip(']')
            dates = dates.replace("'","")
            dates = dates.replace(" scores/","")
            dates = dates.replace("scores/","")
            dates = dates.split(",")
    # print(type(dates), dates)
    # print(type(game_ids), game_ids)

    if (time=='gamemonth'):
        for each in dates:
            webpage_filename = each + '_index.html'
            webpage_filename = webpage_filename.replace('/','_')
            specificMonth_gamedays_list.append(webpage_filename)
            complete_name = os.path.join(save_path, webpage_filename)
            file_object = open(complete_name, 'w')
            driver = webdriver.Chrome(executable_path=r"/Users/jif/chromedriver")
            driver.set_page_load_timeout(20)
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.get("http://stats.nba.com/scores/"+each)
            html = driver.page_source
            file_object.write(html)
            driver.close()
            return specificMonth_gamedays_list


# This reduces the gamemonth file size by a factor of 10.
# get_htmls_info(time='gamemonth')

# This produces all of the gameday htmls
# I should save this in a textfile. (and save the game_ids, with the two teams [HOME_TEAM_ID and VISITOR_TEAM_ID], in a DB--3 columns.)
# specificMonth_gamedays_list = get_days_gameids(time='gamemonth')
specificMonth_gamedays_list = ['11_01_2017_index.html','11_02_2017_index.html','11_03_2017_index.html','11_04_2017_index.html','11_05_2017_index.html','11_06_2017_index.html','11_07_2017_index.html','11_08_2017_index.html','11_09_2017_index.html','11_10_2017_index.html','11_11_2017_index.html','11_12_2017_index.html','11_13_2017_index.html','11_14_2017_index.html','11_15_2017_index.html','11_16_2017_index.html','11_17_2017_index.html','11_18_2017_index.html','11_19_2017_index.html','11_20_2017_index.html','11_21_2017_index.html','11_22_2017_index.html','11_24_2017_index.html','11_25_2017_index.html','11_26_2017_index.html','11_27_2017_index.html','11_28_2017_index.html','11_29_2017_index.html','11_30_2017_index.html']

# for day in specificMonth_gamedays_list:
#     save_path = os.path.expanduser('~/Miscellaneous/')
#     day_fullpath = os.path.join(save_path, day)
#     # print(day_fullpath)
#     mytree = get_htmls_info(time = 'gameday', url_gameday = day_fullpath)
#     gameday_filename = day + '_gameday.txt'
#     complete_name = os.path.join(save_path+'SpecificMonth_gamedays/', gameday_filename)
#     file_object = open(complete_name, 'w')
#     file_object.write(str(mytree))
#     file_object.close()

for day in specificMonth_gamedays_list:
    save_path = os.path.expanduser('~/Miscellaneous/SpecificMonth_gamedays/')

    gameday_filename = r'/Users/jif/Miscellaneous/SpecificMonth_gamedays/11_24_2017_index.html' + '_gameday.txt'
    day_fullpath = os.path.join(save_path, gameday_filename)
    print(day_fullpath)
    get_days_gameids(time='gameday', file_gameday = day_fullpath)
    print(game_ids)
    # game_ids = ''.join(str(v) for v in game_ids)
    # game_ids = game_ids.lstrip('[')
    # game_ids = game_ids.rstrip(']')
    # game_ids = game_ids.replace("'","")
    # game_ids = game_ids.replace(" scores/","")
    # game_ids = game_ids.replace("scores/","")
    # game_ids = game_ids.split(",")
