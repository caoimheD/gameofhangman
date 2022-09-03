![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

This is a Python terminal game of 'Hangman', deployed to Heroku.

Players must guess a random word, and each wrong guess leads to a part of the man being drawn. If the players guess the word before the whole figure has been displayed, they win. Otherwise, they lose.

## How to play

This game is based on the traditional hangman game:
- A random word is chosen and displayed as underscores
- Players are asked to guess a letter
- If their guess is correct, the letter replaces one of the underscores
- If their guess is incorrect, they lose a turn and the figure of the hangman starts to be drawn

If the player guesses the word before theirs turns go to zero and the full figure is drawn, then the player wins.

If the turns go to zero and the full image of the hangman is drawen, then the player loses.

## Features

The first feature that the user encounters is being asked for their name. The purpose of this is to allow for a more personalized experience. The player will input their name and they will then receive a welcome message.

The payer will then see instructions and rules about the game. They are told that they have to guess the word and that they have 10 attempts.

Below this, the player will see the hidden word letters as an underscore, so they will know the legnth of the word.

### Guessing a letter

Player can press any letter of the alphabet on their keyboard to start the game. The game is set to recognize both upper and lower case entries.

If the letter they guess is correct, they receive a message that tells them that the letter chosen is in the word. The underscores in the hidden word then update to show that letter (in it's position in the word). Players also see their turns left and letters used. In this case, as the letter was correct, they do not lose a turn.

If the letter guessed is incorrect, players again receive a message, this time stating that the letter is not in the word. The 'turns left' diminishes by one and the letter guessed is added to the 'letters tried' list. The image of the hangman also starts to be drawn. As the 'turns left' gets lower, a new graphic is added, eventually showing the whole graphic.

### Winning and losing

Players can win the game by guessing all of the letters in the word. When they do this, they receive a message saying that they have guessed the word and won the game. The message also displayes the correct word again.

Players lose the game when they run out of turns and the full graphic is displayed. In this instance, they receive a message stating that they have lost and showing that the correct word was.

For both instances of winning and losing, the player is asked if they want to play again. They in put y for yes and n for no.

## Testing

Testing was mainly conducted through the gitpod terminal; as each feature was implemented, the program was run in the terminal and the feature was tested.

## Deployment

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Credits

List of random words was generated from: https://www.randomlists.com/random-words