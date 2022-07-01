import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape(team, year):
    URL = "https://afltables.com/afl/stats/teams/{}/{}_gbg.html".format(team, year)

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    data = []
    headers = []
    table = soup.find('table', attrs={'class':'sortable'})

    table_head = table.find('thead')
    rows = table_head.find_all('tr')
    for row in rows:
        cols = row.find_all('th')
        cols = [ele.text.strip() for ele in cols]
        cols.pop()
        # removes overall header
        if len(cols) > 1:
            headers.append(cols)


    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        cols.pop()
        # data.append([ele for ele in cols if ele != '-' and ele])# Get rid of empty values
        data.append([x if x != '' and x != '-' else '0' for x in cols])

    table_collated = headers + data
    df = pd.DataFrame(table_collated[1:], columns=table_collated[0])
    df[headers[0][1:]] = df[headers[0][1:]].astype(int)

    return df
