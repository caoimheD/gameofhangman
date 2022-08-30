import random
from data import words


def thegame():
    word = random.choice(words)
    turns = 10
    playerguess = ''
    validchoices = set('abcdefghijklmnopqrstuvwxyz')
    random_word = ["_" for i in range(len(word))]
    guessed_letters = []
    guessed = False

    while len(word) > 0 and turns > 0:

        print("Guess the word! ", " ".join(random_word))
        playerguess = input()

        if playerguess in validchoices:

            if playerguess in word:
                print('Well done!', playerguess, 'is in the word!')
                guessed_letters.append(playerguess)
                print('Turns left: ', turns)
                print("Letters tried: ", guessed_letters)
                display_letter(word, random_word, playerguess)

            elif playerguess in guessed_letters:
                print('you already tried this letter', playerguess)
                turns -= 1
                print('Turns left: ', turns)
                print("Letters tried: ", guessed_letters)
            else:
                print(playerguess, 'is not in the word')
                turns -= 1
                guessed_letters.append(playerguess)
                print('Turns left: ', turns)
                print("Letters tried: ", guessed_letters)
                
        else:
            print('Not a valid guess. Please enter a valid character')    
            playerguess = input()
        
        if turns == 0:
            print('Game over! The word was', word)
            break

        if random_word == word:
            print(random_word)
            print("You guessed the word!")
            guessed = True
            break


def main():
    while input("Play again? Y/N ").upper() == "Y":
        thegame()

def display_letter(word, random_word, playerguess):
    for i in range(len(word)):
        if playerguess == word[i]:
            random_word[i] = playerguess
    
    return(" ".join(random_word))


getname = input('Lets play Hangman! Enter your name: ')
print('Hi', getname)
print('Try to guess the word, you have 10 attempts')


thegame()
main()
