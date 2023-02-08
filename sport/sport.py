import requests
from bs4 import BeautifulSoup

SPORTS_RU_URL = 'https://www.sports.ru/'
SPORTS_RU_FOOTBALL_URL = 'https://www.sports.ru/football/news/'
SPORTS_RU_HOCKEY_URL = 'https://www.sports.ru/hockey/news/'


def sports_ru_football():
	url = SPORTS_RU_FOOTBALL_URL
	response = requests.get(url)
	bs = BeautifulSoup(response.text, "lxml")
	news_list = bs.find_all('a', 'short-text')[:10]
	news_dict = {}
	for news in news_list:
		url = str(news).split('href="', 1)[1]
		url = str(url).split('" title', 1)[0]
		news_dict[news.text] = SPORTS_RU_URL + url
	return news_dict


def sports_ru_hockey():
	url = SPORTS_RU_HOCKEY_URL
	response = requests.get(url)
	bs = BeautifulSoup(response.text, "lxml")
	news_list = bs.find_all('a', 'short-text')[:10]
	news_dict = {}
	for news in news_list:
		url = str(news).split('href="', 1)[1]
		url = str(url).split('" title', 1)[0]
		news_dict[news.text] = SPORTS_RU_URL + url
	return news_dict
