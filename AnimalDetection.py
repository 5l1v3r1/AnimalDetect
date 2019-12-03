from aip import AipImageClassify
import json
from pprint import pprint
with open('config.json','r') as f:
	data = json.load(f)
APP_ID = data['appId']
API_KEY = data['apiKey']
SECRET_KEY = data['secretKey']

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
# print('starting...')
class Animal(object):
	def __init__(self,fn,client=client):
		self.image = self.get_file_content(str(fn))
		self.status = 1
		if self.image == None:
			self.status = 0
		self.client = client

	def get_file_content(self,filePath):
		# print('yay!')
		try:
			with open(filePath, 'rb') as fp:
				# print('yay!')
				return fp.read()
		except:
			# print('oh no!')
			return None

	def isAnimal(self):
		if self.image != None:
			# print('loading...')
			options = {}
			options['top_num'] = 2
			result = self.client.animalDetect(self.image,options)['result']
			# pprint(result)
			if result[0]['name'] == '非动物':
				return False
			else:
				return True
# animal = Animal('IMG_0648.jpeg')