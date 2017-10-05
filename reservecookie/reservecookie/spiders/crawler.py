from scrapy import Spider

class MySpider(Spider):
    name = "neu"

    start_urls = ["http://www.baidu.com",]

    def parse(self, response):
        print response