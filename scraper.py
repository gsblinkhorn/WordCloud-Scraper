from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests

main_link = 'https://www.careerbuilder.com/jobs'
keywords = 'software developer'
location = 'Atlanta, GA'

payload = {'keywords': keywords, 'location': location}
 
content = requests.get(main_link, params=payload).content
soup = BeautifulSoup(content.decode('utf-8'), features="html.parser")	

headers = soup.find_all("h2", "job-title")
links = []

for h2 in headers:
	a = h2.find("a")
	links.append(a.attrs['href'])
	
main_link = "https://www.careerbuilder.com"	
for link in links:
	print(link)
	url = main_link + link
	content = requests.get(url).content
	soup = BeautifulSoup(content.decode('utf-8'), features="html.parser")
	divs = soup.find_all("div", {"class": "description"})

	words_list = []  
	for i,div in enumerate(divs):
		if i % 2 == 0:
			continue
		elems = div.children
		words = " "
		for elem in elems:
			if isinstance(elem, NavigableString):
				continue
			else:
				words = words + elem.text.strip() + " "
		words = words.split()
		words_list.append(words)		
		print(len(words))
		
	

