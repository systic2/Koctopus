from bs4 import BeautifulSoup
import requests
import pandas as pd

address = "http://sports.news.naver.com/basketball/schedule/index.nhn?data=20210224&month=02&year=2021&teamCode=&category=kbl"
request = requests.get(address)
html = request.text
soup = BeautifulSoup(html, 'html.parser')
soupData = [soup.findAll('div', {'class':'sch_tb'}), soup.findAll('div', {'class':'sch_tb2'})]

dataList = []

for data_tb in soupData:
    for data in data_tb:
        date_val = data.findAll('span',{'class':'td_date'})[0].text
        match_cnt = data.findAll('td')[0]['rowspan']
        if int(match_cnt) == 5:
            continue

        for i in range(0, int(match_cnt)):
            matchData = {}
            matchData['날짜'] = date_val
            matchData['시간'] = data.findAll('tr')[i].findAll('span',{'class':'td_hour'})[0].text
            matchData['홈팀'] = data.findAll('tr')[i].findAll('span', {'class': 'team_lft'})[0].text
            matchData['원정팀'] = data.findAll('tr')[i].findAll('span', {'class': 'team_rgt'})[0].text
            matchData['구장'] = data.findAll('tr')[i].findAll('span', {'class': 'td_stadium'})[0].text

            dataList.append(matchData)

df = pd.DataFrame(dataList)
print(df.head(3))