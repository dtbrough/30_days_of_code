#!/bin/env python3

from functions import setup, display_information, get_information, user_input
import random


no_of_incorrect_guesses = 10


def main():
    user_input.greet_user()
    difficulty = user_input.ask_user_difficulty()
    # print(difficulty[1])
    # print(difficulty[0])
    word = get_information.get_random_word(difficulty[0], difficulty[1])
    word = word.rstrip()
    placeholder = setup.setup_hangman(word)
    print(''.join(placeholder))
    game = user_input.ask_user_guess(placeholder, word, no_of_incorrect_guesses)


if __name__ == "__main__":
    main()
