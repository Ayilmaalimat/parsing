import scrapy


class MenuSpider(scrapy.Spider):
    name = 'Menu'
    allowed_domains = ['agro.gov.kg']
    start_urls = ['http://agro.gov.kg/']

    def parse(self, response):
        menuNav = response.css("div.main-menu *::text").getall()
        yield {
            "Nab Bar" : menuNav
        }
