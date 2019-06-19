from bs4 import BeautifulSoup
import requests, csv, os, re

def _get_html(url):
	try:
		response = requests.Session().get(url)
		if response.ok: return response.text
		else: return response.status_code
	except: 
		exit('error open url')	

def _write_row_csv(data, fileName):
	try:
		with open(fileName, 'a') as f:
			writer = csv.writer(f)
			writer.writerow(data)
	except:
		exit('error write csv')	

def _delete_csv_file(fileName):
	if os.path.exists(fileName):
		try:
  			os.remove(fileName)
		except:
  			exit('error delete csv file')
	else: return 'file does not exist'

def _get_page_data(url, fileCsvName):
	html = _get_html(url)
	soup = BeautifulSoup(html, 'lxml')
	for tr in soup.find(id='currencies').find('tbody').findAll('tr'):
		td = tr.findAll('td')
		try:
			title = td[1].find('a', {'class': 'currency-name-container'}).text.strip()
		except:
			title = ''
		try:
			link = td[1].find(class_='currency-name-container').get('href').strip()
		except:
			link = ''
		try:
			price = td[3].find(attrs={'class': 'price'}).get('data-usd').strip()
		except:
			price = ''
		_write_row_csv([title, link, price], 'page_coin.csv')
	return True

def get_pages_data(url, fileCsvName):
	_delete_csv_file(fileCsvName)
	while True:
		_get_page_data(url, fileCsvName)
		html = _get_html(url)
		soup = BeautifulSoup(html, 'lxml')
		try:
			page = soup.find(class_='top-paginator').find('a',text=re.compile('[N|n]ext 100')).get('href')
		except:
			break
		else:
			url = _raw_url(url)+'/'+str(page)

def _raw_url(url):
	raw_url_list = url.split('/')
	if(len(raw_url_list) == 4):
		raw_url_list.pop()
		url =  ('/').join(raw_url_list)
	return url


def main():
	url = 'https://coinmarketcap.com/'
	file_name = 'page_coin.csv'
	get_pages_data(url, file_name)

if __name__ == '__main__':
	main()



