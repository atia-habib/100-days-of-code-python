import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 to 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")


num = random.randint(1, 100)

def Number_Guessing(num):
    if level == 'hard': 
        attempts = 5
    elif level == 'easy':
        attempts = 10
    else:
        print("Invalid difficulty level. Please choose 'easy' or 'hard'.")
        return  

    while attempts > 0:
        print(f'You have {attempts} attempts remaining to guess the number.')
        guess = int(input("Make a guess: "))  

        if guess > num:
            print("Too high!")
            attempts -= 1
        elif guess < num:
            print("Too low!")
            attempts -= 1
        else:
            print(f"You got it right! The number was {num}.")
            break

        if attempts == 0:
            print(f"Sorry, you've run out of attempts. The number was {num}.")

Number_Guessing(num)
