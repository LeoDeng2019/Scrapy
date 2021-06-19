import scrapy
from whiskyScraper.items import WhiskyscraperItem

class WhiskySpider(scrapy.Spider):
    name = 'whisky'
    start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self, response):
        item = WhiskyscraperItem()
        for product in response.css('div.product-item-info'):
            
            item['name'] = product.css('a.product-item-link::text').get()
            item['href'] = product.css('a.product-item-link').attrib['href']
            item['price'] = product.css('span.price::text').get()

            yield item
            
        
        next_page = response.css('a.action.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

