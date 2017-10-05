from scrapy import Spider


class TestSpider(Spider):
    name = "testSpider"

    start_urls = ["http://www.baidu.com",]

    def parse(self, response):
        print 'end parse****************************************************'
        m = response.body
        print m