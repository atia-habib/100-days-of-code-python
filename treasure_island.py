print("Welcome to the treasure island!\n Your mission is to find the treasure!")
dir=input("You are at a cross road.Where do u want to go?\n Type 'left' or 'right' ")
if dir=="left":
    print("You've come to a lake.There is an island in the middle of the lake.")
    comm=input("Type 'wait' to wait for a boat.Type 'swim' to swim across. ")
    if comm=="wait":
        print("You arrived at the island unharmed.There is a house with 3 doors.")
        col=input("One red,one yellow and one blue.Which color do you choose?")
        if col=="red" or col=="blue":
            print("Game over!")
        elif col=="yellow":
            print("You Won!")    

    elif comm=="swim":
        print("Game over!")    
else:
    print("Game over!")    
      

