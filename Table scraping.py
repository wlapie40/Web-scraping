import bs4 as bs
import urllib.request
import pandas as pd

html_code = urllib.request.urlopen('http://www.xe.com/currencyconverter/').read()
soup = bs.BeautifulSoup(html_code, 'lxml')
table = soup.find('table')
table_rows = table.find_all('tr')

# print(table_rows)
# for tr in table_rows:
#     print(tr.find_all('td'))

for tr in table_rows:
    td = tr.find_all('td')
    row = [(i.text).strip() for i in td]
    print(row)


#  Pandas version
dfs = pd.read_html('http://www.xe.com/currencyconverter/')

for df in dfs:
    print(df)