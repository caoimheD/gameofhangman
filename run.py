import random

# importing and initializing colorama, for colour text
from colorama import init, Fore, Back, Style
init(autoreset=True)

# imports list of words from data file
from data import words

# function that gets a random word from the list of words in data file
def get_word():
    word = random.choice(words)

    return word

# function that plays the game (while loop breaks if word guessed or turns is 0)
def thegame():
    word = get_word()
    turns = 10
    playerguess = ''
    validchoices = set('abcdefghijklmnopqrstuvwxyz')
    random_word = ["_ " for i in range(len(word))]
    guessed_letters = []
    guessed = False

    while not guessed and turns > 0:

        print("Guess the word! ", " ".join(random_word))
        playerguess = input()

        if playerguess in validchoices:

            if playerguess in guessed_letters:
                print(Fore.RED + 'you already tried this letter', playerguess, '\n')
                turns -= 1
                print('Turns left: ', turns, '\n')
                print("Letters tried: ", guessed_letters, '\n')         
            elif playerguess in word:
                print(Fore.GREEN + "Well done!", playerguess, "is in the word!", '\n')
                guessed_letters.append(playerguess)
                print('Turns left: ', turns, '\n')
                print("Letters tried: ", guessed_letters, '\n')
                display_letter(word, random_word, playerguess)   
            else:
                print(Fore.RED + "That's incorrect!", playerguess, "is not in the word", '\n')
                turns -= 1
                guessed_letters.append(playerguess)
                print('Turns left: ', turns, '\n')
                print("Letters tried: ", guessed_letters, '\n')
                graphics(turns)
                
        else:
            print(Fore.RED + 'Not a valid character. Enter a letter of the alphabet.')    
            pass
        
        if turns == 0:
            graphics(turns)
            print(Fore.RED + "Game over! You lost!", "The word was", word)
            break

        if "_ " not in random_word:
            print(Fore.GREEN + "Well done! You guessed the word!", "The word was", word, '\n')
            guessed = True
            break

# function that gives the option to play the game again
def play_again():
    while input("Play again? Y/N ").upper() == "Y":
        thegame()

# function that replaces the underscore with the letter chosen by player
def display_letter(word, random_word, playerguess):
    for i in range(len(word)):
        if playerguess == word[i]:
            random_word[i] = playerguess
    
    return(" ".join(random_word))

# output that user sees
getname = input('Lets play Hangman! Enter your name: ')
print('Hi', getname)
print('Try to guess the word, you have 10 attempts')

# function for graphics

def graphics(turns):
    if turns == 9:
        print("--------------")
    if turns == 8:
        print("--------------")
        print("       O      ")
    if turns == 7:
        print("--------------")
        print("       O      ")
        print("       |      ")
    if turns == 6:
        print("--------------")
        print("       O      ")
        print("       |      ")
        print("      /       ")
    if turns == 5:
        print("--------------")
        print("       O      ")
        print("       |      ")
        print("      / \     ")
    if turns == 4:
        print("--------------")
        print("      \O      ")
        print("       |      ")
        print("      / \     ")
    if turns == 3:
        print("--------------")
        print("      \O/      ")
        print("       |      ")
        print("      / \     ")
    if turns == 2:
        print("--------------")
        print("      \O/ |   ")
        print("       |      ")
        print("      / \     ")
    if turns == 1:
        print("--------------")
        print("      \O/_|   ")
        print("       |      ")
        print("      / \     ")
    if turns == 0:
        print(Fore.RED + "--------------")
        print("      \O/_|   ")
        print("       |      ")
        print("      / \     ")

# calling functions
thegame()
play_again()