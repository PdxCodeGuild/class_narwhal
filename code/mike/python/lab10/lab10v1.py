'''
Lab 10
Average Numbers
Version 1
'''

# numbers list referenced for loop
nums = [5, 0, 8, 3, 4, 1, 6]

print(f'List: {nums}')

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

print(f'\nLength: {l}')
print(f'Sum: {s}')
print(f'Average: {a:.2f}')