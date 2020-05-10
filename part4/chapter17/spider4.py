import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Spider4Spider(CrawlSpider):
    name = 'spider4'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    # ❶ルールではURLにpageを含むページだけを処理する
    rules = (
        Rule(LinkExtractor(allow='(page)'), callback='parse_page'),
    )

    # ❷parse_pageメソッドでスクレーピング処理
    def parse_page(self, response):
        print("page: " + response.url)
        for quote in response.css("div.quote"):
            item = {
                "text": quote.css("span.text::text").extract_first(),
                "author": quote.css("small.author::text").extract_first(),
            }
            print(item)

        for href in response.css('a::attr(href)'):
            yield response.follow(href, callback=self.parse)
