# -*- coding: utf-8 -*-
import scrapy


class Spider(scrapy.Spider):
    name = 'ip'
    allowed_domains = []

    def start_requests(self):
        url = 'http://myip.ipip.net/'

        for i in range(4):
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        print(response.text)
        print(response.request.headers['User-Agent'])
