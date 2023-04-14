from Words_list import lst_words
from random import randint

word = lst_words[randint(0, len(lst_words) - 1)]
# print(word)
print("It can be prase, wich isn't separated or one word")

attempts = 10


def guess_word():
    guess = input("Try to guess the word: ")
    return guess


for i in range(attempts):
    w = guess_word()
    if w == word:
        print(f"YEAH, it's: {word.upper()}")
        break
    elif i == 0 and w != word:
        print(f"Word starts with '{word[0]}'")
    elif i == 1 and w != word:
        print(f"Word ends with '{word[-1]}'")
    elif i == 2 and w != word:
        print(f"Word's length is: {len(word)}")
    elif i == 3 and w != word:
        letter = word[randint(1, len(word) - 2)]
        print(f"Tip: {word.index(letter) + 1} letter is '{letter}'")
    elif i == 4 and w != word:
        print(f"Try to guess {attempts - 5} times yet")
    elif 5 <= i < attempts - 1 and w != word:
        print(f"Wrong")
    else:
        print(f"You have used all attempts, word is: {word}")
        break
