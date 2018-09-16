from bs4 import BeautifulSoup, NavigableString
import requests

# get-request with keywords and location arguments
main_link = 'https://www.careerbuilder.com/jobs'
keywords = 'registered nurse'
location = 'New York, NY'

payload = {'keywords': keywords, 'location': location}

content = requests.get(main_link, params=payload)
content = content.content.decode('utf-8')

soup = BeautifulSoup(content, features="html.parser")

# get each job posting
headers = soup.find_all("h2", {'class': ['job-title', 'show-for-medium-up']})
links = []

# find the url in each posting
for h2 in headers:
	a = h2.find("a")
	links.append(a.attrs['href'])

# get list of secondary urls
div = soup.find_all("div", {'class' : ['pager']})
url_prefix = ""
max_num = 0
for d in div:
	a_tags = d.find_all("a")
	for i,a in enumerate(a_tags):
		if i == 1:
			url_prefix = a.attrs['href']
		if i == 6:
			max_num = int(str(a.string.strip()))

secondary_urls = []
for index in range(2,max_num+1):
	secondary_urls.append(url_prefix + "?page_number=" + str(index))
	
for url in secondary_urls:
	print(url)
	content = requests.get(url).content.decode('utf-8')
	soup = BeautifulSoup(content, features="html.parser")
	headers = soup.find_all("h2", {"class": ["job-title", "show-for-medium-up"]})
	
	for h2 in headers:
		a = h2.find("a")
		links.append(a.attrs['href'])

main_link = "https://www.careerbuilder.com"
text = ""
links = set(links)
# scrap each link for content
for i, link in enumerate(links):
	print("Scraping Link " + str(i))
	url = main_link + link
	content = requests.get(url).content
	soup = BeautifulSoup(content.decode('utf-8'), features="html.parser")
	divs = soup.find_all("div", {"class": "description"})

	for i,div in enumerate(divs):
		elems = div.children
		words = " "
		for elem in elems:
			if isinstance(elem, NavigableString):
				continue
			else:
				words = words + elem.text.strip() + " "
		words = words.split()
		for word in words:
			text = text + word + " "

with open("output.txt", "w") as f:
	f.write(text)

