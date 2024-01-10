from newsapi import NewsApiClient
from dotenv import load_dotenv
import openai
import os

load_dotenv()

def news_params(q=None,
        qintitle=None,
        sources=None,
        domains=None,
        country=None,
        category=None,
        exclude_domains=None,
        from_param=None,
        to=None,
        language="en",
        sort_by=None,
        page=None,
        page_size=None
    ):
    return {"q": q,
            "qintitle": qintitle,
            "sources": sources,
            "domains": domains,
            "country": country,
            "category": category,
            "exclude_domains": exclude_domains,
            "from_param": from_param,
            "to": to,
            "language": language,
            "sort_by": sort_by,
            "page": page,
            "page_size": page_size}


class GetNewsAPI:
    def __init__(self) -> None:
        super().__init__()
        self.NewsClient = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))
    
    def get_all_news(self, **kwarg):
        return self.NewsClient.get_everything(
                q=kwarg["q"],
                qintitle=kwarg["qintitle"],
                sources=kwarg["sources"],
                domains=kwarg["domains"],
                exclude_domains=kwarg["exclude_domains"],
                from_param=kwarg["from_param"],
                to=kwarg["to"],
                language=kwarg["language"],
                sort_by=kwarg["sort_by"],
                page=kwarg["page"],
                page_size=kwarg["page_size"]
            )
    
    def get_top_news(self, **kwarg):
        return self.NewsClient.get_top_headlines(
                q=kwarg["q"],
                qintitle=kwarg["qintitle"],
                sources=kwarg["sources"],
                language=kwarg["language"],
                country=kwarg["country"],
                category=kwarg["category"],
                page_size=kwarg["page_size"],
                page=kwarg["page"]
            )

class ManageNews:
    def __init__(self, GPTModel) -> None:
        self.GPTKey = os.getenv["OPENAI_KEY"]
        self.GPTModel = GPTModel

    def get__titles(self, news: dict) -> list:
        titles = ""
        for article in news["articles"]:
            titles += article["title"] + ", "
        openai.api_key = self.GPTKey
        #relevantArticles = openai.ChatCompletion.create(model=self.GPTModel,
        #                                                message={"content": f"GIVE ME ONLY THE TITLES SEPERATED BY A COMMA OF THE 5 MOST RELEVANT FROM THE FOLLOWING TITLES TO ATTRACT VIEWERS FOR A NEWS VIDEO {titles}"})
        relevantArticles = titles

        return relevantArticles.split(", ")
    
    def get_relevent_Articles(self, titles=None, news=None) -> list:
        if news == None:
            raise ValueError("No source have been Provided")
        articles = []
        if titles == None:
            titles = self.get__titles(news)
            for i in news:
                if i["title"] in titles:
                    articles.append(i)
        else:
            if type(titles) == str:
                titles = list(titles)
            for i in news:
                if i["title"] in titles:
                    articles.append(i)
        
        return articles
    

