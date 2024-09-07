import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images=[rock,paper,scissor]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for scissors\n"))
print(game_images[user_choice])
computer_choice=random.randint(0,2)
print(f"Computer choice is {computer_choice}")
print(game_images[computer_choice])


if user_choice==0:
    if computer_choice==0:
        print("It's a draw!")
    elif computer_choice==1:
        print("You lose!")
    elif computer_choice==2:
        print("You won!")   
elif user_choice==1:
    if computer_choice==0:
        print("You won!")
    elif computer_choice==1:
        print("Play again")
    elif computer_choice==2:
        print("You lose!")  
elif user_choice==2:
    if computer_choice==0:
        print("You lose!")
    elif computer_choice==1:
        print("You won!")
    elif computer_choice==2:
        print("Play again!")      
   

       

   

