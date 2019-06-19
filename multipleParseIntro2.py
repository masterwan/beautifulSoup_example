from bs4 import BeautifulSoup
import requests, csv, os


def get_html(url):
	return requests.Session().get(url).text

def write_csv(data):
	if not os.path.exists('./plugins.csv'):
		create_header = True
	else:
		create_header = False

	with open('./plugins.csv','a') as f:
		writer = csv.writer(f)
		if create_header:
			writer.writerow(('title', 'link', 'rating', 'content'))
		writer.writerow((data['title'], data['link'], data['rating'], data['content']))	

def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	result = soup.findAll(class_='plugin-section')[1]
	articles = result.findAll(class_='plugin-card')
	lsts = []
	for article in articles:
		title = article.find(class_='entry-title').text
		link = article.find(class_='entry-title').find('a').get('href') #.attrs['href'] #['href']
		article.find(class_='screen-reader-text').decompose()
		rating = article.find(class_='rating-count').find('a').text.replace(',', '.')
		content = article.find(class_='entry-excerpt').text
		data = {
			'title': title,
			'link': link,
			'rating': rating,
			'content': content,
		}
		write_csv(data)


def main():
	url = 'https://wordpress.org/plugins/'
	html = get_html(url)
	print(get_data(html))


if __name__ == '__main__':
	main()