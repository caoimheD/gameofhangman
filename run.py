# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from data import words

def get_word(words):
    word = random.choice(words)

    return word

def thegame():
    letters = set(word)
    used_letters = set()

    


player_input = input('pick a letter')
print(player_input)

get_word(words)
