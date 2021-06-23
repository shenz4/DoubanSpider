# -*- coding: utf-8 -*-

# Scrapy settings for DoubanCommentsSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DoubanCommentsSpider'

SPIDER_MODULES = ['DoubanCommentsSpider.spiders']
NEWSPIDER_MODULE = 'DoubanCommentsSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
COOKIE = {'bid': 'vvLSLeePh4I', 'douban-fav-remind': '1', 'll': '"108309"', '_vwo_uuid_v2': 'DD814E23D74944471DC49829AF9835583|1dde29d17d1a69101c950a67cf7c9fd9', 'gr_user_id': 'fe1055a2-6077-4b69-9299-103b60106eb8', 'ap': '1', 'ct': 'y', 'ps': 'y', 'push_noty_num': '0', 'push_doumail_num': '0', '__utmv': '30149280.16159', '_ga': 'GA1.2.2020885756.1532170542', '__utmc': '30149280', '__utmz': '30149280.1532565521.22.13.utmcsr', '_gid': 'GA1.2.1389278603.1532568950', '__utma': '30149280.2020885756.1532170542.1532565521.1532571690.23', '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1532572321%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D', '_pk_ses.100001.8cb4': '*', '__utmt': '1', '_gat_UA-7019765-1': '1', '_pk_id.100001.8cb4': '4e6d7a4453b62cbb.1532170538.14.1532572367.1532568946.', '__utmb': '30149280.8.10.1532571690'}

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'Connection': 'keep - alive',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'DoubanCommentsSpider.middlewares.DoubancommentsspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'DoubanCommentsSpider.middlewares.DoubancommentsspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'DoubanCommentsSpider.pipelines.DoubancommentsspiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
