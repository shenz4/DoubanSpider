# coding=utf-8
from scrapy.spiders import Spider
from scrapyspider.items import DoubanInfoItem
from scrapy.http import Request
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


class DoubanSpider(Spider):
    name = "douban_spider"
    allowed_domains = ['movie.douban.com']
    start_urls = ["https://movie.douban.com/top250/"]

    # 统计爬了多少page
    times = 0

    def parse(self, response):
        # 每调用这个函数,times + 1
        self.times += 1

        print(response.text)
        # 电影列表的xpath
        movie_list = response.xpath('//div[@class="article"]//ol[@class="grid_view"]//li')
        # 下一页的xpath的
        next_page = response.xpath('//span[@class="next"]/a[@href]/@href').extract_first()
        for movie in movie_list:
            # holder
            holder = DoubanInfoItem()
            # 片名
            holder["name"] = movie.xpath(
                './/div[@class="hd"]//span[@class="title"]/text()'
            ).extract_first()

            # 导演and主演
            three_attr = movie.xpath(
                './/div[@class="bd"]//p/text()'
            ).extract()
            t1 = three_attr[0]
            t2 = three_attr[1]
            # 去空格
            t1 = "".join(t1.split(" "))
            t2 = "".join(t2.split(" "))
            # 去回车
            t1 = "".join(t1.split("\n"))
            t2 = "".join(t2.split("\n"))

            holder["director"] = t1.split("\xa0\xa0\xa0")[0]
            try:
                holder["actors"] = t1.split("\xa0\xa0\xa0")[1]
            except:
                holder["actors"] = ""

            # 出版日期
            holder["publication_date"] = t2.split("\xa0\xa0\xa0")[0]

            # 评分
            holder["star"] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()'
            ).extract_first()
            # 评分人数
            holder["comment_count"] = movie.xpath(
                './/div[@class="star"]/span/text()'
            ).extract()[1]
            # 简介
            holder["profile"] = movie.xpath(
                './/p[@class="quote"]/span[@class="inq"]/text()'
            ).extract_first()
            yield holder

        # 拼接url并跳转到下一页
        if (next_page is not None) and (self.times <= 30):
            dest = self.start_urls[0] + next_page
            print(dest)
            yield Request(dest, callback=self.parse)
        else:
            print("本次共爬取了{}页信息".format(self.times))
