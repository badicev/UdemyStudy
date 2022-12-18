from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()


soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)

# print(soup.prettify())

print(soup.a)
print(soup.li)
print(soup.p)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())