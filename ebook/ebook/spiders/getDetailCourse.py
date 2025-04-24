import scrapy


class GetDetailCourseSpider(scrapy.Spider):
    name = "get_detail_course"
    start_urls = ["https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short"]

    def parse(self, response):
        print("[============================== START SCRAPING ==============================]")
        
        data_detail_course = response.css('div.course-block')
        
        for course in data_detail_course:
            print("=======================================================================")
            titleCourse = course.css("h4.course-block__title::text").get()
            description = course.css("p.course-block__description::text").get()
            cleanDataDescription = description.strip() if description else None
            duration = course.css('span.course-block__length::text').getall()
            cleanDataDuration = " ".join([text.strip() for text in duration if text.strip()])
            photoFounder = course.css('img.course-block__author-image::attr(src)').get()
            authorCourse = course.css('p.course-block__author-name::text').get()
            authorOccupation = course.css('p.course-block__author-occupation::text').get()

            print(f"Title Course: {titleCourse}")
            print(f"Description Course: {cleanDataDescription}")
            print(f"Duration Course: {cleanDataDuration}")
            print(f"Photo Founder: {photoFounder}")
            print(f"Author Course : {authorCourse}")
            print(f"Author Ocuppation : {authorOccupation}")

            yield {
                'titleCourse': titleCourse,
                'description': cleanDataDescription,
                'duration': cleanDataDuration,
                'photoFounder': photoFounder,
                'authorCourse': authorCourse,
                'authorOccupation': authorOccupation
            }

        print("[============================== END SCRAPING ==============================]")