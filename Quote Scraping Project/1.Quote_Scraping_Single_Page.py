# http://quotes.toscrape.com
# scraping quote by text, author, and bio-link
# scraping only 1 page , find next page button not added yet
# next_btn = soup.find(class_="next")


import requests
from bs4 import BeautifulSoup

all_quotes = []
res = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(res.text , features="html.parser")
quotes = soup.find_all(class_="quote")


for quote in quotes:
	all_quotes.append({
		"text":quote.find(class_="text").get_text(),
		"author":quote.find(class_="author").get_text(),
		"bio-link": quote.find("a")["href"]
		})

print(all_quotes)


# result :
# [{'text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'author': 'Albert Einstein', 'bio-link': '/author/Albert-Einstein'},   {'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', 'author': 'J.K. Rowling', 'bio-link': '/author/J-K-Rowling'},  ...]


