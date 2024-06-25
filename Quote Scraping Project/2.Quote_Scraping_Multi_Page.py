# http://quotes.toscrape.com
# scraping quote by text, author, and bio-link
# multiple page scraping
# put sleep , unless you want your ip banned by bot


import requests
from bs4 import BeautifulSoup
from time import sleep


all_quotes = []
base_url = "http://quotes.toscrape.com"
url = "/page/1/"


while url:

	res = requests.get(f"{base_url}{url}")
	print(f"Now Scraping {base_url}{url}")

	# print(base_url) # http://quotes.toscrape.com
	# print(url)      # /page/1/ , /page/2/ , /page/3/ , etc

        # {base_url}{url} =  "http://quotes.toscrape.com" + "/page/1/" ,
        # {base_url}{url} =  "http://quotes.toscrape.com" + "/page/2/" , 
        # etc

	soup = BeautifulSoup(res.text , features="html.parser")
	quotes = soup.find_all(class_="quote")


	for quote in quotes:
		all_quotes.append({
			"text":quote.find(class_="text").get_text(),
			"author":quote.find(class_="author").get_text(),
			"bio-link": quote.find("a")["href"]
			})

	next_btn = soup.find(class_="next")
	url = next_btn.find("a")["href"] if next_btn else None

	sleep(2)
	# sleep 2 seconds


print(all_quotes)



# result :

# Now Scraping http://quotes.toscrape.com/page/1/
# Now Scraping http://quotes.toscrape.com/page/2/
# Now Scraping http://quotes.toscrape.com/page/3/
# Now Scraping http://quotes.toscrape.com/page/4/
# Now Scraping http://quotes.toscrape.com/page/5/
# Now Scraping http://quotes.toscrape.com/page/6/
# Now Scraping http://quotes.toscrape.com/page/7/
# Now Scraping http://quotes.toscrape.com/page/8/
# Now Scraping http://quotes.toscrape.com/page/9/
# Now Scraping http://quotes.toscrape.com/page/10/

# [{'text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'author': 'Albert Einstein', 'bio-link': '/author/Albert-Einstein'}, {'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', 'author': 'J.K. Rowling', 'bio-link': '/author/J-K-Rowling'}, ...]