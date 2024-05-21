import string
import random

length = int(input("enter password length:"))

print('''choose character set for password from these:
      1.Letters
      2.Digits
      3.Special characters
      4.Exit
                ''')

characterList =""

while(True):
    choice = int(input("pick a number:"))
    if choice == 1:
        characterList += string.ascii_letters
    elif choice == 2 :
        characterList += string.digits
    elif choice == 3:
        characterList += string.punctuation
    elif choice == 4:
        break
    else:
        print("pick a valid option!")

password = ""
for i in range(length):
    randomchar = random.choice(characterList)
    password += randomchar

print("the random password is :",password)