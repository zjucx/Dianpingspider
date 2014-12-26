# -*- coding: utf-8 -*-

# Scrapy settings for dianpingspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'dianpingspider'

SPIDER_MODULES = ['dianpingspider.spiders']
NEWSPIDER_MODULE = 'dianpingspider.spiders'
COOKIES_ENABLES = False

ITEM_PIPELINES = {
    'dianpingspider.pipelines.DianpingspiderPipeline': 300
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dianpingspider (+http://www.yourdomain.com)'
