import scrapy

class GetWarningNotificationSpider(scrapy.Spider):
    name = "get_warning_notification"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        print("[============================== START SCRAPING ==============================]")
        
        # Mengambil semua teks warning dengan CSS selector yang lebih sederhana
        warning_text = response.css('div.alert.alert-warning::text').getall()
        #default > div.container-fluid.page > div > div > div > section > div.alert.alert-warning
        # Membersihkan whitespace dan menggabungkan teks
        cleaned_warning = " ".join([text.strip() for text in warning_text if text.strip()])
        
        print(f"Warning: {cleaned_warning}")
        print("[============================== END SCRAPING ==============================]")