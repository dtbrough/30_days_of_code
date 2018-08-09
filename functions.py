
import requests
import json
import credentials
from random import randint
import linecache


class setup:
    '''Class for holding functions related to the setup of games.'''
    def setup_hangman(word):
        '''Function to setup the dash table indicating letter placeholders'''
        placeholder = []

        for i in word:
            placeholder.append('-')
        return placeholder


class display_information:
    '''Class for holding functions that display information and instruction to
    the user'''
    def placeholder():
        '''Just a placeholder'''
        pass


class get_information:
    '''Class for functions that seek information to be used at a later date.'''
    def get_random_word(min_length, max_length):
        '''Fetch a random word from text file.'''
        word_file = 'words.txt'
        min_length = int(min_length)
        max_length = int(max_length)
        word = ' '

        with open(word_file, 'r') as words:
            count = 0
            for line in words:
                count += 1

            while (len(word) < min_length) or (len(word) > max_length):
                word_id = randint(0, count)
                word = linecache.getline(word_file, word_id)
        return word

    def get_word_definition(word):
        '''Retrieve word definition from oxford dictionary api'''
        app_id = credentials.app_id
        app_key = credentials.app_key

        language = 'en'
        word_id = word

        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

        print("code {}\n".format(r.status_code))
        print("text \n" + r.text)
        print("json \n" + json.dumps(r.json()))
        return r


class user_input:
    '''Class for functions that asks the user for input and interaction.'''
    def greet_user():
        '''Asks the user for their name and displays the greeting message.'''
        answer = input('What is your name? ')
        print('Welcome to the game ' + answer + ".\n")
        return

    def ask_user_guess(placeholder, word, no_of_incorrect_guesses):
        '''Asks user to guess a letter.'''
        count = 0
        word = word.lower()
        no_of_guesses = len(word) + no_of_incorrect_guesses

        while ((count < no_of_guesses) and (list(word) != placeholder)):
            guess = input('Guess a letter: ').lower()
            count += 1
            for i in range(len(word)):
                if guess == word[i]:
                    print('That guess is correct...')
                    placeholder[i] = guess
                    print(''.join(placeholder))
        if count >= no_of_guesses:
            print('You have run out of guesses. The word was: ' + word)
        else:
            print('You have guessed correctly. The word was: ' + word)

    def ask_user_difficulty():
        '''Asks the user for desired difficulty. Easy words have less
        characters. Harder words are longer.'''
        answer = input('Would you like the game to be (E)asy or (H)ard? ')

        if answer.upper() == 'E':
            difficulty = [int(3), int(6), 'Easy']
        elif answer.upper() == 'H':
            difficulty = [int(6), int(16), 'Hard']
        else:
            print('You entered an invalid value.')
        return difficulty
