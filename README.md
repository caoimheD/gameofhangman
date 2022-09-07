![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

This is a Python terminal game of 'Hangman', deployed to Heroku.

Players must guess a random word, and each wrong guess leads to a part of the man being drawn. If the players guess the word before the whole figure has been displayed, they win. Otherwise, they lose.

## How to play

This game is based on the traditional hangman game:
- Players choose a category for the word
- A random word is chosen and displayed as underscores
- Players are asked to guess a letter
- If their guess is correct, the letter replaces one of the underscores
- If their guess is incorrect, they lose a turn and the figure of the hangman starts to be drawn

If the player guesses the word before their turns go to zero and the full figure is drawn, then the player wins.

If the turns go to zero and the full image of the hangman is drawen, then the player loses.

## Features

The first feature that the user encounters is being asked for their name. The purpose of this is to allow for a more personalized experience. The player will input their name and they will then receive a welcome message. This data entry is validated and it cannot be left blank. Players are free to enter any name they like, even with numbers or characters, however if they leave it blank they will be asked to enter their name again.

The player will then see instructions and rules about the game:


They are informed what the objective of the game is and that they can make a maximun of 10 wrong guesses. They are then introduced to a feature of the game which is categorys. There is a choice of 3 categorys (animals, geography, food): depending on the player choice, the word they have to guess will be related to that category.

This is possible through the use of 3 separate lists of words in the data.py file. Based on the category choice, the random word will be selected from only one of them lists.

After making a selection, users will receive a message which confirms their choice and the game then starts; they are asked to guess a letter and the random word is hidden with underscores. This data is validated and the only acceptable entres are the numbers 1, 2 and 3.

### Guessing a letter

Player can press any letter of the alphabet on their keyboard to start the game. The game is set to recognize both upper and lower case entries. Data is validated, which means that if the player enters a character that is not a letter (for example a number), then they will get a message asking to input a valid character.

If the letter they guess is correct, they receive a message that tells them that the letter chosen is in the word. The underscores in the hidden word then update to show that letter (in it's position in the word). Players also see their 'incorrect guesses left' and letters used. In this case, as the letter was correct, they do not lose a turn.

If the letter guessed is incorrect, players again receive a message, this time stating that the letter is not in the word. The 'incorrect guesses left' diminishes by one and the letter guessed is added to the 'letters tried' list. The image of the hangman also starts to be drawn. As the 'incorrect guesses left' gets lower, a new part of the graphic is added, eventually showing the whole graphic of the hanging man.

### Winning and losing

Players can win the game by guessing all of the letters in the word. When they do this, they receive a message saying that they have guessed the word and won the game. The message also displays the correct word again.

Players lose the game when they run out of incorrect guesses and the full graphic is displayed. In this instance, they receive a message stating that they have lost and showing what the correct word was.

For both instances of winning and losing, the player is asked if they want to play again. They can input y for yes and n for no.

## Testing

Testing was mainly conducted through the gitpod terminal; as each feature was implemented, the program was run in the terminal and the feature was tested. If it did not work as intended, the code was then worked on again.

The following features were tested:

| Action        | Expected Behaviour  | Result | 
| ------------- | ------------- | ------------- | 
| Run application in terminal  | Message appears and asks for name | pass | 
| Player enters name  | introduction message and category choice appear | pass | 
| Player enters category number  | message confirming category choice appears, game starts | pass | 
| Player enters random character when asked for category  | player is asked to choose again | pass | 
| game starts (after category selection)  | word is displayed as underscores | pass | 
| player enters an uppercase letter  | message says if letter is in the word or not | pass | 
| player enters an lowercase letter  | message says if letter is in the word or not | pass | 
| player enters a letter  | letter is added to 'letters used' list | pass | 
| player enters a number or character  | message says invalid character | pass | 
| letter is correct  | letter replaces underscore | pass | 
| letter is incorrect  | 'incorrect guesses left' decreases by 1 | pass | 
| letter is incorrect  | a piece of the graphic is shown | pass |
| player guesses all letters  | winning message displayed, asked if they want to play again | pass |  
| incorrect guesses left goes to 0  | player told they lost, full graphic drawn, asked if they want to play again | pass |  
| enter 'y' to play again question | game restarts | pass | 
| enter 'n' to play again qustion | game exits | pass | 

## Deployment

This project was deployed to Heroku with the following steps:

- create new app

- adding two buildpacks from the _Settings_ tab: `heroku/python`, `heroku/nodejs`
- creating a _Config Var_ called `PORT` and setting this to `8000`
- connected to GitHub repository and deployed

Live link: https://game-hangman-pp3.herokuapp.com/

## Credits

List of random words was generated from: https://www.randomlists.com/random-words