import requests
from bs4 import BeautifulSoup
import time

# Функция для парсинга страницы
HEADERS = {
    'HEADERS'
}
cookies = {
    'cookies'
    }

url = 'https://poshmark.com/category/Women'
response = requests.get(url, headers=HEADERS, cookies=cookies)
items = BeautifulSoup(response.text, "html.parser").find_all("div", class_="card card--small tile")

for item in items:
    try:

        link = "https://poshmark.com" + item.find("a")["href"]
        soup = BeautifulSoup(requests.get(link, headers=HEADERS, cookies=cookies).text, "html.parser")
        title = soup.find("h1", class_="fw--light m--r--2 listing__title-container").text.strip()
        price = soup.find("p", class_="h1").contents[0].strip()

        print(title, price, sep="\n", end="\n" + "-" * 30 + "\n")
    except:
        pass
    time.sleep(1)