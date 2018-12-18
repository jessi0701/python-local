import requests
from bs4 import BeautifulSoup

url = "http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')
song = soup.select('table.dtable.clr tbody tr')

for songs in song :
    print(songs.select_one('td:nth-of-type(1) a').text,end=" ")
    print(songs.select_one('td:nth-of-type(2)').text)
    
