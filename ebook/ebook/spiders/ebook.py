import scrapy

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        print("[============================== START SCRAPING ==============================]")
        dataBuku = response.css('article')
        for buku in dataBuku:
            namaBuku = buku.css('h3 a::text').get()
            hargaBuku = buku.css('p.price_color::text').get()
            gambarBuku = buku.css('div.image_container img::attr(src)').get()
            stock = buku.css('p.instock.availability::text').getall()  
            stock = ' '.join([s.strip() for s in stock if s.strip()])
            
            print(f"Nama Buku: {namaBuku},\nHarga Buku: {hargaBuku},\nGambar Buku: {gambarBuku},\nStok: {stock}")
            yield {
                'namaBuku': namaBuku,
                'hargaBuku': hargaBuku,
                'stok': stock,
                'gambarBuku': gambarBuku
            }
        print("[============================== END SCRAPING ==============================]")