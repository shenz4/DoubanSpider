# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanInfoItem(scrapy.Item):
    # 片名
    name = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 主演
    actors = scrapy.Field()
    # 发布日期
    publication_date = scrapy.Field()
    # 评分
    star = scrapy.Field()
    # 评分人数
    comment_count = scrapy.Field()
    # 简介
    profile = scrapy.Field()
