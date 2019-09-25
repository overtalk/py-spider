# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .items import DouBanMovieItem


class DouBanMoviePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, DouBanMovieItem):
            pass
        return item

