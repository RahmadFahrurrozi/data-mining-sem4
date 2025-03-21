import scrapy

class CategorySpider(scrapy.Spider):
    name = "category"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        print("[============================== START SCRAPING ==============================]")
        dataCategory = response.css('div.container-fluid.page div div aside div.side_categories ul li ul li') 
        for category in dataCategory:
            namaKategory = category.css('a::text').get()  
            namaKategory = namaKategory.strip() if namaKategory else None  
            print(f"Kategori: {namaKategory}")
            yield {
                'namaKategory': namaKategory
            }
        print("[============================== END SCRAPING ==============================]")
        #default > div.container-fluid.page > div > div > aside > div.side_categories > ul > li > ul > li:nth-child(1)
        #default > div.container-fluid.page > div > div > aside > div.side_categories > ul > li > ul > li:nth-child(1)