from pprint import pprint as print
from bs4 import BeautifulSoup
import requests

def get_html(url):
	return requests.Session().get(url).text


soup = BeautifulSoup(get_html('https://onliner.by'), 'lxml')

if soup.find('p'):
	result = soup.find('p').text

print(result)