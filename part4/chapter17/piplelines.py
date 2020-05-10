import csv

class ScrapysamplePipeline(object):
　  # ❶スパイダーの開始時にコールされる
    def open_spider(self, spider):
        self.csvfile = open("quote.csv", "w")
        self.csvwriter = csv.writer(self.csvfile)
    
    # ❷スパイダーの終了時にコールされる
    def close_spider(self, spider):
        self.csvfile.close()

    # ❸スパイダーでアイテムがyeildされるごとにコールされる
    def process_item(self, item, spider):
        self.csvwriter.writerow([item["author"], item["text"]])

        return item
