from crawler import YTCrawler
from face import Face

class Interact:
    def __init__(self):
        self.key = '19a47ce8abd540fc9fcc3dfc06c11342'
        self.url = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/detect'

    def playSongAccordingToEmo(self):
        emo = Face()
        happiness, sadness = emo.getEmo(self.key, self.url)
        #print(happiness)
        #print(sadness)
        crawler = YTCrawler()
        if happiness >= sadness :
            crawler.retrieve_vids("happy songs")
        else:
            crawler.retrieve_vids("sad songs")

if __name__=="__main__":
    obj = Interact()
    obj.playSongAccordingToEmo()

