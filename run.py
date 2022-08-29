# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from data import words

def thegame():
    word = random.choice(words)
    turns = 10
    playerguess = ''
    validchoices = set('abcdefhijklmnopqrstuvwxyz')

    while len(word) > 0:
        random_word = ''

        for letter in word:
            if letter in playerguess:
                random_word = random_word + letter
            else:
                random_word = random_word + "_ "
        
        if random_word == word:
            print(random_word)
            print("you guessed the word!")
            break

        print("Guess the word! ", random_word)
        guess = input()

        if guess in validchoices:
           playerguess = playerguess + guess
        else:
            print('enter a valid character')
            guess = input()

        if guess not in word:
            turns = turns - 1
        if turns == 0:
            print('game over')
            break


getname = input('Enter your name: ')
print('Hi', getname,'!')
print('try to guess the word, 10 attempts')

thegame()
