import random 



num_2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
            

num_2words10 = {2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy",\
               8:"Eighty", 9:"Ninety"}

def number(Number):

    if (Number >= 1) or (Number < 19):
        return (num_2words1[Number])
    elif (Number > 20) or (Number < 99):
        return (num_2words10[Number])
    else:
        print("Number is not in the range try again")
    

user_1 = input("Please enter a number. ")



tens = int(user_1)//10 
ones = int(user_1)%10

print(num_2words10 [tens])
print(num_2words1 [ones])



#print(ones)
#print(tens)
#print(user_1)
  
        








