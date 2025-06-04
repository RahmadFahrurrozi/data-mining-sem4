import scrapy

#pagination with button next trigger

class Pagination2Spider(scrapy.Spider):
    name = "pagination2"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/category/books/sequential-art_5"]

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

        # Get the href attribute of the next button
        next_button_href = response.css('li.next a::attr(href)').get()
        if next_button_href is not None:
            yield response.follow(next_button_href, self.parse)
        