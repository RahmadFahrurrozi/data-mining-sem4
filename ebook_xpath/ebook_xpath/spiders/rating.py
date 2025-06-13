import scrapy


class RatingSpider(scrapy.Spider):
    name = "rating"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/index.html"]
    

    def parse(self, response):
        print("[============================== START SCRAPING ==============================]")
        dataBook = response.css('article')
        for book in dataBook:
            namaBuku = book.css('h3 a::text').get()
            hargaBuku = book.css('p.price_color::text').get()
            ratingTeks = book.css('p::attr(class)').get().split(' ')[1]
            if ratingTeks == 'One':
                rating = 1
            elif ratingTeks == 'Two':
                rating = 2
            elif ratingTeks == 'Three':
                rating = 3
            elif ratingTeks == 'Four':
                rating = 4
            elif ratingTeks == 'Five':
                rating = 5
            
            stock = book.css('p.instock.availability::text').getall()  
            stock = ' '.join([s.strip() for s in stock if s.strip()])
            
            print(f"Nama Buku: {namaBuku},\nHarga Buku: {hargaBuku},\nStok: {stock} \nRating: {rating}")

            yield {
                'namaBuku': namaBuku,
                'hargaBuku': hargaBuku,
                'stock': stock,
                'rating': rating
            }
            
        print("[============================== END SCRAPING ==============================]")
