# -*- coding: utf-8 -*-
import scrapy

class MinistrySpider(scrapy.Spider):
    name = 'Ministry'
    allowed_domains = ['agro.gov.kg/language/ru/ministry/minister']
    start_urls = [
        'http://agro.gov.kg/language/ru/ministry/minister/',
        'https://agro.gov.kg/language/ru/ministry/deputy-ministers'
        ]

    def parse(self, response):
        image_urls = response.css("div.elementor-image img::attr(data-src)").getall()
        name = response.css("div.elementor-text-editor h2::text").getall()
        biografy = response.css("div.elementor-tab-content *::text").getall()

        if len(name) == 0:
            name = response.css("h2.elementor-heading-title span::text").getall()
        
        yield{
            'name': name,
            'biografy': biografy,
            'image_urls': image_urls,
        }