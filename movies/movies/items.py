# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesItem(scrapy.Item):
    # 编号
    number = scrapy.Field()
    # 豆瓣评分
    star = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 主演
    performer = scrapy.Field()
    # 语言
    language = scrapy.Field()
    # 字幕
    subtitle = scrapy.Field()
    # 电影类型
    movie_type = scrapy.Field()
    # 视频尺寸
    video_size = scrapy.Field()
    # 片长
    time = scrapy.Field()
    # 上映日期
    release_date = scrapy.Field()
    # 上传时间
    upload_time = scrapy.Field()
    # 电影详情url
    details_url = scrapy.Field()
    # 电影下载地址
    download_url = scrapy.Field()
    #电影介绍
    introduce = scrapy.Field()


