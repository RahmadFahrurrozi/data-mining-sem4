import scrapy


#pagination with add url

class PaginationSpider(scrapy.Spider):
    name = "pagination"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    "https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html",
    ]

    def parse(self, response):
        print("[============================== START SCRAPING ==============================]")
        dataBook = response.css('article')
        for book in dataBook:
            namaBuku = book.css('h3 a::text').get()
            hargaBuku = book.css('p.price_color::text').get()
            # gambarBuku = book.css('div.image_container img::attr(src)').get()
            stock = book.css('p.instock.availability::text').getall()  
            stock = ' '.join([s.strip() for s in stock if s.strip()])
            
            print(f"Nama Buku: {namaBuku},\nHarga Buku: {hargaBuku},\nStok: {stock}")
          
        print("[============================== END SCRAPING ==============================]")