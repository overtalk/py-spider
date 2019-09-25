# -*- coding: utf-8 -*-
import scrapy


class Spider(scrapy.Spider):
    name = 'ip'
    allowed_domains = []

    def start_requests(self):
        url = 'https://ip.tool.chinaz.com'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        selector = scrapy.Selector(response)
        ip = selector.xpath('//dl[@class="IpMRig-tit"]/dd[@class="fz24"]/text()').extract_first()
        print("ip 地址为 ---> ", ip)
