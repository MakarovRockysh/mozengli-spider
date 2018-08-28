from scrapy import cmdline
cmdline.execute('scrapy crawl movies_spider -o test.csv'.split())