# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from urllib.parse import unquote

class customImagePipline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        return request.url.split('/')[-1]

class customFilePipline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        url_name = request.url.split('/')[-1] 
        return unquote(url_name)