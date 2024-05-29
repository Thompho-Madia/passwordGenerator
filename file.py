with open('passwords.txt', 'r') as f:
    # print("\nTime of request:",current_time)
    # print("Passwords:\n")
    noSquareBrackets = f.readlines()
    printt = "".join(noSquareBrackets)
    # print(printt)
    # sys.exit()
    # print()
    # print(noSquareBrackets)

retrieve = input("Enter website URL: ")
    
count  = 0
length = len(noSquareBrackets)
for i in noSquareBrackets:
    # print(i)
    colon = i.find(":")
    # print(colon)
    website = i[:colon-1]
    # print(website)
    if website == retrieve:
        print(i)
    count+=1
    if count == length:
        print("Password not found")
    # print(count)