import random

# imports list of words from data file
from data import words

# importing and initializing colorama, for colour text
from colorama import init, Fore, Back, Style
init(autoreset=True)


def get_word():
    """
    function that gets a random word from the list of words in data file
    """
    word = random.choice(words)
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

        print("Guess the word! ", " ".join(random_word))
        player_guess = input().lower()

        if player_guess in valid_choices:

            if player_guess in guessed_letters:
                print(Fore.RED + 'you already tried this letter', player_guess, '\n')
                turns -= 1
                print('Turns left: ', turns, '\n')
                print("Letters tried: ", guessed_letters, '\n')         
            elif player_guess in word:
                print(Fore.GREEN + "Well done!", player_guess, "is in the word!", '\n')
                guessed_letters.append(player_guess)
                print('Turns left: ', turns, '\n')
                print("Letters tried: ", ', '.join(guessed_letters), '\n')
                display_letter(word, random_word, player_guess)   
            else:
                print(Fore.RED + "That's incorrect!", player_guess, "is not in the word", '\n')
                turns -= 1
                guessed_letters.append(player_guess)
                print('Turns left: ', turns, '\n')
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


# output that user sees
get_name = input('Lets play Hangman! Enter your name: ')
print('Hi', get_name)
print('Try to guess the word, you have 10 attempts')


def graphics(turns):
    """
    function that displays graphics
    """
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
the_game()
play_again()
