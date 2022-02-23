import scrapy

class ZyteAssignment1Spider(scrapy.Spider):
    name = 'zyte_assignment1'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']


    # Top level, handles book categories
    def parse(self, response): 
        # Get list of all categories
        categories = response.css('ul.nav-list li ul li a::attr(href)').getall()

        # Go to each category. When there is not a 'next' category, the loop stops automatically
        for category in categories:
            yield response.follow(url=category, callback=self.handle_info)


    # Handles each page of the category
    def handle_info(self, response):
        # Scrapes each page of the category
        titles = response.css('article h3 a::attr(title)').getall()
        prices = response.css('p.price_color::text').getall()
        image_URLs = response.css('div.image_container a img::attr(src)').getall()
        details_page_URLs = response.css('div.image_container a::attr(href)').getall()

        # Each item is pipelined individually. It also takes care of duplications automatically
        for index, title in enumerate(titles):
            books = {
                'title': title, 
                'price': prices[index],
                'image_URL': response.urljoin(image_URLs[index]), 
                'details_page_URL': response.urljoin(details_page_URLs[index])
            }
            yield books

        # If there is a 'next' page, go there and repeat the same process
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(url=next_page, callback=self.handle_info)
