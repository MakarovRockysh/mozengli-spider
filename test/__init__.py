class Dytt8Spider(scrapy.Spider):
    name = 'dytt8'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/list_23_1.html']

    def parse(self, response):
        movie_url = response.xpath('//table[@class="tbspan"]')
        for i in movie_url:
            time.sleep(0.5)
            url_detail = i.xpath('tr[2]/td[2]//a[@class="ulink"]/@href').extract_first()
            url_detail = urljoin('http://www.dytt8.net', url_detail)
            print(url_detail)
            yield scrapy.Request(url_detail, callback=self.parse_url)
        n_url = response.xpath('//div[@class="x"]//a[text()="下一页"]/@href').extract_first()
        print(n_url)
        if n_url:
            next_url = urljoin('http://www.dytt8.net/html/gndy/dyzz/', n_url)
            print(next_url)
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_url(self, response):
        item = MovieItem()
        item['title'] = response.xpath('//div[@class="title_all"]/h1/font/text()').extract_first()
        content = response.xpath('//div[@id="Zoom"]//text()').extract()
        url = response.xpath('//tbody/tr/td/a/@href').extract_first()
        item['url'] = execjs.compile(open(r'./movie/base64.js').read()).call('ThunderEncode', url)
        print(item['url'])
        a = []
        for i in content:
            if i == '【下载地址】':
                break
            a.append(i)
        print(a)
        item['content'] = ''
        for i in a:
            item['content'] += i
        print(item['title'], item['content'])
        print(item['url'])
