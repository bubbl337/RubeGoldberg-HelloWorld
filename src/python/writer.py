import random


def txt_writer(words):
    f = open("text.txt", "w")
    f.writelines(words)
    f.close()


# ? All the letters of the word - "Hello World!!!"
letters = ["H", "E", "L", "O", "W", "R", "D", "!", " "]

word = (
    letters[0]
    + letters[1]
    + letters[2]
    + letters[2]
    + letters[3]
    + letters[8]
    + letters[4]
    + letters[3]
    + letters[5]
    + letters[2]
    + letters[6]
    + letters[7]
    + letters[7]
    + letters[7]
)

randomise = [word.lower(), word.upper(), word.title(), word.capitalize()]

words = random.choice(randomise)

txt_writer(words)