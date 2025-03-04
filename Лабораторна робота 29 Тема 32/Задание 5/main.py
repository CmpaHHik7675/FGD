import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
title = soup.title.text if soup.title else "Заголовок не знайдено"
print("Заголовок сторінки:", title)
