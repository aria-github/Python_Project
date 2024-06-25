from random import choice
from csv import DictReader    # pake DictReader yah


# site = "http://quotes.toscrape.com"

 
def read_quotes(filename):
    with open(filename, "r", encoding="utf-8") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(quotes):

    quote = choice(quotes)

    remaining_guesses = 4

    print('')
    print(f'Here is a quote: {quote['text']}')
    #print(quote['text'])

    # print(quote['author'])

    guess = ''

    while guess.lower() != quote['author'].lower() and remaining_guesses > 0:

        guess = input('Who said this quote? Guesses remaining: {}\nanswer: '.format(remaining_guesses))

        if guess.lower() == quote['author'].lower() :
            print('YOU GOT IT RIGHT!')
            break

        remaining_guesses -= 1


        if remaining_guesses == 3 :
            print('')
            print("Here is a hint: the author was born on {}. {}".format(quote['born_location'], quote['born_date']))


        elif remaining_guesses == 2 :
            print('')
            print("Here is a hint: The author's first name starts with: {}".format(quote['author'][0]))

        elif remaining_guesses == 1 :
            print('')
            last_initial = quote['author'].split(' ')[1][0]
            print("Here is a hint: The author's last name starts with: {}".format(last_initial))

        else :
            print('')
            print("Sorry, you ran out of guesses. The answer was {}".format(quote['author']))



    again = ''
    while again.lower() not in ('yes', 'y', 'no', 'n'):
        again = input('Would you like to play again? (y/n)')

    if again.lower() in ('yes', 'y') :
        return start_game(quotes)

    else :
        print('Goodbye then')



quotes =  read_quotes("5.quotes.csv")

start_game(quotes)



# need csv file "5.quotes.csv"