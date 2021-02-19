####### Lab 20 - CC Validation ########
def Validation(Int_cc):
    Int_cc.reverse()

    every_other_doubled = [digit * 2 if i % 2 == 0 else digit for i, digit in enumerate(Int_cc)]
    subtract_nine = [digit - 9 if digit > 9 else digit for i, digit in enumerate(Int_cc)]
    Ints_sum = sum(subtract_nine)
    
    # for i in range(len(Int_cc)):
    #     if i % 2 == 1:
    #         Int_cc[i] *= 2

    # for i in range(len(Int_cc)):
    #     if Int_cc[i] > 9:
    #         Int_cc[i] -= 9

    # Ints_sum = sum(Int_cc)

    if Ints_sum < 10:
        checksum = Ints_sum
        return checksum
    else:
        checksum = Ints_sum % 10
        return checksum
    return 0
    
def main():
    choice = 'yes'

    while choice == 'yes':
        Str_cc = input("Please enter a 16 digit credit card to validate: ")
        Int_cc = [int(char) for char in Str_cc]
        Check_d = Int_cc.pop()
        print("Check_D = ", Check_d)
        index = len(Int_cc)
        Int_cc.pop(index-1)
    
        checksum = Validation(Int_cc)
        
        if checksum == Check_d:
            print("Your card is valid!!")
        else:
            print("Your card is invalid!")
        choice = input("Do you wanna validate another card (yes/no)?") 

main()