import random

words = ["train", "steak", "finds"]

def pick_word():
    pick = random.randint(0, len(words))
    word = words[pick]
    return word


def guess():
    word = pick_word()
    word_split = list(word)
    print(word)
    while True:
        guess = input("guess: ")
        guess_split = list(guess)
        if len(guess_split) == 5:
            if guess_split == word_split:
                break
            for i in range(5):
                if guess_split[i] == word_split[i]:
                    print(guess_split[i], " is correct")
                elif guess_split[i] in word_split:
                    print(guess_split[i], "differnt position")
        else:
            print("5 letter word")
    print("You winnnnnnn")

guess()