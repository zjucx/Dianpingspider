# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DianpingspiderPipeline(object):

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        self.file.write('aaaa')
        return item

    def __init__(self):
        self.file = open('dianping.json', 'wb')
        # self.file.write('aaaa')
