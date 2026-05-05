import requests 
from datetime import datetime
import userinput

TODAY = datetime.now().strftime("%Y-%m-%d")

MAX_NO_OF_ARTICLES = 4
TOPICS = userinput.main()
API_KEY = '5b2fcee5c1f5447c8e5da0f089704a3b'

def getnews():
    for topic in TOPICS:
        payload={'q': topic, 
                 'apiKey': API_KEY, 
                 'pageSize': MAX_NO_OF_ARTICLES
                 }
        r = requests.get('https://newsapi.org/v2/everything', params=payload)
        processnews(r, topic)
        

def processnews(r, t):
    result_news_dict = r.json()
    noOfArticles = len(result_news_dict)
    print(f"\n{t}:")
    try: 
        for i in range(0, noOfArticles):
            print(f"{i+1}. {result_news_dict['articles'][i]['title']}")
    except IndexError:
        print('No articles were found')


    
            
            
def main():
    getnews()


if __name__ == '__main__':
    main()