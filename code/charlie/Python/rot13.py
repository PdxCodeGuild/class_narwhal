import string
#from string import ascii_lowercase as lower - This allows you to rename built-in methods or functions

def ROT_choose(input_str, rot_amount):
    output_str = ""

    for letter in input_str:
        if letter in string.ascii_lowercase:
            output_str += string.ascii_lowercase[(string.ascii_lowercase.index(letter) + int(rot_amount)) % 26]
        elif letter in string.ascii_uppercase:
            output_str += string.ascii_uppercase[(string.ascii_uppercase.index(letter) + int(rot_amount)) % 26]
        else:
            output_str += letter
    return output_str


        
        


def main():

   # alpha = [string.ascii_lowercase]

    print(ROT_choose(input("Please enter a string: "), input("Please enter a rotation amount: ")))

main()