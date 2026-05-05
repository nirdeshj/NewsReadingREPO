import requests 
from datetime import datetime

TODAY = datetime.now().strftime("%Y-%m-%d")
MAX_NO_OF_ARTICLES = 50
TOPICS = 'United States'
DOMAINS = 'bbc.co.uk, apnews.com, reuters.com'
def getnews():
    payload={'q': TOPICS, 
             'apiKey': '5b2fcee5c1f5447c8e5da0f089704a3b', 
             'pageSize': MAX_NO_OF_ARTICLES, 
             'sources': 'bbc-news, associated-press, reuters',
             'domains' : DOMAINS
             }
    payload_headlines = {
        'apiKey': '5b2fcee5c1f5447c8e5da0f089704a3b',
        'country': 'us, gb'

    }
    r = requests.get('https://newsapi.org/v2/everything', params=payload)
    headlines = requests.get('https://newsapi.org/v2/top-headlines', params = payload_headlines)
    processnews(r)

def processnews(r):
    result_news_dict = r.json()
    noOfArticles = len(result_news_dict)
    news_link = []
    for article in range(0, (noOfArticles)):
        print(result_news_dict['articles'][article]['title'], result_news_dict['articles'][article]['url'])
        news_link.append(result_news_dict['articles'][article]['url'])
    news_link = [(x+"\n") for x in news_link]

    
    with open('newslink.txt', 'w') as f:
        for i in range(0, (noOfArticles)):
            f.write(news_link[i])
def main():
    getnews()


if __name__ == '__main__':
    main()