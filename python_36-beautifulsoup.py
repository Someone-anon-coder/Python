# !pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())


url = "https://www.example.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
title = soup.title

print(title)
print(title.text)


url = "https://www.example.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

p_tag = soup.find('p')
links = soup.find_all('a')

print(p_tag)
print()

for link in links:
    print(link)
    print(link.get("href"))


url = "https://www.example.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
items = soup.select('.item-class')

for item in items:
    print(item.text)


url = "https://finance.yahoo.com/markets/commodities/" # Do not requests multiple times as it is a live functional website
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', attrs={"data-testid": "table-container"})

rows = table.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    print(cols)