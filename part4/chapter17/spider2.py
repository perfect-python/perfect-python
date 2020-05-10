# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor


class Spider2Spider(scrapy.Spider):
    name = 'spider2'
    allowed_domains = ['gihyo.jp']
    start_urls = ['http://gihyo.jp/']
    
    def parse(self, response):
        # ❶取得したページのURLを出力
        print(response.url)
        # ❷ページ内のリンクを抽出するLinkExtractorオブジェクトを作成
        le = LinkExtractor()
        # ❸ページ内のリンクを抽出
        for link in le.extract_links(response):
            # ❹抽出したリンクからRequestオブジェクトを生成して返す
            yield response.follow(
                link.url,
                self.parse)
