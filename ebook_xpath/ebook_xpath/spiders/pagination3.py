import scrapy


class Pagination3Spider(scrapy.Spider):
    name = "pagination3"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/index.html"]

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
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        yield {
            'namaBuku': namaBuku,
            'hargaBuku': hargaBuku,
            'stock': stock
        }
