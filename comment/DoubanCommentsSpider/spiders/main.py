# coding=utf-8
from scrapy import cmdline

if __name__ == "__main__":
    cmdline.execute("scrapy crawl douban_comments_spider -o ./output/douban_movie_comments.csv".split())
