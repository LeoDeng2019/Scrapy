import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield{
                'text': quote.css('span.text::text').extract(),
                'author': quote.css('small.author::text').extract(),
                'tag': quote.css('a.tag::text').extract()
            }

        