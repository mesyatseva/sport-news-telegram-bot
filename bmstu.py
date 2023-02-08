import requests


def print_response():
	response = requests.get('https://bitop.bmstu.ru/schedule/1')
	print(response)
	print(response.json())


if __name__ == '__main__':
	print_response()