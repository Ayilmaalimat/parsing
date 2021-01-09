# -*- coding: utf-8 -*-
import scrapy, re

class DocsSpider(scrapy.Spider):
    name = 'Docs'
    start_urls = ['https://agro.gov.kg/language/ru/ads/']

    def parse(self, response):
        docs = response.css("a.bfd-svg-container.bfd-single-download-btn::attr(href)").getall()
        titles = response.css("p.bfd-download-title strong::text").getall()

        subtitles = ''.join(response.css("p.bfd-bottom-zero small::text").getall())
        t_formats = re.findall(':(\W|)(docx|pdf|doc|rar)', subtitles)
        formats = list(map(lambda x: x[-1], t_formats))
        
        yield {
            'file_urls': docs,
            'doc_titles': titles,
            'doc_formats':formats,
        }

