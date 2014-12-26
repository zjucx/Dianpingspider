# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DianpingspiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    address = scrapy.Field()
    phoneNum = scrapy.Field()
    rank = scrapy.Field()
    commit = scrapy.Field()
    average = scrapy.Field()
    delicious = scrapy.Field()
    env = scrapy.Field()
    srv = scrapy.Field()
    recommend = scrapy.Field()
    pass
