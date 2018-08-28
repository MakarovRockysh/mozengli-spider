# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.http import Request
import os
import execjs
import datetime
import re
from urllib.parse import urljoin
from selenium import webdriver
from scrapy.selector import Selector
from project.movies.movies.items import MoviesItem


class MoviesSpider(scrapy.Spider):
    name = 'movies_spider'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/list_23_1.html']

    def parse(self, response):
        movie_url = response.xpath('//table[@class="tbspan"]')
        for i_item in movie_url:
            # movie_item['movie_name'] = i_item.xpath(".//tr[2]/td[2]/b/a[text()!='[综合电影]']/text()").extract_first()
            upload_time = i_item.xpath(".//tr[3]/td[2]/font/text()").extract_first()
            upload_time = upload_time.split("：")[1].split("\r")[0]
            details_url = i_item.xpath(".//tr[2]/td[2]/b/a[text()!='[综合电影]']/@href").extract_first()
            details_url = urljoin('http://www.dytt8.net', details_url)
            yield scrapy.Request(details_url, callback=self.parse_url,meta={'upload_time':upload_time})

        #下一页
        # next_link = response.xpath('//div[@class="x"]//a[text()="下一页"]/@href').extract_first()
        # link = urljoin('http://www.dytt8.net/html/gndy/dyzz/', next_link)
        # time.sleep(0.5)
        # yield scrapy.Request(link, callback=self.parse)

        # -------------------------selenium模拟操作--------------------------#
        # try:
        #     option = webdriver.ChromeOptions()
        #     option.add_argument("headless")
        #     driver = webdriver.Chrome(chrome_options=option)
        #     driver.get(details_url)
        #     t_selector = Selector(text=driver.page_source)
        #     parameter = t_selector.xpath('//*[@style="WORD-WRAP: break-word"]/a/text()').extract_first()
        #     d_url = execjs.compile(
        #         open(r'/Users/k11/anaconda3/envs/mozengli-spider/project/movies/movies/base64.js').read()).call(
        #         'ThunderEncode', parameter)
        #     movie_item['download_url'] = d_url
        # finally:
        #     driver.close()
        #     os.system('killall chromedriver')
        # print(movie_item)
        # yield movie_item
        # -------------------------selenium模拟操作--------------------------#

    def parse_url(self, response):
        movie_item = MoviesItem()
        movie_item['star'] = response.xpath('//*[@id="Zoom"]//text()[11]').extract_first()
        movie_item['movie_name'] = response.xpath('//div[@class="title_all"]/h1/font/text()').extract_first()
        movie_item['director'] = response.xpath('//*[@id="Zoom"]//text()[17]').extract_first()
        movie_item['performer'] = response.xpath('//*[@id="Zoom"]//text()[18]').extract_first()
        movie_item['language'] = response.xpath('//*[@id="Zoom"]//text()[8]').extract_first()
        movie_item['subtitle'] = response.xpath('//*[@id="Zoom"]//text()[9]').extract_first()
        movie_item['movie_type'] = response.xpath('//*[@id="Zoom"]//text()[7]').extract_first()
        movie_item['video_size'] = response.xpath('//*[@id="Zoom"]//text()[14]').extract_first()
        movie_item['time'] = response.xpath('//*[@id="Zoom"]//text()[16]').extract_first()
        movie_item['release_date'] = response.xpath('//*[@id="Zoom"]//text()[10]').extract_first()
        movie_item['upload_time'] = response.meta['upload_time']
        movie_item['introduce'] = response.xpath('//*[@id="Zoom"]//text()[29]').extract_first()


        parameter = response.xpath('//tbody/tr/td/a/@href').extract_first()
        d_url = execjs.compile(open(r'/Users/k11/anaconda3/envs/mozengli-spider/project/movies/movies/base64.js').read()).call('ThunderEncode', parameter)
        movie_item['download_url'] = d_url
        print('<--------------------------------------------------->')
        print(movie_item)
        yield movie_item
