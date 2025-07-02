import requests
url = "https://rle.wiki/campus/"
response = requests.get(url)
print(response)

from bs4 import BeautifulSoup
contents = response.text
soup = BeautifulSoup(contents, "html.parser")

# 提取大学名称
all_titles= soup.find_all("li")
for title in all_titles:
    print(title.string)
