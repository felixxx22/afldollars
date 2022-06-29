from afltablesscraper import *
import numpy as np

def average(player_data):
    sum = 0

    if len(player_data) > 1:
        for i in range(1, len(player_data)):
            sum += int(player_data[i])
        return sum / (len(player_data)-1)
    else:
        return 0

def fiveGameAverage(player_data):
    sum = 0

    if len(player_data) > 5:
        for i in range(len(player_data)-4, len(player_data)):
            sum += int(player_data[i])
        return sum / (len(player_data)-1)
    else:
        return 0


teams = ['adelaide', 'brisbanel','carlton', 'collingwood', 'essendon','fremantle', 'geelong', 'goldcoast', 'gws','hawthorn','melbourne','kangaroos','padelaide','richmond','stkilda','swans','westcoast','bullldogs']

for i in teams:
    data = scrape(i, '2022')
    for j in data:
        print(j[0])
        print(average(j))
        print(fiveGameAverage(j))
