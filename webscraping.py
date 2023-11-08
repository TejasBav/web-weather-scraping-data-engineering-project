import requests
from bs4 import BeautifulSoup
import pandas as pd

weather_search_url = 'https://www.google.com/search?q=weather+mumbai'

headers_content = {'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

r = requests.get(weather_search_url, headers=headers_content) 

print(r.status_code)

# print(r.content)

soup = BeautifulSoup(r.content, 'html.parser') 

'''fidning temperature'''
temp = soup.find('span', attrs={'id': 'wob_tm'}).text
print(temp)

'''finding temperature unit'''
temp_unit = soup.find('div', attrs={'class': 'vk_bk wob-unit'}).find('span', attrs={'class': 'wob_t'}).text
print(temp_unit)

'''fidning sky'''
sky = soup.find('span', attrs={'id': 'wob_dc'}).text
print(sky)

'''fidning time'''
time = str(soup.find('div', attrs={'id': 'wob_dts'}).text)
print(time)

tempdf = pd.DataFrame([[temp,temp_unit,sky,time]], columns= ['Temperature', 'Unit', 'Sky', 'Time'])

print(tempdf)