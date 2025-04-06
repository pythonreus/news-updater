from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='API_KEY') # i need to enter my api key here

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()


def populate_news_database():
	pass	

def get_all_news_updates():
	pass

def get_single_news_update(news_id):
	pass

def delete_current_news_updates():
	pass