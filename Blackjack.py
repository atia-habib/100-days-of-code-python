import random

import blackjack_art
print(blackjack_art.logo)

def deal_card():
    cards = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # The list includes face cards as 10
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # Check for a blackjack (two cards sum to 21)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # Handle ace as 1 if the sum goes over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack!🥳"
    elif u_score > 21:
        return "You went over. You lose!😢"
    elif c_score > 21:
        return "Opponent went over. You win🥳"
    elif u_score > c_score:
        return "You win!😎"
    else:
        return "You lose!😢"

def play_game():
    print(blackjack_art.logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Initial two cards for user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn
    while not is_game_over:    
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        # Check for blackjack or if user went over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to draw another card, type 'n' to pass: ")    
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn (keep drawing until score reaches at least 17)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())  # Fix the deal_card call
        computer_score = calculate_score(computer_cards)

    # Display final results
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Game loop
while input("Do you want to play the game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 30)
    play_game()
