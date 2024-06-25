# scraping/download the quote and make guessing games from it
# the downside is everytime start the game , it will download the quote from web
# the upside is you will be always be updated
# sleep removed



import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice


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
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
    
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None

        # sleep(2)

    return all_quotes


def start_game(quotes):

    quote = choice(quotes)

    remaining_guesses = 4

    print('')
    print('Here is a quote: ')

    print(quote['text'])
    # print(quote['author'])	# enable this code to reveal the answer

    guess = ''


    while guess.lower() != quote['author'].lower() and remaining_guesses > 0:
        guess = input('Who said this quote? Guesses remaining: {}\n'.format(remaining_guesses))

        if guess.lower() == quote['author'].lower() :
            print('YOU GOT IT RIGHT!')
            break

        remaining_guesses -= 1


        if remaining_guesses == 3 :
            res = requests.get('{}{}'.format(base_url, quote['bio-link']))
            soup = BeautifulSoup(res.text, 'html.parser')
            birth_date = soup.find(class_='author-born-date').get_text()
            birth_place = soup.find(class_='author-born-location').get_text()
            print("Here is a hint: the author was born on {} {}".format(birth_date, birth_place))

        elif remaining_guesses == 2 :
            print("Here is a hint: The author's first name starts with: {}".format(quote['author'][0]))

        elif remaining_guesses == 1 :
            last_initial = quote['author'].split(' ')[1][0]
            print("Here is a hint: The author's last name starts with: {}".format(last_initial))

        else :
            print("Sorry, you ran out of guesses. The answer was {}".format(quote['author']))


    again = ''
    while again.lower() not in ('yes', 'y', 'no', 'n'):
        again = input('Would you like to play again? (y/n)')

    if again.lower() in ('yes', 'y') :
        return start_game(quotes)

    else :
        print('Goodbye then')



quotes =  scrape_quotes()

start_game(quotes)