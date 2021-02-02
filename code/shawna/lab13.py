import string
 
# For each character, find the corresponding character, add it to an output string. 
# Notice that there are 26 letters in the English language, so encryption is the same as decryption.

#create alphabet as a list
alphabet = list(string.ascii_lowercase)

#get message from user
message = input("Enter Secret Message: ").lower()

#create the key
magic_num = input("Please enter the secret key (the number for the cypher) ")
magic_num = int(magic_num)

#convert user message to list
message = list(message)

#convert user message to numbers keeping punctuation
message = [alphabet.index(i) if i.isalpha() else i for i in message]

#add cypher number to each preserving space and punctuation
message = [((num + magic_num) % 26) if isinstance(num, int) else num for num in message]

encoded_message = [alphabet[num] if isinstance(num, int) else num for num in message]

encoded_message = "".join(encoded_message)

print(encoded_message.upper())
