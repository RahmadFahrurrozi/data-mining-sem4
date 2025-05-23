import scrapy

class GamesSpider(scrapy.Spider):
    name= "games"
    start_urls = ["https://sandbox.oxylabs.io/products"]

    def parse(self, response):
        print("[============================== START SCRAPING ==============================]")
        dataGmes = response.css('div.product-card')
        for games in dataGmes:
            print("===================================")
            titleGames = games.css("h4.title::text").get()
            categoryGames = games.css("p.category span::text").getall()
            descriptionGames = games.css("p.description::text").get()
            priceGames = games.css("div.price-wrapper::text").get()
            # stockGames = games.css("p.css-1w904rj::text").get()


            print(f"Title Games: {titleGames}")  
            print(f"Category Games: {categoryGames}")  
            # print(f"Rating Games: {ratingGames}")
            print(f"Rating Games: {descriptionGames}")
            print(f"Price Games: {priceGames}")
            # print(f"Stock Games : {stockGames}")
            
        print("[============================== END SCRAPING ==============================]")
            
        