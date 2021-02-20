###### Python Mini-Capstone ######
# Author:Charles Spahn
# Password Generator


from passlib.context import CryptContext
import passlib.hash
import passlib.exc
import random

# loading a list of encryption schemes for the user
myctx = CryptContext(schemes=["sha256_crypt", "sha512_crypt","ldap_salted_md5", "md5_crypt", "des_crypt"],
                     deprecated = ["md5_crypt", "des_crypt"], ldap_salted_md5__salt_size= 16
                    )
count = 3
choice = 'yes'
print('''Welcome to the OSSS password generation application.
first we will start with a few simple questions to get the party started.''')

while count > 0 and choice == "yes":
    hash_choice = input("Please choose from the following options for encryption levels. \nSHA512, SHA256, salted MD5, MD5, or DES: ")
    hash_choice = hash_choice.upper().strip()

    UI_1 = input("\nwhat was your first pet's name?(make one up if you can't remember or didn't have one!): ")
    UI_2 = input("where were you born?(can be specific or vague): ")
    UI_3 = input("what is one of your favorite books?: ")
    UI_4 = input("One word that does NOT describe you at the moment?: ")

    #Here we take the user inputs to sort, reverse, and shuffle the list.
    user_info = []
    user_info.append(UI_1)
    user_info.append(UI_2)
    user_info.append(UI_3)
    user_info.append(UI_4)
    user_info.sort(reverse=True)
    random.shuffle(user_info)
    my_pass = ",".join(user_info).upper()

    # creating a hash based off the user's choice of encryption scheme and their inputs to prompt questions.
    if hash_choice == 'SHA512':
        UI_to_pass = myctx.hash(my_pass, scheme="sha512_crypt")
    elif hash_choice == "SHA256":
        UI_to_pass = myctx.hash(my_pass, scheme="sha256_crypt")
    elif hash_choice == "SALTED MD5":
        UI_to_pass = myctx.hash(my_pass, scheme="ldap_salted_md5")
    elif hash_choice == "MD5":
        UI_to_pass = myctx.hash(my_pass, scheme="md5_crypt")
    elif hash_choice == "DES":
        UI_to_pass = myctx.hash(my_pass, scheme="des_crypt")
    else:
        print("Error, the value entered for an encryption algorithm is incorrect!")

    print(UI_to_pass)
    Pass_hash = myctx.hash(UI_to_pass, scheme="sha256_crypt")
    pass_to_verify = input("Please enter you password to verify it was encrypted correctly:\n").strip()
    if myctx.verify(pass_to_verify, Pass_hash):
        print("your password is valid and has been encrypted correctly!")
        count -= 1
    else:
        print("Something has gone wrong.........")
        count -= 1
        print(f"You have {count} chances left to verify!")
    if count == 0:
        break
    choice = input("Would you like to have another password generated (yes/no)? ")

print("Thank you for using the OSSS password genration tool.\nGoodbye!")

