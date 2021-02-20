'''
Lab 10
Average Numbers
Version 2
'''

# numbers list referenced for loop
nums = []

while True:
    user_num = input('enter a number, or \'done\': ')
    if user_num == 'done':
        break
    else:
        nums.append(int(user_num))
        print(nums)

# base number for sum
s = 0 

# loop to show sum of list
for t in range(len(nums)):
    s = s + nums[t]
    print(s, end=' ')

# length of list
l = len(nums)

# calculation to determine average of sum of numbers in list
a = s/l

print(f'\n\nYour list: {nums}')
print(f'Length: {l}')
print(f'Sum: {s}')
print(f'Average: {a:.2f}')