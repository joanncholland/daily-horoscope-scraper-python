from bs4 import BeautifulSoup
import requests


URL = 'https://stardm.com/daily-horoscopes/A1-daily-horoscopes.asp'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

starSigns = soup.find_all('h4')
horoscopeText = soup.find_all('p')

horoscopeDict = {}

for i in range(0, 12):
    sign = starSigns[i].text.replace(" ", '')
    text = horoscopeText[i+4].text
    horoscopeDict.update({sign: text})

print(horoscopeDict.get('Sagittarius'))
