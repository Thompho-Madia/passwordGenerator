#a password retriever
#madia thompho
#28 march 2024

import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

password_pin = int(os.environ.get("password_pin"))#the pin to grant password access\

counter = 0
attempts = 3
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
words = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']

website = input("Enter website URL: ")
pin = int(input("Enter PIN: "))

#attempt 1
if pin == password_pin:
    with open('passwords.txt', 'r') as f:
        print("\nTime of request:",current_time)
        print("Passwords:\n")
        noSquareBrackets = f.readlines()
        printt = "".join(noSquareBrackets)
        print(printt)
        sys.exit()
           
else:
    counter +=1
    print(f"\n{words[attempts-counter]} more attempts before all passwords are erased from memory")
    website = input("Enter website URL: ")
    pin = int(input("Enter PIN: "))
    
#attempt 2
if pin == password_pin:
    with open('passwords.txt', 'r') as f:
        print("\nTime of request:",current_time)
        print("Passwords:\n")
        noSquareBrackets = f.readlines()
        printt = "".join(noSquareBrackets)
        print(printt)
        sys.exit()
           
else:
    counter +=1
    print(f"\n{words[attempts-counter]} more attempts before all passwords are erased from memory")
    website = input("Enter website URL: ")
    pin = int(input("Enter PIN: "))
    
#attempt 3
if pin == password_pin:
    with open('passwords.txt', 'r') as f:
        print("\nTime of request:",current_time)
        print("Passwords:\n")
        noSquareBrackets = f.readlines()
        printt = "".join(noSquareBrackets)
        print(printt)
        sys.exit()
           
else:
    print('\nAll attempts have been used up')
    recipient_email = input("Enter EMAIL account to send recovery PIN: ")
    sender_email = "stuffinternet12@gmail.com"
    #For email to be sent, enable 2 step verification the generate "app passwords" and use it as password for email with pyhton script. Browse "Google App passwords" for more info.
    sender_password = os.environ.get("sender_password")
    subject = "Acknowledgement of Terms and Conditions - MDX Security Services"
    body = f'''

    Dear valued customer,

    We hope this email finds you well. We are writing to formally acknowledge your agreement to the terms and conditions governing the use of MDX Security's services, including our
    password management system. As of {current_time}, you have accessed or utilized our services, indicating your acceptance and agreement to comply with the following terms and conditions:
    
    These terms and conditions, in conjunction with our commitment to excellence since 28 March 2024, regulate your use of our services. By utilizing our services, you agree to comply with 
    these terms fully. You are solely responsible for maintaining the confidentiality of your PIN and any other authentication credentials.
    
    Incorrect entry of the PIN may lead to the loss of access to stored passwords. Our services are for personal and non-commercial use only. Sharing of your PIN or authentication credentials
    with third parties is strictly prohibited. We prioritize the protection of your personal information and ensure its security through encryption.
    
    MDX Security shall not be liable for any loss or damage resulting from your failure to comply with these terms and conditions. We reserve the right to amend these terms and conditions at
    any time. Your continued use of our services implies acceptance of any revised terms.

    For any questions or concerns regarding these terms and conditions, please contact us at https://github.com/Thompho-Madia
    Please be aware that by using our services, you are bound by these terms and conditions. Should you have any queries or require further clarification, do not hesitate to reach out to us.

    Kindly note that this is an automated email and replies to this email address will not be monitored. If you need assistance, please contact us through the provided contact information.
    Thank you for choosing MDX Security. We look forward to serving you with excellence. The pin in the photo is incorrect the Password is: PaSword123

    Best regards,
    MDX Security Team
    '''
    
    #open the image, write the name of the file. Image must be a jpeg
    with open('authentication.jpg', 'rb') as f:
        image_part = MIMEImage(f.read())
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email
    html_part = MIMEText(body)
    message.attach(html_part)
    message.attach(image_part)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
    print(f"A recovery pin has been sent to {recipient_email}. If pin entered incorrectly all passwords saved in memory will be erased.")

recovered_pin_from_email = input("\nEnter recovery pin: ")
stored_pin = os.getenv("recovery_pin")

if recovered_pin_from_email != stored_pin:
    with open("passwords.txt", "w") as delete:
            delete.write("All passwords have been erased.")
else:
    with open("passwords.txt", "r") as all_passwords:
        print("Here are the passwords:\n")
        for line in all_passwords:
            print(line.strip()) #print all the passwords exaclty as in password file
            