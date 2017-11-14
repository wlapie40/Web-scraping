import bs4 as bs
import urllib.request
from pytube import YouTube

def html_parser(link):
    html_code = urllib.request.urlopen(link).read()
    soup = bs.BeautifulSoup(html_code,'lxml')
    www_list=['https://www.youtube.com'+link.get('href') for link in soup.find_all('a') if link.get('href')[:9]=='/watch?v=']
    return www_list

