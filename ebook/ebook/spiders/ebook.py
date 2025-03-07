import scrapy


class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        print("[============================== START SCRAPING ==============================]")
        # print(response.css('h3 a').get())
        dataBuku = response.css('article')
        for buku in dataBuku:
            namaBuku = buku.css('h3 a::text').get()
            hargaBuku = buku.css('p.price_color::text').get()
            gambarBuku = buku.css('div.image_container img::attr(src)').get()
            print(f"Nama Buku: {namaBuku},\nHarga Buku: {hargaBuku},\nGambar Buku: {gambarBuku}")
            yield {
                'namaBuku': namaBuku,
                'hargaBuku': hargaBuku,
                'gambarBuku': gambarBuku
            }
        print("[============================== END SCRAPING ==============================]")
