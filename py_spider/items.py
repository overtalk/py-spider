# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DouBanMovieItem(Item):
    rank = Field()
    href = Field()
    name = Field()
    star = Field()
    quote = Field()
    actor = Field()
    director = Field()
    year = Field()
    region = Field()
    category = Field()
