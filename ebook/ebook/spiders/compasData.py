import scrapy

class CompasDataSpider(scrapy.Spider):
    name = "compasData"
    allowed_domains = ["www.kompas.com"]
    start_urls = ["https://www.kompas.com/"]

    def parse(self, response):
        print('==================start==================')
        listNewshighlight = response.css('div.spotlightItem')
        # print(f'jumlah berita sorotan : {len(listNewshighlight)}')
        for news in listNewshighlight:
            print("===================================")
            titleNews = news.css('h2.spotlightTitle::text').get()
            cleanDataTitleNews = titleNews.strip() if titleNews else None
            print(f"Title News: {cleanDataTitleNews}")
        print('==================end==================')