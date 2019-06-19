from bs4 import BeautifulSoup
import requests, json, time
from pprint import pprint as print

def get_html(url):
	return requests.Session().get(url).text

def get_page(url):
	html = get_html(url)
	soup = BeautifulSoup(html, 'lxml')
	pages = soup.findAll(class_='adm-nav-page')[-3].text
	return pages

def get_data(url):
	pages = get_page(url)
	items_box = []
	for page in range(1,int(pages)+1):
		html = get_html(url+str(page))
		soup = BeautifulSoup(html, 'lxml')
		for item in soup.findAll('div', attrs={"itemprop": "itemListElement"}):
			title = item.find(class_='item-title').text
			link = item.find(class_='item-title').get('href')
			price = item.find(attrs={"itemprop":"price"}).get('content')
			items_box.append({'title': title, 'link': link, 'price': price})
	return items_box	

def write_json(data, fileName):
	with open(fileName, 'w', encoding='utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent=2)	

def main():
	url = 'https://mamashop.by/catalog/3406/?PAGEN_1='
	products = get_data(url)
	write_json(products, './products.json')

if __name__ == '__main__':
	main()


	
		