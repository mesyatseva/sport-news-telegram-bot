import requests
from bs4 import BeautifulSoup


def show_tempertaure_moscow():
	url = 'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526'
	response = requests.get(url)
	bs = BeautifulSoup(response.text,"lxml")
	temp = bs.find_all('span', 'temp__value temp__value_with-unit').__getitem__(1)
	return temp.text
