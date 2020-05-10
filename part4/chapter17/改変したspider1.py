# -*- coding: utf-8 -*-
import scrapy


class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['gihyo.jp']
    start_urls = ['http://gihyo.jp/']

    def parse(self, response):
        with open('index.html', 'w') as html_file:
            # ❶responseのhtmlをファイルに保存
            html_file.write(response.text)
