
import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!','#', '$', '%', '&', "'", '(', ')', '*', '+']

print("Welcome to Password generator!")
let=int(input("How many letters would you like in your password?"))
sym=int(input("How many symbols would you like?"))
no=int(input("How many numbers would you like?"))

#Easy Level
'''password=""
for char in range(1,let+1): 
    password+=random.choice(letters)
for char in range(1,sym+1): 
    password+=random.choice(symbols)
for char in range(1,no+1): 
    password+=random.choice(numbers)
print(f"Yor generated password is {password}")   '''

#Hard Level

password_list=[]
for char in range(1,let+1): 
    password_list.append(random.choice(letters))
for char in range(1,sym+1): 
    password_list.append(random.choice(symbols))
for char in range(1,no+1): 
    password_list.append(random.choice(numbers))
#print(f"Yor generated password is {password_list}") 
random.shuffle(password_list)
#print(password_list)

passw=""
for char in password_list:
    passw+=char
print(f"Your password is {passw}")



