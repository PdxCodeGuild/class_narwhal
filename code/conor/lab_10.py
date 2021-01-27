# ---- Lab 10 ---- #

# - Average Calculation - #

# - Version 1 - #

#nums = [5, 0, 8, 3, 4, 1, 6]

#x = sum(nums)/7

#print(round(x, 2))

# - Version 2 - #

print("""
Welcome to the "Average" Calculator!""")

nums = [] # blank list that will be filled by the user inputs

# loop for the user input. Will break when user types "finished"
while True:
    num_in = input("Please enter a number or type 'done': ")
    if num_in == 'done': # 'done' breaks the loop
        break
    else: # else: will keep append'ing the 'nums' list until 'done' is typed
        nums.append(float(num_in))

# the sum of 'nums' is then divided by the lenght of 'nums'
avg = sum(nums)/len(nums)
print(f"""
You entered: {nums}""") # shows which numbers the user input
print(f"""
The average is: {avg:.2f}.""") # shows what the average of the input numbers

#######################################