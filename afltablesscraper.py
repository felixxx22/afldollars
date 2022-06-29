import requests
from bs4 import BeautifulSoup

def scrape(team, year):
    URL = "https://afltables.com/afl/stats/teams/{}/{}_gbg.html".format(team, year)

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    data = []
    table = soup.find('table', attrs={'class':'sortable'})

    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values

    return data

print(scrape('geelong', '2022'))
