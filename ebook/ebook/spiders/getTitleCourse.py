import scrapy

class GetTitleCourseSpider(scrapy.Spider):
    name = "get_title_course"
    start_urls = ["https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short"]

    def parse(self, response):
        print("[============================== START SCRAPING ==============================]")
        title_course = response.css('div a div.course-block__body')
        for title in title_course:
            title = title.css('h4::text').get()
            print(f"Title Course: {title}")
        print("[============================== END SCRAPING ==============================]")