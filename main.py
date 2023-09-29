import random

from Art import logo

print(logo)


def pick_card(deck, hand):
    """Picks a card for the passed hand from the deck, and removes it from the deck."""
    chosen_card = deck.pop(random.randrange(len(deck)))
    hand.append(chosen_card)


def is_sublist(main_list, other_list):
    """Checks if every item in the second list
    is inside the first list and the order is not
    important"""
    for item in other_list:
        if item not in main_list:
            return False
    return True


def calculate_score(hand):
    """Sums up the scores and gives the right value to an ACE."""
    if hand == ['ACE', 'ACE']:
        return 21
    if len(hand) == 4 and is_sublist(['JACK', 'QUEEN', 'KING'], hand):
        return 21
    total = 0
    for card in hand:
        if card not in ['ACE', 'JACK', 'QUEEN', 'KING']:
            total += card
        elif card == 'JACK':
            total += 3
        elif card == 'QUEEN':
            total += 4
        elif card == 'KING':
            total += 5
    for card in hand:
        if card == 'ACE':
            if total < 11:
                total += 11
            else:
                total += 1
    return total


def display_status(player, hand):
    """Displays the current status of the game."""
    if player == 'your':
        print(f"{player.capitalize()} hand: {hand} total: {calculate_score(hand)}")
    else:
        print(f"{player.capitalize()}'s hand: {hand} total: {calculate_score(hand)}")


def blackjack_game():
    """Main function to run the Blackjack game."""
    while input("Do you want to play? '0' , '1' ") == "1":
        deck = 4 * ['ACE', 'JACK', 'QUEEN', 'KING', 2, 3, 4, 5, 6, 7, 8, 9, 10]
        dealer_hand, player_hand = [], []
        player_did_not_lose = True

        # Initial deal
        for _ in range(2):
            pick_card(deck, player_hand)
            pick_card(deck, dealer_hand)

        display_status("your", player_hand)
        print(f"Dealer's hand: {dealer_hand[0]}")

        # Player's turn
        while True:
            choice = input("Another card? '0' , '1' ")
            if choice == "0":
                break
            pick_card(deck, player_hand)
            if calculate_score(player_hand) > 21:
                player_did_not_lose = False
                break
            display_status("your", player_hand)

        # Dealer's turn
        while (player_did_not_lose and
               (calculate_score(dealer_hand) < 17 or
                calculate_score(dealer_hand) < calculate_score(player_hand))):
            pick_card(deck, dealer_hand)
            if (calculate_score(dealer_hand) > 21 or
                    calculate_score(dealer_hand) == calculate_score(player_hand) == 21):
                print("___________________________")
                print("You won.")
                print("___________________________")
                break
        else:
            print("___________________________")
            print("You lost.")
            print("___________________________")

        display_status("your", player_hand)
        display_status("dealer", dealer_hand)


if __name__ == "__main__":
    blackjack_game()
