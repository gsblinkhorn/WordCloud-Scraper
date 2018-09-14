from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# transform string into wordcloud
stopwords = set(STOPWORDS)

with open('stopwords.txt') as f:
       for word in f.read().split():
              stopwords.add(word)

text = ""
with open('output.txt', 'r') as f:
        text = f.read()

wordcloud = WordCloud(stopwords=stopwords, 
			background_color="white", 
			max_words=100,
			width=800,
			height=600).generate(text)
wordcloud.to_file("wordcloud.png")
