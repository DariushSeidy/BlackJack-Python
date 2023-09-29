# Blackjack Game

This is a simple command-line Blackjack game implemented in Python. The game allows you to play Blackjack against a dealer.

## Features

- **Pick Card Functionality:** The game includes a function to pick a card for a given hand from the deck and remove it from the deck.
- **Scoring:** A scoring function calculates the total score of a hand, considering the values of different cards, including special handling for ACE.
- **Game Logic:** The main game function `blackjack_game()` orchestrates the gameplay, allowing the player to draw cards and compete against the dealer.

## How to Play

1. Run the `blackjack_game()` function in the script.
2. Follow the prompts to decide whether to draw another card or not.
3. The game continues until the player chooses to stop or busts (score exceeds 21).
4. The dealer then plays according to standard Blackjack rules.
5. The winner is determined, and the game displays the final results.

## Usage

Clone the repository and run the script:

```bash
python blackjack.py
