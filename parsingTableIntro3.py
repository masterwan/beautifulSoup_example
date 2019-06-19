from bs4 import BeautifulSoup
import requests, csv


def get_html(url):
	return requests.Session().get(url).text

def write_csv(data, fileName):
	with open(fileName, 'a') as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerow(data)

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	for tr in soup.find(id="currencies").find('tbody').find_all('tr'):
		tds = tr.find_all('td')
		symbol = tds[1].find('span', class_='currency-symbol').text
		name = tds[1].find('a', class_='currency-name-container').text
		link = 'https://coinmarketcap.com{}'.format(tds[1].find('a').get('href'))
		price = tds[3].find('a', class_='price').get('data-usd')

		write_csv([symbol, name, link, price], 'cmc.csv')		





def main():
	html = get_html('https://coinmarketcap.com/')
	get_page_data(html)

if __name__ == '__main__':
	main()	