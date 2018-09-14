from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

main_link = 'https://www.careerbuilder.com/jobs'
keywords = 'software developer'
location = 'Atlanta, GA'

payload = {'keywords': keywords, 'location': location}

content = requests.get(main_link, params=payload).content
soup = BeautifulSoup(content.decode('utf-8'), features="html.parser")

headers = soup.find_all("h2", {'class': ['job-title', 'show-for-medium-up']})
links = []

for h2 in headers:
	a = h2.find("a")
	links.append(a.attrs['href'])

links = set(links)
main_link = "https://www.careerbuilder.com"
words_list = []

for link in links:
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
		words_list.append(words)
		print(len(words))

text = ""
for word_list in words_list:
	for word in word_list:
		text = text + word + " "

wordcloud = WordCloud().generate(text)
wordcloud.to_file("wordcloud.png")
