import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com']+[
        'https://quotes.toscrape.com/page/{}'.format(i) for i in range(2,4)
        ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield{
                'text': quote.css('span.text::text').extract(),
                'author': quote.css('small.author::text').extract(),
                'tag': quote.css('a.tag::text').extract()
            }

