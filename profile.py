import pandas as pd
from time import time
import json


class Profile:
	def __init__(self, data_list):
		self._data_list = data_list

	def to_csv(self, file_name=''):
		if not file_name:
			file_name = f'cat{int(time())}.csv'
		pd.DataFrame(self._data_list).to_csv(file_name, index=False)

	def to_json(self, file_name=''):
		if not file_name:
			file_name = f'cat{int(time())}.json'
		with open(file_name, 'w') as file:
			json.dump(self._data_list, file, ensure_ascii=False, indent=4)
