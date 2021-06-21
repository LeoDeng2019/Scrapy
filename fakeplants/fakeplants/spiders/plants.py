import scrapy


class PlantsSpider(scrapy.Spider):
    name = 'plants'
    allowed_domains = ['fake-plants.co.uk']
    start_urls = ['http://fake-plants.co.uk/']

    def parse(self, response):
        for link in response.css('li.product-category a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_cate)
    
    def parse_cate(self, response):
        for product in response.css('li.ast-col-sm-12'):
            yield {
                'cate': product.css('span.ast-woo-product-category::text').get().strip(),
                'name': product.css('h2.woocommerce-loop-product__title::text').get()            
            }
