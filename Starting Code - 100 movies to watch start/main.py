import requests
from bs4 import BeautifulSoup
from requests.models import parse_url

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
res = requests.get(url=URL)

soup = BeautifulSoup(res.text,"html.parser")


titles_and_ranks = soup.select(".article-title-description__text h3")

list = []


for h3 in titles_and_ranks:
    list.append(h3.get_text())

list.reverse()

with open("top-moives.txt" , "w") as doc:
    for title in list:
        doc.write(title + "\n")
