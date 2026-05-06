import requests 
import userinput
from dotenv import load_dotenv
import sys
import os 

load_dotenv()
MAX_NO_OF_ARTICLES = 15
API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY:
    sys.exit("API Key not found try again ")


def getnews(TOPICS):
    topic_articles = {}
    for topic in TOPICS:
        payload={'q': topic, 
                 'apiKey': API_KEY, 
                 'pageSize': MAX_NO_OF_ARTICLES,
                 'language': 'en'
                 }
        r = requests.get('https://newsapi.org/v2/everything', params=payload)
        topic_articles.update({topic : processnews(r)}) 
    
    return topic_articles

def processnews(r):
    result_news_dict = r.json()
    articles = result_news_dict.get('articles', [])
    
    #print(f"\n{t.title()} (Total {result_news_dict['totalResults']}):")

    if not articles:
         return []
    return articles

     
def main(TOPICS):
    return getnews(TOPICS)


