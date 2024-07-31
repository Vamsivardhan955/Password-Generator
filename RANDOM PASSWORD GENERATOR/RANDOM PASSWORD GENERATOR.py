#############################      PASSWORD GENERATOR        ################################
import random
print("welcome to password generator!!!!!!!!!")

letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['1','2','3','4','5','6','7','8','9']
special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '.', '<', '>',
    '/', '?', '~', '`'
]
password_list=[]
password=""

n_letters=int(input("enter number of letters in password:"))
n_numbers=int(input("enter number of numbers in password:"))
n_specialcharacter=int(input("enter number of specialcharatcer in password:"))
for i in range(1,n_letters+1):
    characters=random.choice(letters)
    password_list+=characters

for i in range(1,n_numbers+1):
    characters=random.choice(numbers)
    password_list+=characters

for i in range(1,special_characters+1):
    characters=random.choice(special_characters)
    password_list+=characters

random.shuffle(password_list)


for char in password_list:
    password+=char
print(password)






