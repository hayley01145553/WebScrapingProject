# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NPEntranceFeeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    park_name = scrapy.Field()
    time = scrapy.Field()
    annual_pass = scrapy.Field()
    per_vehicle = scrapy.Field()
    per_person = scrapy.Field()
    per_motorcycle = scrapy.Field()
    
