import scrapy


class CleaningdataSpider(scrapy.Spider):
    name = "cleaningData"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/index.html"]
    

    def parse(self, response):
        print("[============================== START SCRAPING ==============================]")
        dataBook = response.css('article')
        for book in dataBook:
            bookName = book.css('h3 a::text').get()
            image = book.css('div.image_container img::attr(src)').get()
            priceTeks = book.css('p.price_color::text').get()
            price = float(priceTeks.replace('£', ''))

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
            
            print(f"Book Name: {bookName},\n Image Book: {image},\nPrice Book: {price},\nStock: {stock} \nRating: {rating}")

            # yield {
            #     'bookName': bookName,
            #     'image': image,
            #     'price': price,
            #     'stock': stock,
            #     'rating': rating
            # }
            
        print("[============================== END SCRAPING ==============================]")
