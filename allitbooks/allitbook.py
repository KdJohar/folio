import requests
from bs4 import BeautifulSoup
import re
import json
import urllib2
import os
from datetime import datetime

def soupsite(url):
	data = requests.get(url)
	soup = BeautifulSoup(data.content, "html.parser")
	return soup

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

def book_crawl(url):
	print url
	payload = {}
	'''
	site = requests.get(url=url)
	print url
	soup = bs(site.content, "html.parser")
	'''
	soup = soupsite(url)
	title = soup.find('h1', attrs={'class':'single-title'})
	payload['title'] = title.text
	desc_div = soup.find('div', attrs={'class':'entry-content'})
	description = desc_div.text.split(':')
	description = description[1]
	payload['description'] = description.replace('\n', '').replace('\u', '')
	download_div = soup.find('span', attrs={'class':'download-links'})
	payload['download'] = download_div.a['href'].replace(' ','%20')
	div_image = soup.find('div', attrs={'class':'entry-body-thumbnail hover-thumb'})
	image =  div_image.find('img')
	obj_image = image['src']
	if obj_image.find('x'):
		no = obj_image.find('x')
		start = no-4
		end = no+4
		obj_image = obj_image.replace(obj_image[start:end], '')
	payload['image'] = obj_image

	div = soup.findAll('dd')
	i = 0
	for content in div:
		i += 1
		if i == 1:
			author = content.text
			payload['author'] = author
		if i == 2:
			isbn = content.text
			if isbn.find('-'):
				isbn = isbn.replace('-', '').replace(' ', '')
			payload['isbn'] = isbn

		if i == 4:
			pages = content.text
			payload['pages'] =  pages.replace(' ', '')
		if i == 5:
			language = content.text
			payload['language'] = language.replace(' ', '')


	
	payload['slug'] = slugify(payload['title']+' '+payload['isbn'])
	
	#book_detail = requests.post(url='http://127.0.0.1:8000/api/1/book/', data=payload)
	book_detail = requests.post(url='http://folio.co.in/api/1/book/', data=payload)

	print book_detail
	if book_detail.status_code == 400:
		book_error_log.write('Error 400:'+'\n')
		book_error_log.write(book_detail.text+'\n')
		book_error_log.write('-+'*10+'\n')
	elif book_detail.status_code == 201:
		print 'created'
	elif book_detail.status_code == 500:
		book_error_log.write('Error 500:'+'\n')
		book_error_log.write(book_detail.text+'\n')
		book_error_log.write('-+'*10+'\n')
		

def crawl(page):
		url = 'http://www.allitebooks.com/page/%s'%page
		print url
		soup = soupsite(url)
		i = 0
		payload = {}
		for a in soup.findAll('a', attrs={'rel':'bookmark'}):
			i += 1
			if i % 2 == 0:
				url = a['href']
				payload['url'] =  url
				payload['title'] =  a.text

				#book_post = requests.post(url='http://127.0.0.1:8000/api/1/getbook/', data=payload)
				book_post = requests.post(url='http://folio.co.in/api/1/getbook/', data=payload)

				if book_post.status_code == 400:
					get_book_error_log.write('Error 400:'+'\n')
					get_book_error_log.write(book_post.text+'\n')
					get_book_error_log.write('-+'*10+'\n')
					print payload['url']
				elif book_post.status_code == 500:
					get_book_error_log.write('Error 500:'+'\n')
					get_book_error_log.write(book_post.text+'\n')
					get_book_error_log.write('-+'*10+'\n')
					print payload['url']
				elif book_post.status_code == 201:
					print 'going'
					global total_books
					total_books += 1
					book_crawl(url)
start_time = datetime.now()
initial_soup = soupsite('http://www.allitebooks.com/')
total_pages = initial_soup.find('a', attrs={'title': re.compile('Last Page *')})
total_pages = int(total_pages.text)
total_books = 0
script_path = os.path.dirname(os.path.abspath(__file__))
crawl_log = open(script_path+'/crawl.txt', 'w')
get_book_error_log = open(script_path+'/get_book_error.txt', 'w')
book_error_log = open(script_path+'/book_error.txt', 'w')
book_log = open(script_path+'/book.txt', 'w')
for page in range(1, 7):
	crawl(page)
	crawl_log.write(str(page)+'\n')
book_log.write('Total books fetched today - '+str(total_books)+'\n')
crawl_log.close()
get_book_error_log.close()
book_error_log.close()
end_time = datetime.now()
total_time = 'Duration: {}'.format(end_time - start_time)
book_log.write(total_time)
book_log.close()
print 'Done'
