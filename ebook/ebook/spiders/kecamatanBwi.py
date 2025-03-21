import scrapy

class saucedemoSpider(scrapy.Spider):
    name = "saucedemo"
    start_urls = ["https://www.saucedemo.com/"]

    def parse(self, response):
        # Kirim request login
        print("[============================== START SCRAPING ==============================]")
        print(response)
        print("[============================== END SCRAPING ==============================]")