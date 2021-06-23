# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CommentItem(scrapy.Item):
    name = scrapy.Field()       # 电影名
    director = scrapy.Field()   # 导演
    region = scrapy.Field()     # 地区
    date = scrapy.Field()       # 评论时间
    type = scrapy.Field()       # 类型
    user_id = scrapy.Field()    # 用户名
    content = scrapy.Field()    # 评论内容
    star = scrapy.Field()       # 评分
    dianzan = scrapy.Field()    # 点赞数量