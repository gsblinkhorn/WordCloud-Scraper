from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# get-request with keywords and location arguments
main_link = 'https://www.careerbuilder.com/jobs'
keywords = 'software developer'
location = 'Atlanta, GA'

payload = {'keywords': keywords, 'location': location}

content = requests.get(main_link, params=payload).content
soup = BeautifulSoup(content.decode('utf-8'), features="html.parser")

# get each job posting
headers = soup.find_all("h2", {'class': ['job-title', 'show-for-medium-up']})
links = []

# find the url in each posting
for h2 in headers:
	a = h2.find("a")
	links.append(a.attrs['href'])

# eleiminate duplicate links
links = set(links)
main_link = "https://www.careerbuilder.com"
text = ""

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

# transform string into wordcloud
stopwords = set(STOPWORDS)
with open('stopwords.txt') as f:
	for word in f.read().split():
		stopwords.add(word)

wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=50).generate(text)
wordcloud.to_file("wordcloud.png")
