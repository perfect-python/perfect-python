import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Spider5Spider(CrawlSpider):
    name = 'spider5'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    rules = (
        Rule(LinkExtractor(allow='(page)'), callback='parse_page'),
    )

    def parse_page(self, response):
        print("page: " + response.url)
        # ❶ XPathによる要素の
        for quote in response.xpath("//div[@class='quote']"):
            item = {
                "text": quote.xpath("//span[@class='text']/text()").extract_first(),
                "author": quote.xpath("//small/text()").extract_first(),
            }
            print(item)

        for href in response.css('a::attr(href)'):
            yield response.follow(href, callback=self.parse)
