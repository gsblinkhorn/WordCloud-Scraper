# WordCloud-Scraper
Scrapes careerbuilder.com for job postings and generates a Word Cloud of the contents of those postings. 

## Scraper.py
This script will scrape every job posted returned by the {keywords, location} query and output every word into a file
named output.txt. The postings retrieved can be modified by changing the keywords and location variables in the scraper.py script.

## Generate_wc.py
This script opens the output.txt file and feeds its contents to the WordCloud module. The Word Cloud image is saved to the
working directory as wordcloud.png

## Example
### Keywords: software developer
### Location: Atlanta, GA

<p align="center">
  <img src="wordcloud.png">
</p>
