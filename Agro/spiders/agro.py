# -*- coding: utf-8 -*-
import scrapy, csv, json

class AgroSpider(scrapy.Spider):
    name = "Agro"

    start_urls = [
            'https://agro.gov.kg/language/ru/main',
        ]
     
    page_incr = 1
    parse_urls = []
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
                print(url)

    def parse_item(self, response):
        print(response.body)
        # title = response.css("h1.post-title a::text").getall()
        # description = response.css("div.entry-content::text").getall()
        # image = response.css("img.attachment-full::attr(src)").getall()
        # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        # print(title)
        # print("\n\n\n")
        # print(description)
        # print("\n\n\n")
        # print(image)
        # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")



