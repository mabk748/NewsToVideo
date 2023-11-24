from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='216d716c191442b9aac2e3b1d84de482')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='israel',
                                          sources='bbc-news,the-verge',
                                          language='en')
print(top_headlines)

# /v2/everything


# /v2/top-headlines/sources
sources = newsapi.get_sources() 


