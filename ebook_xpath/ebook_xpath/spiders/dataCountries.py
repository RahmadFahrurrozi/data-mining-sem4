import scrapy

class DatacountriesSpider(scrapy.Spider):
    name = "dataCountries"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/simple/"]

    def parse(self, response):

        for country in response.css('div.country'):
            
            country_name = country.css('h3.country-name::text').getall()      
          
            population = country.css('span.country-population::text').get()
         
            print(f"Negara: {country_name} Populasi: {population}")
            
         