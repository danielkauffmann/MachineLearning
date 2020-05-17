import pandas as pd
from bs4 import BeautifulSoup
import re

# link = 'https://steamcommunity.com/id/sp1nalcord/gcpd/730?tab=matchhistorycompetitive'
# url = requests.get(link)
# soup = BeautifulSoup(url.content, 'html.parser')

ls_all = []
ls_player = []
ls_score = []
ls_ping = []
ls_kill = []
ls_assist = []
ls_death = []
ls_mvp = []
ls_hsp = []
ls_match_score = []
ls_score = []

with open('data/CSGO.html', encoding='utf8') as file:
    soup = BeautifulSoup(file, 'html.parser')
    table_ = soup.find(class_='generic_kv_table csgo_scoreboard_root')
    table = table_.find_all(class_='csgo_scoreboard_inner_right banchecker-formatted')
    for i in range(0, 2):
        print(i)
        for row in table[i].find_all('td'):
            if row.find('a'):
                # print(row.get_text())
                name = row.get_text().strip()
                #if re.match(r'^\w+$', name):
                ls_player.append(name)
                # else:
                #     ls_player.append('-')
            elif "colspan" in row.attrs:
                # print(row.get_text())
                ls_match_score.append(row.get_text().strip())
            else:
                # print(row.get_text())
                ls_all.append(row.get_text().strip())
# print(soup)
# print(ls_all)
for i in range(0, len(ls_all), 7):
    ls_ping.append(ls_all[i])
    ls_kill.append(ls_all[i + 1])
    ls_assist.append(ls_all[i + 2])
    ls_death.append(ls_all[i + 3])
    ls_all[i+4] = ls_all[i+4].replace('★', '')
    ls_mvp.append(ls_all[i + 4])
    ls_hsp.append(ls_all[i + 5])
    ls_score.append(ls_all[i + 6])

# print(len(ls_ping))
# print(len(ls_kill))
# print(len(ls_assist))
# print(len(ls_death))
# print(len(ls_mvp))
# print(len(ls_hsp))
# print(len(ls_score))

df = pd.DataFrame()
df['Player Name'] = ls_player
df['Ping'] = ls_ping
df['Kills'] = ls_kill
df['Assists'] = ls_assist
df['Deaths'] = ls_death
df['MVP'] = ls_mvp
df['HSP'] = ls_hsp
df['Score'] = ls_score
df = df.replace(r'^\s*$', 0, regex=True)
print(df)
df.to_csv('CSGO_Data.csv')
