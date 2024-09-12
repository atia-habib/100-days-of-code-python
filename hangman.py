
import random
from hangman_words import word_list
from hangman_art import stages, logo


# Step5 Todo1: Update the word list to use the word_list from hangman_words.py 
# Step5 Todo2: Update the code to use the stages list from file hangman_art.py


#word_list=["apple", "laptop", "camel"]

# Step4 Todo1: Create a variable called 'lives' to keep the track of number of lives left.
lives = 6

print(logo)

# Step5 Todo3: Import the logo from hangman.art and print it at the start of the game


# Step1 Todo1: Randomly choose a word from the word_list, assign it to chosen_word and print it.
chosen_word=random.choice(word_list)
print(chosen_word)    

# Step2 Todo1: Create an empty string called "placeholder" with the same number of blanks as of the chosen_word
placeholder=""
word_length = len(chosen_word)
for i in range(word_length):
    placeholder += "_"
print(placeholder)

# Step3 Todo1: Use a while loop to let the user guess again.
# We can modify step1 todo2 

# Step1 Todo2: Ask the user to guess a letter & assign their answer to a variable called guess.Make guess lowercase.print guess
game_over= False
correct_letters=[]


while not game_over:

    # Step5 Todo6: Update the code to tell user how many lives are left.

    print(f"******************************** {lives}/6 LIVES LEFT ********************************")
    guess=input("\nGuess the letter: ").lower()
# print(guess)

# Step5 Todo4: If the user has entered a letter they've already guessed print the letter & let them know.
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
# Step1 Todo3: Check if the letter user guessed (guess) is one of the3 letters in chosen_word. Print "Right" if it is else print "Wrong"

# Step2 Todo2 Create a "display" that puts letter in the right positions & _ in the rest of the string.
#(use the same for loop as in step1 todo3 and change accordingly)

    display = ""
    
    # Step3 Todo2: Change the for loop so that you can keep the previous correct letters in display
    for let in chosen_word:
        if guess==let:
            display += let
            correct_letters.append(guess)
        elif let in correct_letters:
            display += let   
        else:
            display += "_"  

    print("Word to guess: " + display)

    # Step4 Todo2: If guess letter is not in the chosen_word then reduce lives by 1.
    # If lives goes down to 0 then the game should end printing you lose.

    if guess not in chosen_word:
        lives -= 1
# Step5 Todo5:If guess letter is not in the chosen_word then print it & let the user know that it is not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life!")

        if lives == 0:
            game_over = True

            # Step5 Todo7: Update the print statement below to give the user correct word they were trying to guess.
            print(f"******************************** IT WAS {chosen_word}! YOU LOSE ********************************")

    if "_" not in display:
        game_over= True
        print("********************************YOU WON******************************** ")  
    print(stages[lives])

# Step4 Todo3: print the ascii art from list stages that correspond to the number of lives the user has remaining        
