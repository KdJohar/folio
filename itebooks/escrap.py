import requests
from bs4 import BeautifulSoup as bs
import re
import string
from datetime import datetime
def slugify(s):
  
    s = s.lower()
    for c in [' ', '-', '.', '/']:
        s = s.replace(c, '_')
    s = re.sub('\W', '', s)
    s = s.replace('_', ' ')
    s = re.sub('\s+', ' ', s)
    s = s.strip()
    s = s.replace(' ', '-')
    return s


def getbook(url):

	payload = {}
	site = requests.get(url=url)
	print url
	soup = bs(site.content, "html.parser")
	title = soup.find('h1', attrs={'itemprop':'name'})
	payload['title'] = title.text
	des = soup.find('span', attrs={'itemprop':'description'})
	payload['description'] = des.text
	publisher = soup.find('a', attrs={'itemprop':'publisher'})
	payload['publisher'] = publisher.text
	author = soup.find('b', attrs={'itemprop':'author'})
	payload['author'] = author.text
	isbn = soup.find('b', attrs={'itemprop':'isbn'})
	isbntext = isbn.text.replace('-','')
	payload['isbn'] = isbntext
	image = soup.find('img', attrs={'itemprop':'image'})
	imagesrc = base_url+image['src']
	payload['image'] = imagesrc
	page = soup.find('b', attrs={'itemprop':'numberOfPages'})
	payload['pages'] = page.text
	language = soup.find('b', attrs={'itemprop':'inLanguage'})
	payload['language'] = language.text
	payload['slug'] = slugify(payload['title']+' '+payload['isbn'])
	try:
		download = soup.find('a', href=re.compile('http://filepi.com/*'))
		payload['download'] = download['href']
	except TypeError:
		payload['download'] = 'null'
	book_detail = requests.post(url='http://192.241.228.4/api/1/book/', data=payload)
	if book_detail.status_code == 400:
		error_log.write(url+'\n'+book_detail.text+'\n'+'-+'*20+'\n')
		print 'Error'
	elif book_detail.status_code == 201:
		print 'created'
		global book_detail_fetch
		book_detail_fetch = book_detail_fetch+1
	else:
		step_log.write(url+'\n')

def crawl(url):
	print url
	crawl_log.write(url+'\n')
	payload = {}
	site = requests.get(url)
	soup = bs(site.content, "html.parser")
	a = soup.find_all('a', href=re.compile('/book/*'))
	i = 0
	for links in a:
		i = i+1
		if i%2 == 0:
			link =  base_url+links['href']
			title = links.text
			payload['title'] = title
			payload['url'] = link
			book = requests.post(url='http://192.241.228.4/api/1/getbook/', data=payload)
			global total_books
			total_books = total_books +1
			if book.status_code == 400:
				pass
			elif book.status_code == 201:
				global book_fetch
				book_fetch = book_fetch+1
				getbook(link)

start_time = datetime.now()
base_url = 'http://it-ebooks.info'
book_fetch = 0
book_detail_fetch = 0
total_books = 0
book_log = open('/home/kd/itebooks/crawl_log/booklog.txt', 'w')
crawl_log = open('/home/kd/itebooks/crawl_log/crawllog.txt', 'w')
error_log = open('/home/kd/itebooks/crawl_log/errorlog.txt', 'w')
step_log = open('/home/kd/itebooks/crawl_log/steplog.txt', 'w')
for alphabet in string.lowercase[:27]:
	crawl_url = 'http://it-ebooks.info/%s'%alphabet		
	crawl(crawl_url)
crawl_url = 'http://it-ebooks.info/1'
crawl(crawl_url)
book_log.write('Total books fetched today - '+str(total_books)+'\n')
book_log.write('Total new books fetched today - '+str(book_fetch)+'\n')
book_log.write('Total new books details fetched today - '+str(book_detail_fetch)+'\n')
end_time = datetime.now()
total_time = 'Duration: {}'.format(end_time-start_time)
book_log.write(total_time)
book_log.close()
crawl_log.close()
error_log.close()
step_log.close()
print 'Done'
