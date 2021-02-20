######### Lab 15 - "Number to Phrase" ###########

ones_dict = {
            0 : 'Zero',
            1 : 'One',
            2 : 'Two',
            3 : 'Three',
            4 : 'Four',
            5 : 'Five',
            6 : 'Six',
            7 : 'Seven',
            8 : 'Eight',
            9 : 'Nine'
            }

tens_dict = {
            0 : 'Zero',
            2 : 'Twenty',
            3 : 'Thirty',
            4 : 'Forty',
            5 : 'Fifty',
            6 : 'Sixty',
            7 : 'Seventy',
            8 : 'Eighty',
            9 : 'Ninety',
            }

huns_dict = {            
            1 : 'One hundred',
            2 : 'Two hundred',
            3 : 'Three hundred',
            4 : 'Four hundred',
            5 : 'Five hundred',
            6 : 'Six hundred',
            7 : 'Seven hundred',
            8 : 'Eight hundred',
            9 : 'Nine hundred'
            }

Teens_dict = {
            1.0 : 'Ten',
            1.1 : 'Eleven' ,
            1.2 : 'Twelve',
            1.3 : 'Thirteen',
            1.4 : 'Fourteen',
            1.5 : 'Fifteen',
            1.6 : 'Sixteen',
            1.7 : 'Seventeen',
            1.8 : 'Eighteen',
            1.9 : 'Nineteen'
             }

def get_teens(user_num, Teens_dict):
    teens = 0.0
    teens = (user_num % 100)/10
    if teens in Teens_dict:
        word_num = Teens_dict[teens]
        return word_num
    else: return False
            
def main():
    choice = 'yes'
    user_num = input("Please enter a number that is between 100-999 and this program will display its english representation: ")

    while choice == 'yes':
        user_num = int(user_num)
        ones_digit = user_num % 10
        tens_digit = (user_num % 100) // 10
        huns_digit = user_num // 100 

        if tens_digit == 1:
            teens_num = get_teens(user_num, Teens_dict)
            print(f'Your number is {huns_dict[huns_digit]} {teens_num}')
        elif tens_digit < 1 and ones_digit < 1:
            print(f'Your number is {huns_dict[huns_digit]}')
        elif tens_digit < 1:
            print(f'Your number is {huns_dict[huns_digit]} {ones_dict[ones_digit]}')
        elif ones_digit < 1:
            print(f'Your number is {huns_dict[huns_digit]} {tens_dict[tens_digit]}')
        else:
            print(f'Your number is {huns_dict[huns_digit]} {tens_dict[tens_digit]}-{ones_dict[ones_digit]}')

        choice = input('Would you like to see another number (yes/no)? ')
        if choice == 'no': break 
        user_num = input('Please enter a number: ')

    print('Goodbye!')

main()