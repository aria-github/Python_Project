import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter    # pake DictWriter yah
 

base_url = "http://quotes.toscrape.com"

 
def scrape_quotes():

    all_quotes = []
    url = "/page/1"
 
    while url:
        res = requests.get(f"{base_url}{url}")
        print(f"Now Scraping {base_url}{url}....")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        
        for quote in quotes:
            #print(scrape_bio(quote.find("a")["href"])[0])
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"],
                "born_date": scrape_bio(quote.find("a")["href"])[0],
		"born_location": scrape_bio(quote.find("a")["href"])[1]
            })
    
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None

        # sleep(2)

    return all_quotes



def scrape_bio(bio_link):

    res_bio = requests.get(f"{base_url}{bio_link}")
    soup = BeautifulSoup(res_bio.text, "html.parser")
    born_date = soup.select(".author-born-date")[0].get_text()
    born_location = soup.select(".author-born-location")[0].get_text()
    
    return [born_date, born_location]



def write_quotes(quotes):

    with open("quotes.csv", "w", encoding="utf-8") as file:
        headers = ["text", "author", "bio-link", "born_date", "born_location"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()

        for quote in quotes:
            csv_writer.writerow(quote)


quotes = scrape_quotes()

write_quotes(quotes)



# kalo gak ada encoding="utf-8" , bakal error
# 'charmap' codec can't encode character '\u2032' in position 1: character maps to <undefined>
