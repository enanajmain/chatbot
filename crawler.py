import requests
from bs4 import BeautifulSoup

class YTCrawler:
    def __init__(self):
        pass

    def retrieve_vids(self, query, qnt = 5):
        words = query.split()
        keyword_str = ""
        for w in words:
            if w is words[0]:
                keyword_str = keyword_str + w;
            else:
                keyword_str = keyword_str + "+" + w
        site_link = "https://www.youtube.com/results?search_query=" + keyword_str + "&sp=CAMSAhAB"
        site = requests.get(site_link)
        soup = BeautifulSoup(site.content, "html.parser")

        title = soup.find_all('h3', {'class':'yt-lockup-title'})
        link = ""
        no = 0
        for tits in title:
            links = tits.children
            for l in links:
                if l.has_attr('href'):
                    link = link + l['href']
            print(str(no+1) + ". " + tits.get_text())
            print("links : www.youtube.com" + str(link))
            link = ""
            no +=1
            if no == qnt:
                return
