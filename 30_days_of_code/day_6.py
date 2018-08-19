
cases = input()
word_list = []
word_length = []


def get_inputs():
    for i in range(0, int(cases)):
        word = input()
        word_list.append(word)
        word_length.append(len(word))


def split_characters():
    for word in word_list:
        evens = []
        odds = []
        for i in range(0, len(word)):
            if (i % 2) == 0:  # Even numbers
                evens.append(word[i])
            elif (i % 2) != 0:  # Odd numbers
                odds.append(word[i])

        evens = ''.join(evens)
        odds = ''.join(odds)
        print(evens, odds)


get_inputs()
split_characters()
