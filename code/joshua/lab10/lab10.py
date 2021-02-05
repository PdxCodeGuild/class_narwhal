'''
Josh Novac
Python
Lab10
PDX Code Guild
'''

# verison 1
# --------------------------------------------------------------------- #

nums = [5, 0, 8, 3, 4, 1, 6,]
digit = 0

# loop over the elements
# digit starts at zero to loop through each number in the list and returns the listed numbers in nums
for num in nums:
    digit += num

# 27 comes from adding all numbers in the list; 7 comes from number of elements in the list
# the sum of the digits input by the user divides by number of elements entered
# 5 + 0 + 8 + 3 + 4 + 1 + 6 = 27 -->  7 elements in list -->  sum = 27 / 7 = 3.857142857142857
sum = 0
sum = digit / (len(nums))
# print(sum)


# verison 2
# -------------------------------------------------------------------------------- #

# start with empty list, iterate each number from user input
nums = []
digit = 0
sum = 0

# have user input numbers in a list or the word 'done'
while True:
    user_input = input('Enter a number, or type done: ')
    if user_input == 'done':
        break
    nums.append(int(user_input))
# loops over each element
for num in nums:
    digit += num
# solves the average of numbers from user's input
sum = digit / len(nums)
(print(f'The average is: {sum}'))