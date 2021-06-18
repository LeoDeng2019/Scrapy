import scrapy

class WhiskySpider(scrapy.Spider):
    name = 'whisky'
    start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self, response):
        for product in response.css('div.product-item-info'):
            yield {
                'name': product.css('a.product-item-link::text').get(),
                'href': product.css('a.product-item-link').attrib['href'],
                'price': product.css('span.price::text').get(),
            }
        
        next_page = response.css('a.action.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

