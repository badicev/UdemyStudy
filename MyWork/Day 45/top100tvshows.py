from bs4 import BeautifulSoup
import requests
import json

response = requests.get("https://www.empireonline.com/tv/features/best-tv-shows-ever-2/")

soup = BeautifulSoup(response.content, "html.parser")

top100 = json.loads(soup.select_one("#__NEXT_DATA__").contents[0])


# movies = soup.find_all(name="h3", class_="jsx-4245974604")

# print(soup)
def find_articles(data):
    try:
        if isinstance(data, dict):
            for k, v in data.items():
                if k.startswith("ImageMeta:"):
                    yield v["titleText"]
                else:
                    yield from find_articles(v)
        elif isinstance(data, list):
            for i in data:
                yield from find_articles(i)
    except:
        pass


movies_list = []
for a in find_articles(top100):
    movies_list.append(a)
movies = movies_list[::-1]  # reverse the list

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"[{movie}\n")

