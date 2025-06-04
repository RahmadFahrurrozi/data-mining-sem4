import scrapy

class PaginationSpider(scrapy.Spider):
    name = "pagination"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogu"]

    def parse(self, response):
        pass