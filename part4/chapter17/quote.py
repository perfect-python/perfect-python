import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scrapysample.items import QuoteItem

class QuoteSpider(CrawlSpider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow='(page)'), callback='parse_page'),
    )
    
    def parse_page(self, response):
        print("page: " + response.url)
        for quote in response.css("div.quote"):
            # ❶リスト17.9で定義したQuoteItemオブジェクトの作成
            item = QuoteItem()
            # ❷作成したitemの各フィールドに値を設定
            item["text"] =  quote.css("span.text::text").extract_first()
            item["author"] = quote.css("small.author::text").extract_first()
            
            # ❸itemをyeildする
            yield item

        for href in response.css('a::attr(href)'):
            yield response.follow(href, callback=self.parse)
