


from scrapy import Spider
from NationalParkVisitation.items import NationalparkvisitationItem

# for문 이름 
# for문 입장료 
# 이름, 입장료를 zip으로 묶어서 튜플로 되고 이거를 List에 넣음
# 만든 최종 리스트를 가지고 item에 넣어서 yield 




class NPVisitationSpider(Spider):
	name = "np_visitation_spider"
	allowed_urls = ['https://www.nps.gov']
	start_urls = ['https://www.nps.gov/aboutus/visitation-numbers.htm']

	def parse(self, response):
		part = response.xpath('//div[@class="table-wrapper"]')[1]
		item = part.xpath('./table//tr')

		print("##############")
		print(item)

		for i,v in enumerate(item):
			if(i==0):
				continue

			item = NationalparkvisitationItem()

			num = v.xpath('./td[1]//text()').extract_first()
			park_name=v.xpath('./td[2]//text()').extract_first()
			visits_number = v.xpath('./td[3]//text()').extract_first()

			item['num'] = num
			item['park_name'] = park_name
			item['visits_number'] = visits_number
			
			
			yield item

		'''
		park_name_list = []
		park_info_list = []
		
		#get park name list 
	
		for i,v in enumerate(part):
			print("i:",i)
			if(i==0):
				continue
			else:
				print("-"*30)
				#park_name= i.xpath('./h3/text()').getall()
				#park_name= i.xpath('./h3').getall()
				park_name= v.xpath('.//h3/text()').getall()
				#print(park_name)
				park_name_list.extend(park_name) 
				#print("="*30,"park_name_list","="*30)
				print(park_name_list, " np name count : " ,str(len(park_name_list)))

				#print("check value: ", v.xpath('./div[@class="table-wrapper"]/table//tr/td/b/text()'))

				#print("check value: ", v.xpath('./div[@class="table-wrapper"]/table').getall())

				info_per_park = v.xpath('./div[@class="table-wrapper"]/table')

				# per park
				for j in info_per_park:
					per_park_list = [];

					info_per_row = j.xpath('.//tr')
					# per row(time)
					for i2,k in enumerate(info_per_row):
						
						per_row_list = [];

						if(i2==0):
							continue

						time = k.xpath('.//td[1]//text()').extract_first()
						annual_pass=k.xpath('.//td[2]//text()').extract_first()
						per_vehicle = k.xpath('.//td[3]//text()').extract_first()
						per_person = k.xpath('.//td[4]//text()').extract_first()
						per_motorcycle = k.xpath('.//td[5]//text()').extract_first()

						per_row_list.append(time)
						per_row_list.append(annual_pass)
						per_row_list.append(per_vehicle)
						per_row_list.append(per_person)
						per_row_list.append(per_motorcycle)

						per_park_list.append(per_row_list)
						
						print("-per_row_list-: ", per_row_list)

					park_info_list.append(per_park_list)
					print("=per_park_list=: ", per_park_list)

				
				print("=park_info_list=: ", park_info_list, " np info count : " ,str(len(park_name_list)))
				
				item = BestbuyItem()
				item['user'] = user
				item['rating'] = rating
				item['title'] = title
				item['text'] = text
				item['helpful'] = helpful
				item['unhelpful'] = unhelpful
				item['product'] = product
				item['question'] = question

				yield item
			
				
			park_merge_info_list = [(i, j) for i, j in zip(park_name_list,park_info_list)]	
			print("="*30)
			print(park_merge_info_list)
			print("="*30)
			

			for z in park_merge_info_list:
				
				for y in z[1]:
				
					item = NPEntranceFeeItem()

					#print(y)
					#print(y[0])
					

					item['park_name'] = z[0]
					item['park_name'] = z[0]
					item['time'] = y[0]
					item['annual_pass'] = y[1]
					item['per_vehicle'] = y[2]
					item['per_person'] = y[3]
					item['per_motorcycle'] = y[4]
					
					yield item
					
				
			#print(i)


		
		
		
	   # rows.get_attribute("innerHTML")

		for row in rows[1:]:
			RDate = row.xpath('./td[2]/a/text()').extract_first()
			Title = row.xpath('./td[3]/b/a/text()').extract_first()
			PBudget = row.xpath('./td[4]/text()').extract_first()
			DomesticG = row.xpath('./td[5]/text()').extract_first()
			WorldwideG = row.xpath('./td[6]/text()').extract_first()

			item = BudgetItem()
			item['RDate'] = RDate
			item['Title'] = Title
			item['PBudget'] = PBudget
			item['DomesticG'] = DomesticG
			item['WorldwideG'] = WorldwideG

			yield item
		'''

# for문 이름 
# for문 입장료 
# 이름, 입장료를 zip으로 묶어서 튜플로 되고 이거를 List에 넣음
# 만든 최종 리스트를 가지고 item에 넣어서 yield 
