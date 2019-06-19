import requests, csv

from multiprocessing import Pool
#from multiprocessing import Process

from time import sleep


def get_html(url):
	return requests.get(url).text



def write_csv(data):
	with open('sites.csv', 'a') as file:
		order = ['name', 'url', 'description', 'traffic', 'percent']
		writer = csv.DictWriter(file, fieldnames=order)
		writer.writerow(data)


def get_page_data(text):
		data = text.strip().split('\n')[1:]

		for row in data:
			pass
			columns = row.strip().split('\t')
			name = columns[0]
			url = columns[1]
			description = columns[2]
			traffic = columns[3]
			percent = columns[4]

			data = {'name': name,
			        'url': url,
			        'description': description,
			        'traffic': traffic,
			        'percent': percent}
			write_csv(data)

def make_all(url):
	text = get_html(url)
	get_page_data(text)


def main():
	url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'
	urls = [url.format(i) for i in range(0, 7950)]
	#print(urls)
	
	with Pool(200) as p:
		p.map(make_all, urls)
		sleep(1)



if __name__ == '__main__':
	main()			

