from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
y_website = response.text

soup = BeautifulSoup(y_website, "html.parser")
print(soup.title)

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    article_text = article_tag.getText()
    article_link = article_tag.a.get("href")
    article_links.append(article_link)
    article_texts.append(article_text)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)


upvotes = [int(upvote.split()[0]) for upvote in article_upvotes]
print(upvotes)

largest_number = max(upvotes)
largest_index = upvotes.index(largest_number)
print(article_links[largest_index])
print(article_texts[largest_index])


