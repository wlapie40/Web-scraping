import bs4 as bs
import urllib.request


html_code = urllib.request.urlopen('https://www.washingtonpost.com/news-sitemap-index.xml').read()
soup = bs.BeautifulSoup(html_code, 'lxml')

http_list=[link.text for link in soup.find_all('loc')]
print(http_list)