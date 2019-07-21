from scrapy import Spider, Request
from npwiki.items import NpwikiItem
import re

class NpwikiSpider(Spider):
	name = 'npwiki_spider'
	allowed_urls = ['https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States']
	start_urls = ['https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States']

	def parse(self, response):
		rows = response.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr')
		print(rows.getall())
		for i, row in enumerate(rows):
			if i<1:
				continue
			name = row.xpath('.//*/a/text()').extract_first()
			visitor_temp = row.xpath('./td[5]/text()').extract_first()
			visitor = row.xpath('./td[6]/text()').extract_first()

			item = NpwikiItem()
			item['name'] = name
			#print(visitor)
			if visitor[0].isdecimal():
				item['visitor'] = visitor.strip()
			else:
				item['visitor'] = visitor_temp.strip()

			yield item
