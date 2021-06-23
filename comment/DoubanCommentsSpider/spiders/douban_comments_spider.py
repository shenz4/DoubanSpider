import io
import logging
import re
import sys

from scrapy import FormRequest
from scrapy.http import Request
from scrapy.spiders import Spider

from DoubanCommentsSpider.items import CommentItem

# 解决windows平台下编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# logger配置
logging.basicConfig(
    filename="./output/debug_info",
    level=logging.DEBUG
)
logger = logging.getLogger("douban_logger")


class DoubanCommentsSpider(Spider):
    name = "douban_comments_spider"
    allowed_domains = ["douban.com"]
    start_urls = ["https://accounts.douban.com/login", "https://movie.douban.com/cinema/nowplaying/chongqing/"]

    # 通过re找出src-URL中的验证码id
    @staticmethod
    def re_get_id(url):
        re_id = re.compile("https://www\.douban\.com/misc/captcha\?id=.*?&size=s")
        id_list = re_id.findall(url)
        return id_list[0]

    # 入口函数
    def start_requests(self):
        yield Request(url=self.start_urls[0], callback=self.post_login)

    # 模拟登陆
    def post_login(self, response):
        # 账号密码输入提示
        account = input("please input account:")
        password = input("please input password:")
        # 若需要输入验证码,进入if语句
        # 获取验证码图片和id,用户自己识别
        # 不清楚写得对不对,自己没运行到这段
        verify = response.xpath('//*[@id="captcha_image"]')
        if verify:
            verify_info = response.xpath(".//@src").extract_first().extract_first()
            verify_id = self.re_get_id(verify_info)
            print("Verification code URL:", verify_info)
            verify_answer = input("please input verification code")
            yield FormRequest.from_response(response,
                                            formdata={
                                                "source": "movie",
                                                "redir": "https://movie.douban.com",
                                                "form_email": account,
                                                "form_password": password,
                                                "captcha-solution": verify_answer,
                                                "captcha-id": verify_id,
                                                "login": "登录"
                                            }, callback=self.parse)
            logger.info("login sucessfully!")
        # 不需要验证码就跳入else语句
        else:
            yield FormRequest.from_response(response,
                                            formdata={
                                                "source": "movie",
                                                "redir": "https://movie.douban.com/",
                                                "form_email": account,
                                                "form_password": password,
                                                "login": "登录"
                                            }, callback=self.main_page)

    def main_page(self, response):
        logger.info(response.url)
        yield Request(self.start_urls[1], callback=self.parse)

    def parse(self, response):
        logger.info("begin to parse!")
        # 获取电影列表
        movie_urls_list = response.xpath(
            '//div[@class="mod-bd"]//li[@data-category="nowplaying"]//li[@class="poster"]/a/@href'
        ).extract()

        # 如果列表不为null,说明当前页面是“导航页面”，遍历所有“电影主页”后return
        # 否则说明当前页面是“电影主页”或“评论页面”，进行下一步判断
        if movie_urls_list:
            for url in movie_urls_list:
                yield Request(url, callback=self.redirect)
                logger.info("1.电影列表{}".format(url))

    def redirect(self, response):
        redirect_url = response.xpath(
            '//*[@id="comments-section"]/div[1]/h2/span/a/@href'
        ).extract()
        # 如果元素不为None,说明当前页面是“电影主页”,需要重定向到“所有评论”
        if redirect_url:
            for i in redirect_url:
                yield Request(i, callback=self.parse_detail)
                logger.info("2.重定向:{}".format(i))

    # 核心,爬取评论并处理下一页跳转
    def parse_detail(self, response):
        # 评论列表
        comments_list = response.xpath(
            '//div[@class="mod-bd"]//div[@class="comment-item"]'
        )
        # 下一页地址
        next_page = response.xpath(
            '//div[@class="mod-bd"]//div[@class="center"]/a[@class="next"]/@href'
        ).extract_first()
        # 当前地址
        current_url = response.url.split("?")
        # 电影名称
        name = response.xpath(
            '//div[@id="wrapper"]//div[@id="content"]/h1/text()'
        ).extract_first()
        name = name.split(" ")[0]
        # 导演名称
        director = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div/span/p[1]/a/text()'
        ).extract_first()
        # 类型
        movie_type = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div/span/p[3]/text()'
        ).extract()
        movie_type = "".join(movie_type)
        movie_type = movie_type.replace(" ", "")
        movie_type = movie_type.replace("\n", "")

        # 地区
        region = response.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div/span/p[4]/text()'
        ).extract()
        region = "".join(region)
        region = region.strip()

        # # 上映时间
        # up_time = response.xpath(
        #     '//*[@id="content"]/div/div[2]/div[1]/div/span/p[6]/text()'
        # ).extract_first()
        # up_time = "".join(up_time.split(" "))

        for i in comments_list:
            # 生成 scrapy 容器
            holder = CommentItem()
            holder["name"] = name
            holder["director"] = director
            holder["type"] = movie_type
            holder["region"] = region

            # 获取用户id
            holder["user_id"] = i.xpath(
                './/span[@class="comment-info"]/a/text()'
            ).extract_first()
            # 获取评论内容
            holder["content"] = i.xpath(
                './/span[@class="short"]/text()'
            ).extract_first()
            # 获取评论时间
            t = i.xpath(
                './/span[@class="comment-info"]/span[last()]/text()'
            ).extract_first()
            t = "".join(t)
            holder["date"] = t.strip()
            # 获取评分
            t = i.xpath(
                './/span[@class="comment-info"]/span[last()-1]/@class'
            ).extract()
            t = "".join(t)
            holder["star"] = t.strip()
            # 获取点赞数
            t = i.xpath(
                './/span[@class="votes"]/text()'
            ).extract_first()
            t = t.split(" ")[0]
            holder["dianzan"] = t
            yield holder

        if next_page is not None:
            dest = current_url[0] + next_page
            yield Request(dest, callback=self.parse_detail)
            logger.info("3.电影名:{}, 下一页：{}".format(name, dest))
