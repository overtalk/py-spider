# -*- coding: utf-8 -*-
from scrapy import Spider, Request, Selector
from ..items import DouBanMovieItem


class DouBanSpider(Spider):
    name = 'douban'
    base_url = 'https://movie.douban.com/top250'
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 '
                      'Safari/537.36'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse, headers=self.header)

    def parse(self, response):
        selector = Selector(response)
        # get all movies
        for item in self.__parse_detail(selector):
            yield item
        # parse next url
        url = self.__next_url(selector)
        if url is not None:
            yield Request(url=url, callback=self.parse, headers=self.header)

    def __parse_detail(self, selector):
        items = []
        movies = selector.xpath('//div[@class="item"]')
        for movie in movies:
            items.append(self.__parse_one(movie))
        return items

    def __parse_one(self, movie):
        item = DouBanMovieItem()
        item["name"] = movie.xpath('div[@class="info"]/div[@class="hd"]/a/span/text()').extract_first()
        item["star"] = movie.xpath(
            'div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract_first()
        item["quote"] = movie.xpath(
            'div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract_first()
        return item

    def __next_url(self, selector):
        url = selector.xpath('//span[@class="next"]/a/@href').extract_first()
        if url is None:
            return None
        return self.base_url + url


