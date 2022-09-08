import random

from data import animalwords  # imports lists of words from data file
from data import geowords
from data import foodwords

import colorama  # importing and initializing colorama, for colour text
from colorama import init, Fore, Back, Style
init(autoreset=True)


def output_area():
    """
    output that user sees, introduction messages
    """
    get_name = input('Lets play Hangman! Enter your name: ')

    while get_name == "":
        print('please enter a valid name')
        get_name = input('Lets play Hangman! Enter your name: ')

    print('\nHi', get_name)
    print(Fore.YELLOW + '\nObjective of the game is to guess a hidden word,',
          Fore.YELLOW + 'you can make 10 incorrect guesses.\n')


class CategoryChoice:
    """
    class for category choice
    """
    def __init__(self, category):
        self.category = category

    def display(self):
        """
        Displays category based on player choice
        """
        if self.category == "1":
            print(Fore.YELLOW + 'The category selected is animals!')
        elif self.category == "2":
            print(Fore.YELLOW + 'The category selected is geography!')
        elif self.category == "3":
            print(Fore.YELLOW + 'The category selected is food!')

    def words(self):
        """
        Returns word from category chosen by player
        """
        if self.category == '1':
            return animalwords
        elif self.category == '2':
            return geowords
        elif self.category == '3':
            return foodwords
        else:
            return None


def get_word():
    """
    function that gets a random word from the list of words in data file
    """

    while True:

        make_choice = input("Choose your category (enter 1, 2 or 3):\n\n"
                            "1. Animals\n2. Geography\n3. Food\n")

        acceptable_input = ['1', '2', '3']
        # data validation for category choice input
        if make_choice not in acceptable_input:
            print('enter only 1, 2 or 3')
            continue

        category = CategoryChoice(make_choice)
        category.display()  # uses the display function in the CategoryChoice
        # class to print a message based on player choice
        word = random.choice(category.words())
        return word


def the_game():
    """
    function that plays the game (while loop breaks if word guessed
    or turns is 0)
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

        try:  # data validation for user input (ensures it is a letter)
            if player_guess not in valid_choices:
                raise ValueError('invalid')
        except ValueError:
            print(Fore.RED + 'Not a valid character. Enter a',
                  Fore.RED + 'letter of the alphabet.')
            continue

        if player_guess in guessed_letters:
            # if statement for 3 scenarios of player's guessed letter
            # (letter already used, letter correct and letter incorrect)
            print(Fore.RED + 'you already tried this letter', player_guess,
                  '\n')
            turns -= 1
            print('Incorrect guesses left: ', turns, '\n')
            print("Letters tried: ", ', '.join(guessed_letters), '\n')
        elif player_guess in word:
            print(Fore.GREEN + "Well done!", player_guess, "is in the",
                  "word", '\n')
            guessed_letters.append(player_guess)
            print('Incorrect guesses left: ', turns, '\n')
            print("Letters tried: ", ', '.join(guessed_letters), '\n')
            display_letter(word, random_word, player_guess)
        else:
            print(Fore.RED + "That's incorrect!", player_guess, "is not",
                  "in the word", '\n')
            turns -= 1
            guessed_letters.append(player_guess)
            print('Incorrect guesses left: ', turns, '\n')
            print("Letters tried: ", ', '.join(guessed_letters), '\n')
            graphics(turns)

        if turns == 0:  # ends game as user reached max errors allowed
            graphics(turns)
            print(Fore.RED + "Game over! You lost!", "The word was", word)
            break

        if "_ " not in random_word:  # ends game as user guessed all letters
            print(Fore.GREEN + "Well done! You guessed the word!",
                  "The word was", word, '\n')
            guessed = True
            break


def play_again():
    """
    function that gives the option to play the game again
    """
    start_over = input("Do you want to play again? enter y for yes or "
                       "any other letter to exit: ")

    if start_over.lower() == "y":
        main()
    else:
        exit()


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


def main():
    """
    calling all functions
    """
    output_area()
    the_game()
    play_again()


main()
