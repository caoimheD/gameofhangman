import random
from data import words
# importing and initializing colorama, for colour text
from colorama import init, Fore, Back, Style
init(autoreset=True)

# function that gets a random word from the list of words in data file
def get_word():
    word = random.choice(words)

    return word

# function that plays the game (while loop that breaks if word guessed or turns is 0)
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
                
        else:
            print(Fore.RED + 'Not a valid character. Enter a letter of the alphabet.')    
            pass
        
        if turns == 0:
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

# calling functions
thegame()
play_again()