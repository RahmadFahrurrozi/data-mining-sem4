import scrapy

class DatanewsSpider(scrapy.Spider):
    name = "dataNews"
    allowed_domains = ["www.kompas.com"]
    start_urls = ["https://www.kompas.com/"]

    def parse(self, response):

        print('==================start==================')

        listNewshighlight = response.css('div.spotlightCol')

        for news in listNewshighlight:
            print("===================================")
            titleNews = news.css('h2.spotlightTitle::text').get()
            print(f"Title News: {titleNews}")
        print('==================end==================')
            