import scrapy


class PrimersSpider(scrapy.Spider):
    name = 'primers'
    allowed_domains = ['https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1']
    start_urls = ['http://https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1/']

    def parse(self, response):
        pass
