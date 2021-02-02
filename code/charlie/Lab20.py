####### Lab 20 - CC Validation ########
def Validation(Int_cc, Sum):
    Int_cc.reverse()

    for i in range(len(Int_cc)):
        if i % 2 == 1:
            Int_cc[i] *= 2

    for i in range(len(Int_cc)):
        if Int_cc[i] > 9:
            Int_cc[i] -= 9

    for i in Int_cc:
        Sum += Int_cc[i]

    if Sum < 10:
        checksum = Sum
        return checksum
    else:
        checksum = Sum % 10
        return checksum
    return 0
    
def main():
    choice = 'yes'

    while choice == 'yes':
        Sum = 0
        Str_cc = input("Please enter a 16 digit credit card to validate: ")
        Int_cc = [int(char) for char in Str_cc]
        Check_d = Int_cc[-1]
        Int_cc.pop(15)
    
        checksum = Validation(Int_cc, Sum)
        
        if checksum == Check_d:
            print("Your card is valid!!")
        else:
            print("Your card is invalid!")
        choice = input("Do you wanna validate another card (yes/no)?") 

main()