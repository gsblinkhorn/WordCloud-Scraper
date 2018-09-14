import bs4
import requests

def main():
	link = "https://www.indeed.com/"
	response = requests.get(link)

 if __name__ == "__main__":
	main()
