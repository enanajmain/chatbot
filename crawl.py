import requests
import re
from bs4 import BeautifulSoup

quote_page = "https://www.lyrics.com/lyric/16415874/Mims/Rock+%27n+Rollin%27"
page = requests.get(quote_page)
soup = BeautifulSoup(page.content, "html.parser")

print(soup.find("pre", {"id": "lyric-body-text"}).get_text())
