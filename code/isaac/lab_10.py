import random  


# nums = [5,0,8,3,4,1,6]
# for n in nums:
#     avg = sum(nums)/len(nums)

# print (f"The average of the list is {avg} ")



#list_nums = []
counter = 0
total = 0


while True:
  
    number = input("Enter a number: ")
    
    if number == "Done":
        break



    else: 
        #list_nums.append(float(number))
        total += float(number) 
        counter +=1 
    

#avg = sum(list_nums)/len(list_nums)

avg = total/counter

print(avg)
    
     



    
    

    
     

    
    
