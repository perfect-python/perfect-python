import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# ❶CrawlSpiderを拡張したクラス
class Spider3Spider(CrawlSpider):
    name = 'spider3'
    allowed_domains = ['quotes.toscrape.com']

    start_urls = ['http://quotes.toscrape.com']

    # ❷ruleの定義
    rules = (
        Rule(LinkExtractor(allow='(tag)'), callback='parse_tag'),
        Rule(LinkExtractor(allow='(page)'), callback='parse_page')
    )

    def parse_tag(self, response):
        print("tag: " + response.url)
        for href in response.css('a::attr(href)'):
            yield response.follow(href, callback=self.parse)

    def parse_page(self, response):
        print("page: " + response.url)
        for href in response.css('a::attr(href)'):
            yield response.follow(href, callback=self.parse)

