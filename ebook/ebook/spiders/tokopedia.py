import scrapy

class TokopediaSpider(scrapy.Spider):
    name = "tokopedia"
    start_urls = ["https://www.tokopedia.com/p/handphone-tablet/handphone"]

    def parse(self, response):
        print("[============================== START SCRAPING ==============================]")
        dataTitleProduct = response.css('div.prd_link-product-name.css-3um8ox::text').getall()
        for titleName in dataTitleProduct:
            titleName = titleName.strip() if titleName else None
            print(f"Title: {titleName}")
        print("[============================== END SCRAPING ==============================]")