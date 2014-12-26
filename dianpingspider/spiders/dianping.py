import scrapy
import MySQLdb
from selenium import webdriver
from selenium import selenium

from dianpingspider.items import DianpingspiderItem

class DianPingSpider(scrapy.Spider):
    name = "dianping"
    allowed_domains = ["dianping.com"]

    # def __init__(self):
    #     scrapy.Spider.__init__(self)
    #     self.verificationErrors = []
    #     self.selenium = selenium("localhost", 4444, "*firefox", "http://www.dianping.com")
    #     self.selenium.start()
    #
    # def __del__(self):
    #     self.selenium.stop()
    #     print self.verificationErrors
    #     scrapy.Spider.__del__(self)

    def start_requests(self):
        urls = []
        #conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="test",charset="utf8")
        #cursor = conn.cursor()
        #n = cursor.execute("select id from shop_info")
        #for row in cursor.fetchall():
        #    for r in row:
        #        url = 'http://www.dianping.com/shop/' + str(r)
        #        urls.append(url)
        #for url in urls:
        #    yield scrapy.Request(url,
        #        headers={'User-Agent': "cx"})
        #url = 'http://www.dianping.com/shop/536376/'
        download_delay = 2
        yield scrapy.Request('http://www.dianping.com/shop/536376',
                headers={'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14"})

    def parse(self, response):
        print response
        #webdriver = webdriver.PhantomJS()
        #driver.get(''http://www.dianping.com/shop/536376')
        #driver = webdriver.PhantomJS()
#        driver.get('http://www.dianping.com/shop/536376')

        item = DianpingspiderItem()
        item['title'] = ''.join(response.xpath('//div[@id="basic-info"]/h1/text()').extract()).replace('\n', '').replace(' ', '')
        item['address'] = ''.join(response.xpath('//*[@id="basic-info"]/div[2]/span[2]/@title').extract())
        item['rank'] = ''.join(response.xpath('//*[@id="basic-info"]/div[1]/span[1]/@title').extract())
        item['commit'] = ''.join(response.xpath('//*[@id="basic-info"]/div[1]/span[2]/text()').extract())
        item['average'] = ''.join(response.xpath('//*[@id="basic-info"]/div[1]/span[3]/text()').extract())
        item['delicious'] = ''.join(response.xpath('//*[@id="basic-info"]/div[1]/span[4]/text()').extract())
        item['env'] = ''.join(response.xpath('//*[@id="basic-info"]/div[1]/span[5]/text()').extract())
        item['srv'] = ''.join(response.xpath('//*[@id="basic-info"]/div[1]/span[6]/text()').extract())
        item['recommend'] = ''
        keywords = ''
 #       infos = driver.find_elements_by_xpath('//*[@id="shop-tabs"]/div[1]/p/a')
 #       for info in infos:
 #           keywords = keywords + info.text() + ''
 #       print keywords
        print item['title'], item['address'], item['rank'], item['commit'], item['average'], \
            item['delicious'], item['env'], item['srv'], item['recommend']
