from bs4 import BeautifulSoup
import requests

def get_html(url):
	response = requests.Session().get(url)
	if response.ok: return response.text
	else: return response.status_code	 

def get_data(url):
	html = get_html(url)
	if html == 404: return '404 - not found'
	soup = BeautifulSoup(html, 'lxml')
	data = soup.find(id='home-welcome').find('header').find('h1').text
	return data

def main():
	url = 'https://wordpress.org/q'
	print(get_data(url)) 


if __name__ == '__main__':
	main()