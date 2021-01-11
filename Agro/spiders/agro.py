# -*- coding: utf-8 -*-
import scrapy, csv, json

class AgroSpider(scrapy.Spider):
    name = "Agro"
    page_incr = 1
    parse_urls = []
    start_urls = ['https://agro.gov.kg/language/ru/main',]
    pagination_url = 'https://agro.gov.kg/wp-admin/admin-ajax.php'

    def parse(self, response):
        sel = scrapy.selector.Selector(response)

        if self.page_incr > 1:
            data_json = json.loads(json.loads(response.body))
            sel = scrapy.selector.Selector(text=data_json['code'])

        links = sel.css("h3.post-title a::attr(href)").getall()
        self.parse_urls += links

        if sel.css("h3"):
            self.page_incr +=1
            formdata = {
                        "action": "tie_blocks_load_more",
                        "block[cat][]": [
                            "16",
                            "1"
                        ],
                        "block[id][]": "1",
                        "block[number]": "5",
                        "block[pagi]": "load-more",
                        "block[excerpt]": "true",
                        "block[excerpt_length]": "15",
                        "block[post_meta]": "true",
                        "block[read_more]": "true",
                        "block[breaking_effect]": "reveal",
                        "block[sub_style]": "timeline",
                        "block[style]": "timeline",
                        "page": str(self.page_incr),
                        "width": "single"
                    }
            yield scrapy.http.FormRequest(url=self.pagination_url, formdata=formdata, callback=self.parse)
        else:
            for url in self.parse_urls:
                yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        titles = response.css("h1.post-title::text").getall()
        descriptions = response.css("div.entry-content *::text").getall()
        public_times = response.css("span.date span::text").get()
        images = response.css("img.attachment-full::attr(data-src)").getall()

        yield {
            'titles': titles,
            'descriptions': descriptions,
            'times': public_times,
            'image_urls': images,
        }




