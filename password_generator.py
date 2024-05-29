#a password generator
#madia thompho
#27 march 2024

import random
from datetime import datetime

capitalLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
smallLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']
specialCharacters = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
#it is easier to join if list of digit is in strings
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#a list of all single character lists
listToSelectFrom = [capitalLetters, smallLetters, digits, specialCharacters]
#randomly choose a list among lists
randomSelectionOfLists = random.choice(listToSelectFrom)
#choice a single charcater
character = random.choice(randomSelectionOfLists)
#choice to characters at once
twoCharcaters = random.choice(letters)

#user input
website = input("Enter website URL: ")
username = input("Enter username: ")

length = int(input("Enter the length (12-16): "))
#if user entres invaild number
if length < 12 or length > 16:
    print("\nInvalid length, default length chosen")
    defaultPassword = "o"*16
else:   
    #prepare the password for string slicing and manupulation
    defaultPassword = "o"*length

#it will avoid repetion of character throught the even possitons when using random.choice(random.choice(listToSelectFrom)) than character
def even_position(initalDefaultPassword):
    #the new_password is not yet initialised thus it will not be apart of the for loop
    new_password = "".join(random.choice(random.choice(listToSelectFrom)) if i == 1 else char for i, char in enumerate(defaultPassword))
    #start at position 3 since the above line takes care of the first even positon statrting at 1-12
    for even in range(len(defaultPassword)):
        new_password = "".join(random.choice(random.choice(listToSelectFrom)) if i == even else char for i, char in enumerate(new_password))
    return new_password

password = even_position(defaultPassword)
#to print time password requested, additional feature
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print("\ntime of request:",current_time)
print("username: "+username)
print("password: "+password)

# now have to append the passwords to the password file
with open("passwords.txt", "a") as append_passwords:
    append_passwords.write(f"\n{website} : {username} : {password}\n")
