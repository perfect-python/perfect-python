import scrapy

# ❶scrapy.Itemクラスを派生して、データを保存するQuoteItemクラスを定義
class QuoteItem(scrapy.Item):
    # ❷アイテムのデータはscrapy.Fieldのオブジェクトとして定義
    author = scrapy.Field()
    text = scrapy.Field()
