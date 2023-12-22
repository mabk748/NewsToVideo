import scrapy


class NewsscraperSpider(scrapy.Spider):
    name = "newsScraper"
    allowed_domains = ["news.google.com"]
    start_urls = ["https://news.google.com"]

    def parse(self, response):
        pass
