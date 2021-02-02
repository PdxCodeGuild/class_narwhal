# Lab 13: ROT Cipher
# Richard
# January 28th, 2021

import string
'''
Write a program that prompts the user for a string, and encodes it with ROT13. 
For each character, find the corresponding character, add it to an output string.
Notice that there are 26 letters in the English language, so encryption is the same as decryption.
| Index   | 0| 1| 2| 3| 4| 5| 6| 7| 8| 9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|
|---------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
| English | a| b| c| d| e| f| g| h| i| j| k| l| m| n| o| p| q| r| s| t| u| v| w| x| y| z|
| ROT+13  | n| o| p| q| r| s| t| u| v| w| x| y| z| a| b| c| d| e| f| g| h| i| j| k| l| m|
<!-- To wrap around from index 25 to 0 use modulus %26 to give you the remainder -->
'''

# 1. Get user input
user_input = input("Please enter a string: ")
user_input = user_input.lower()
print(f"You entered: {user_input}")

user_input_shift = int(input("How much of a shift do you want? (enter 0 to 26) "))
print(f"You asked for a shift of {user_input_shift}")

# 2. Turn user input into a list
input_v2 = [(x) for x in user_input]
# print(f"User input as list: {input_v2}")

# 3. Import the lower case alphabet
alphabet = list(string.ascii_lowercase)
# print(alphabet)

# 4. Write a function that tell me the position of a letter
output_number = []
for item in input_v2:
    index = alphabet.index(str(item))
    output_number.append((index + user_input_shift) % 26)
    # print(index)
# print(output_number)

# 5. Calculate the new values
output_letter = []
for item in output_number:
    output_letter.append(alphabet[item])
# print(output_letter)

# 6. Output the new values
listToStr = ''.join([str(elem) for elem in output_letter])  
print(f"Here's what you get back: {listToStr}")  


'''
## Version 2 (optional)
Allow the user to input the amount of rotation used in the encryption / decryption.
'''
# done by adjusting the code above

# 6. Calculate the new values
output_letter = []
for item in output_number:
    output_letter.append(alphabet[item])
# print(output_letter)

# 7. Output the new values
listToStr = ''.join([str(elem) for elem in output_letter])  
print(f"Here's what you get back: {listToStr}")  


'''
## Version 2 (optional)
Allow the user to input the amount of rotation used in the encryption / decryption.
'''
# done by adjusting the code above