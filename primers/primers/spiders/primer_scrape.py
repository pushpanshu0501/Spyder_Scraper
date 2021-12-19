import scrapy

class PrimerSpider(scrapy.Spider):
    name = "primer_scrape"
    
    def start_requests(self):
        self.index = 0
        urls = [
            'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1',
        ]
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)
    
    def parse(self, response):
        price = response.css('.price span::text').extract()
        title = response.css('.catalog-item-name::text').extract()
        stock_status = response.css('.out-of-stock::text').extract()
        manufacturor = response.css('.catalog-item-brand::text').extract()

        # if(stock_status=='Out of Stock'): stock_status=False
        # else: stock_status=True

        for item in zip(price,title,stock_status,manufacturor):
            #create a dictionary to store the scraped info
            status_stock = True
            if(item[2]=='Out of Stock'): status_stock=False
            else: status_stock= True

            scraped_info = {
                'Price ($)' : item[0][1:],
                'Title' : item[1],
                'Stock Status' : status_stock,
                'Manufacturor' : item[3]
            }

            yield scraped_info

