import scrapy

class DatabukuSpider(scrapy.Spider):
    name = "dataBuku"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        # Mengambil semua elemen article
        books = response.xpath("//article")
        
        # Looping melalui setiap buku
        for book in books:
            judul = book.xpath(".//h3/a/text()").get()
            title = book.xpath(".//h3/a/@title").get()
            price = book.xpath(".//p[@class='price_color']/text()").get()  # Perbaikan di sini
            stock = book.xpath(".//p[contains(@class, 'instock')]/text()[normalize-space()]").get()  # Perbaikan di sini
            href = book.xpath(".//h3/a/@href").get()
           
            print("==========================")
            print(f"Judul: {judul}")
            print(f"Title: {title}")
            print(f"Price: {price}")
            print(f"Stock: {stock.strip()}")  # Membersihkan whitespace
            print(f"URL: {href}")
            print("==========================")