import scrapy


class Pagination4Spider(scrapy.Spider):
    name = "pagination4"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]


    def __init__(self):
        super().__init__()
        self.page = 1
        self.totalPage = 5
    
    def start_requests(self):
        baseUrl = "https://books.toscrape.com/catalogue"
        while self.page <= self.totalPage:
            yield scrapy.Request(f"{baseUrl}/page-{self.page}.html")
            self.page += 1


    def parse(self, response):
        print("[============================== START SCRAPING ==============================]")
        dataBook = response.css('article')
        for book in dataBook:
            namaBuku = book.css('h3 a::text').get()
            hargaBuku = book.css('p.price_color::text').get()
            stock = book.css('p.instock.availability::text').getall()  
            stock = ' '.join([s.strip() for s in stock if s.strip()])
            
            print(f"Nama Buku: {namaBuku},\nHarga Buku: {hargaBuku},\nStok: {stock}")

            yield {
                'namaBuku': namaBuku,
                'hargaBuku': hargaBuku,
                'stock': stock
            }
          
        print("[============================== END SCRAPING ==============================]")
