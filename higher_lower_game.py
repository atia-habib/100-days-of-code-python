import random
import higher_lower_art
import higher_lower_game_data

print(higher_lower_art.logo)

def more_followers(A, B):
    if A['follower_count'] > B['follower_count']:
        return 'A'
    else:
        return 'B'

should_continue = True
score = 0

A = random.choice(higher_lower_game_data.data)

while should_continue:
 
    print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}")

    print(higher_lower_art.vs)

    B = random.choice(higher_lower_game_data.data)

    while A == B:
        B = random.choice(higher_lower_game_data.data)

    print(f"Against B: {B['name']}, a {B['description']} from {B['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    result = more_followers(A, B)

    if guess == result:
        score += 1
        print(f"You're right! Current score: {score}")
        
        if result == 'B':
            A = B  
    else:
        should_continue = False
        print(f"Sorry! That's a wrong answer. Your final score is {score}")
