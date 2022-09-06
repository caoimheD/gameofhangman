import random

from data import animalwords  # imports lists of words from data file
from data import geowords
from data import foodwords

import colorama  #importing and initializing colorama, for colour text
from colorama import init, Fore, Back, Style
init(autoreset=True)

# output that user sees
get_name = input('Lets play Hangman! Enter your name: ')
print('Hi', get_name)
print('Objective of the game is to guess a hidden word, you can make 10 incorrect guesses.')


class CategoryChoice:
    """
    class for category choice
    """
    def __init__(self, category):
        self.category = category

    def category_selection(self):
        """
        Decides category based on player choice
        """
        if self.category == "1":
            print(Fore.YELLOW + 'The category selected is animals!')
        elif self.category == "2":
            print(Fore.YELLOW + 'The category selected is geography!')
        elif self.category == "3":
            print(Fore.YELLOW + 'The category selected is food!')


def get_word():
    """
    function that gets a random word from the list of words in data file
    """

    while True:
        make_choice = input("Choose your category (enter 1, 2 or 3):\n\n 1. Animals\n 2. Geography\n 3. Food\n")
        CategoryChoice(make_choice).category_selection()  # uses the function in the CategoryChoice class to print based on player choice

        if make_choice == '1':
            word = random.choice(animalwords)
            break
        elif make_choice == '2':
            word = random.choice(geowords)
            break
        elif make_choice == '3':
            word = random.choice(foodwords)
            break
        else:
            print('enter only 1, 2 or 3')
            pass
    
    return word




def the_game():
    """
    function that plays the game (while loop breaks if word guessed or turns is 0)
    """
    word = get_word()
    turns = 10
    player_guess = ''
    valid_choices = set('abcdefghijklmnopqrstuvwxyz')
    random_word = ["_ " for i in range(len(word))]
    guessed_letters = []
    guessed = False

    while not guessed and turns > 0:

        print("Guess a letter! ", " ".join(random_word))
        player_guess = input().lower()

        if player_guess in valid_choices:

            if player_guess in guessed_letters:
                print(Fore.RED + 'you already tried this letter', player_guess, '\n')
                turns -= 1
                print('Incorrect guesses left: ', turns, '\n')
                print("Letters tried: ", guessed_letters, '\n')         
            elif player_guess in word:
                print(Fore.GREEN + "Well done!", player_guess, "is in the word!", '\n')
                guessed_letters.append(player_guess)
                print('Incorrect guesses left: ', turns, '\n')
                print("Letters tried: ", ', '.join(guessed_letters), '\n')
                display_letter(word, random_word, player_guess)   
            else:
                print(Fore.RED + "That's incorrect!", player_guess, "is not in the word", '\n')
                turns -= 1
                guessed_letters.append(player_guess)
                print('Incorrect guesses left: ', turns, '\n')
                print("Letters tried: ", ', '.join(guessed_letters), '\n')
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


def play_again():
    """
    function that gives the option to play the game again
    """
    while input("Play again? y/n ").lower() == "y":
        the_game()


def display_letter(word, random_word, playerguess):
    """
    function that replaces the underscore with the letter chosen by player
    """
    for i in range(len(word)):
        if playerguess == word[i]:
            random_word[i] = playerguess
    
    return (" ".join(random_word))


def graphics(turns):
    """
    function that displays graphics
    """
    if turns == 9:
        print(Fore.RED + "--------------")
    if turns == 8:
        print(Fore.RED + "--------------")
        print(Fore.RED + "       O      ")
    if turns == 7:
        print(Fore.RED + "--------------")
        print(Fore.RED + "       O      ")
        print(Fore.RED + "       |      ")
    if turns == 6:
        print(Fore.RED + "--------------")
        print(Fore.RED + "       O      ")
        print(Fore.RED + "       |      ")
        print(Fore.RED + "      /       ")
    if turns == 5:
        print(Fore.RED + "--------------")
        print(Fore.RED + "       O      ")
        print(Fore.RED + "       |      ")
        print(Fore.RED + "      / \     ")
    if turns == 4:
        print(Fore.RED + "--------------")
        print(Fore.RED + "      \O      ")
        print(Fore.RED + "       |      ")
        print(Fore.RED + "      / \     ")
    if turns == 3:
        print(Fore.RED + "--------------")
        print(Fore.RED + "      \O/      ")
        print(Fore.RED + "       |      ")
        print(Fore.RED + "      / \     ")
    if turns == 2:
        print(Fore.RED + "--------------")
        print(Fore.RED + "      \O/ |   ")
        print(Fore.RED + "       |      ")
        print(Fore.RED + "      / \     ")
    if turns == 1:
        print(Fore.RED + "--------------")
        print(Fore.RED + "      \O/_|   ")
        print(Fore.RED + "       |      ")
        print(Fore.RED + "      / \     ")
    if turns == 0:
        print(Fore.RED + "--------------")
        print(Fore.RED + "      \O/_|   ")
        print(Fore.RED + "       |      ")
        print(Fore.RED + "      / \     ")


# calling functions
def main():
    the_game()
    play_again()


main()

