import scrapy


class NewsscraperSpider(scrapy.Spider):
    name = "newsScraper"
    allowed_domains = ["news.google.com"]
    start_urls = ["https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"]

    def parse(self, response):
        
        articles = response.xpath("//c-wiz/c-wiz/c-wiz")
        for article in articles:
            #title = article.xpath("/c-wiz/c-wiz/article/a/text()")
            yield {
                "title": article.css("article a::text").get(),
                "link": article.css("article a").attrib["href"]
                }