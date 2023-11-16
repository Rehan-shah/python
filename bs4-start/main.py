from os import name
from bs4 import BeautifulSoup
import requests

content = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(content.text, "html.parser")

heading = soup.select(".titleline a")
upvote_span = soup.find_all(name="span" , class_="score")

article_texts = []
article_links = []
article_upvotes = []

for head in heading:
    article_texts.append(head.get_text())
    article_links.append(head.get("href"))

for span in upvote_span:
    article_upvotes.append(int(span.get_text().split()[0]))

max_id = article_upvotes.index(max(article_upvotes))

print(article_texts[max_id])
print(article_links[max_id])
print(article_upvotes[max_id])
