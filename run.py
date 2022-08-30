import random
from data import words

def thegame():
    word = random.choice(words)
    turns = 10
    playerguess = ''
    validchoices = set('abcdefhijklmnopqrstuvwxyz')
    random_word = "_ " * len(word)
    guessed_letters = []
    guessed = False

    while not guessed and turns > 0:
        random_word = ''

        for letter in word:
            if letter in playerguess:
                random_word = random_word + letter
            else:
                random_word = random_word + "_ "

        if random_word == word:
            print(random_word)
            print("You guessed the word!")
            break

        print("Guess the word! ", random_word)
        guess = input()

        if guess in validchoices and len(guess) == 1:
            if guess in guessed_letters:
                print('you already tried this letter', guess)
                turns -= 1
                print('Turns left: ', turns)
            elif guess not in word:
                print(guess, 'is not in the word')
                turns -= 1
                guessed_letters.append(guess)
                print('Turns left: ', turns)
            elif guess not in validchoices:
                print('Not a valid guess. Please enter a valid character')
                guess = input()
                print('Turns left: ', turns)
            else:
                print('Well done!', guess, 'is in the word!')
                guessed_letters.append(guess)
                playerguess = playerguess + guess
            
        if turns == 0:
            print('Game over! The word was', word)
            break

def main():
    while input("Play again? Y/N ").upper() == "Y":
        thegame()

getname = input('Lets play Hangman! Enter your name: ')
print('Hi', getname)
print('Try to guess the word, you have 10 attempts')


thegame()
main()
