import scrapy
from scrapy.crawler import CrawlerProcess
from Agro.spiders.agro import AgroSpider
from Agro.spiders.docs import DocsSpider
from Agro.spiders.menu import MenuSpider
from Agro.spiders.ministry import MinistrySpider


if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "FEEDS": {
            "data.csv": {"format": "csv"},
        },
        "ITEM_PIPELINES" : {
            'Agro.pipelines.customImagePipline': 1,
            'Agro.pipelines.customFilePipline': 1,
        },
        "DOWNLOAD_TIMEOUT" : 1200,

        "MEDIA_ALLOW_REDIRECTS" : True,

        "IMAGES_STORE" : 'images',
        "FILES_STORE" : 'files',

        "LOG_LEVEL" : 'DEBUG',
        "LOG_FILE" : 'log.txt',
    })

    process.crawl(DocsSpider)
    process.crawl(MenuSpider)
    process.crawl(MinistrySpider)
    process.crawl(AgroSpider)
    
    process.start()