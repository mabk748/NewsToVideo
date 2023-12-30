from newsapi import NewsApiClient
from dotenv import load_dotenv
import openai
import os
import json

load_dotenv()

def news_params(q=None,
        qintitle=None,
        sources=None,
        domains=None,
        exclude_domains=None,
        from_param=None,
        to=None,
        language=None,
        sort_by=None,
        page=None,
        page_size=None):
    return {"q": q,
            "qintitle": qintitle,
            "sources": sources,
            "domains": domains,
            "exclude_domains": exclude_domains,
            "from_param": from_param,
            "to": to,
            "language": language,
            "sort_by": sort_by,
            "page": page,
            "page_size": page_size}

class GetNews:
    def __init__(self, GPTModel) -> None:
        self.NewsClient = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))
        self.GPTKey = os.getenv["OPENAI_KEY"]
        self.GPTModel = GPTModel

    def get_relevent_News(self, **kwarg):
        articles = self.NewsClient.get_everything(q=kwarg["q"],
                                                  qintitle=kwarg["qintitle"],
                                                  sources=kwarg["sources"],
                                                  domains=kwarg["domains"],
                                                  exclude_domains=kwarg["exclude_domains"],
                                                  from_param=kwarg["from_param"],
                                                  to=kwarg["to"],
                                                  language=kwarg["language"],
                                                  sort_by=kwarg["sort_by"],
                                                  page=kwarg["page"],
                                                  page_size=kwarg["page_size"])
        
        titles = json.loads (articles)[""]
        openai.api_key = self.GPTKey
        relevantArticles = openai.ChatCompletion.create(model=self.GPTModel,
                                                        message={"content": f"GIVE ME ONLY THE TITLES SEPERATED BY A COMMA OF THE 5 MOST RELEVANT FROM THE FOLLOWING TITLES TO ATTRACT VIEWERS FOR A NEWS VIDEO {titles}"})
        return relevantArticles.split(", ")
