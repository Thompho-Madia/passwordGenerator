#a password generator
#madia thompho
#27 march 2024

import random
from datetime import datetime

capitalLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
smallLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']
specialCharacters = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
listToSelectFrom = [capitalLetters, smallLetters, digits, specialCharacters]
randomSelectionOfLists = random.choice(listToSelectFrom)
character = random.choice(randomSelectionOfLists)
twoCharcaters = random.choice(letters)

website = input("Enter website URL: ")
username = input("Enter username: ")

length = int(input("Enter the length (12-16): "))
if length < 12 or length > 16:
    print("\nInvalid length, default length chosen")
    defaultPassword = "o"*16
else:   
    #prepare the password for string slicing and manupulation
    defaultPassword = "o"*length

def even_position():
    new_password = "".join(random.choice(random.choice(listToSelectFrom)) if i == 1 else char for i, char in enumerate(defaultPassword))
    for even in range(len(defaultPassword)):
        new_password = "".join(random.choice(random.choice(listToSelectFrom)) if i == even else char for i, char in enumerate(new_password))
    return new_password

password = even_position()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print("\ntime of request:",current_time)
print("username: "+username)
print("password: "+password)

# now have to append the passwords to the password file
with open("passwords.txt", "a") as append_passwords:
    append_passwords.write(f"\n{website} : {username} : {password}\n")
