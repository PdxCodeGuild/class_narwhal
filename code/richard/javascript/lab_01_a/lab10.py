# Richard
# Lab 10 - average numbers
# January 27th, 2021

# https://github.com/PdxCodeGuild/class_narwhal/blob/main/1%20Python/labs/lab10-average_numbers.md



############################################
# Version 1 - Take the average by adding the numbers up and dividing by the total

nums = [5, 0, 8, 3, 4, 1, 6]

'''
# loop over the elements
for num in nums:
    print(num)

# loop over the indices
for i in range(len(nums)):
    print(nums[i])
''' 


'''
total = 0
for num in nums:
    total = total + num
print(total / len(nums))
'''

############################################
# Version 2 - Ask the user to enter the numbers one at a time

'''
> enter a number, or 'done': 5
> enter a number, or 'done': 3
> enter a number, or 'done': 4
> enter a number, or 'done': done
average: 4


nums = []
nums.append(5)
print(nums)
'''

# Step 1: Get user input and use to create and display the list of numbers
num_list = []
user_input = 0

while True:
    user_input = input("enter a number, or 'done': ")

    if user_input == "done" or user_input == " ":
        break

    try:
        val = float(user_input)
        num_list.append(float(user_input))
        continue
    except ValueError:
        print("That's not a number!")

        

print(f"The list of numbers you entered is: {num_list}")


# Step 2: do the math on the number list and display the average


user_total = 0
for num in num_list:
    user_total = user_total + num
user_average = (user_total / len(num_list))
print(f"average: {user_average}")