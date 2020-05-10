# -*- coding: utf-8 -*-
import scrapy

# ❶クラス宣言
class Spider1Spider(scrapy.Spider):
    # ❷スパイダーの名前
    name = 'spider1'
    # ❸巡回を許可するドメイン
    allowed_domains = ['gihyo.jp']
    # ❹巡回するURL
    start_urls = ['http://gihyo.jp/']

    #❺取得したURLを処理
    def parse(self, response):
        pass
