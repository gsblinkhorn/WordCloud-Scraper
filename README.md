# WordCloud-Scraper
Scrapes careerbuilder.com for job postings and generates a Word Cloud of the contents of those postings. 

## Scraper.py
This script will scrape every job posting returned by the {keywords, location} query and output every word into a file
named output.txt. The postings retrieved can be modified by changing the keywords and location variables in the scraper.py script.

## Generate_wc.py
This script opens the output.txt file and feeds its contents to the WordCloud module. 
It also reads stopwords in from the stopwords.txt file to prevent them from being shown in the Word Cloud. This allows the user to refine the Word Cloud to drop common words that aren't particularly descriptive. 
The Word Cloud image is saved to the working directory as wordcloud.png

## Example
Given the query below, careerbuilder.com returns ~300 job listings. The scraper reads each of these listings in generating its output.txt document. By using this tool, you can get a visualization of what employers are looking for for certain positions.
### Keywords: software developer
### Location: Atlanta, GA

<p align="center">
  <img src="wordcloud.png">
</p>
