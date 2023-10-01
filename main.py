from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.select(".titleline a")
articles_text = []
articles_link = []
dummy=[]

n=0
for article in articles:
    text = article.getText()
    articles_text.append(text)
    link = article.get("href")
    dummy.append(link)

for item in dummy:
    if n % 2 == 0:
        articles_link.append(item)
    n+=1

articles_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(articles_text)
print(articles_link)
print(articles_upvote)
max(articles_upvote)
val = False
if len(articles_text) == len(articles_link) == len(articles_upvote):
    val = True
print(val)
# with open(file="website.html", encoding="utf-8") as web:
#     contents = web.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags = soup.find_all(name="a")
# for a in all_anchor_tags:
#     print(a.get("href"))
