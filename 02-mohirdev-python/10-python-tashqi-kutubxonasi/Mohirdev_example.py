import requests
from bs4 import BeautifulSoup


sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
# pprint(r.text)

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())
news = soup.find_all(class_="small-cards__default-text")
print(news[0].text)
# print(len(news))

# import requests
# from bs4 import BeautifulSoup

# sahifa = 'https://kun.uz/news/main'
# r = requests.get(sahifa)

# # Sahifaning HTML kodini go'zallashtirilgan formatda chiqarish
# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
