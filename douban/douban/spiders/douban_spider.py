# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver
from project.douban.douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    #默认的解析方法
    def parse(self, response):
        moive_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in moive_list:
            douban_item = DoubanItem()
            douban_item['number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['moive_name'] = i_item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            content = i_item.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            for i_content in content:
                content_s = "".join(i_content.split())
                douban_item['introduce'] = content_s
            douban_item['star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            douban_item['describe'] = i_item.xpath(".//p[@class='quote']/span/text()").extract_first()
            douban_item['link'] = i_item.xpath(".//div[@class='hd']/a/@href").extract_first()
            # url = douban_item['link']
            # douban_item['comment']
            # dvi = webdriver.Chrome()
            # dvi.get(url)
            # time.sleep(2)
            # dvi.find_element_by_xpath('//*[@id="comments-section"]/div[1]/h2/span/a').click()
            # douban_item['comment'] = i_item.xpath('//*[@id="comments"]/div[1]/div[2]/p/span/text()').extract()
            # dvi.close()
            print(douban_item)
            yield douban_item
        next_link = response.xpath(".//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)
        print(moive_list)
