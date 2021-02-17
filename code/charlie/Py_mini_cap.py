from passlib.context import CryptContext
import passlib.hash
import passlib.exc

# loading a list of encryption schemes for the user
myctx = CryptContext(schemes=["sha256_crypt", "sha512_crypt", "md5_crypt", "des_crypt"],
                     deprecated = ["md5_crypt", "des_crypt"]
                    )

print('''Welcome to the OSSS password generation application.
first we will start with a few simple questions to get the party started.''')

UI_1 = input("\nwhat was your first pet's name?(make one up if you can't remember or didn't have one!): ")
UI_2 = input("where were you born?(can be specific or vague): ")
UI_3 = input("what is one of your favorite books?:")
UI_4 = input("One word that does NOT describe you at the moment?: ")

user_info = []
user_info.append(UI_1)
user_info.append(UI_2)
user_info.append(UI_3)
user_info.append(UI_4)
print(user_info)