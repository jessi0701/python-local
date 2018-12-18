import requests
from bs4 import BeautifulSoup

url = "https://music.bugs.co.kr/chart"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')
song = soup.select('table.list.trackList.byChart tbody tr')
for songs in song :
    print(songs.select_one('th:nth-of-type(1) p a').text)
    print(songs.select_one('td:nth-of-type(5) p a').text)
    
