# Richard 
# March 3rd, 2021
# Fizz Buzz

'''
Write a Python program which iterates the integers from 1 to 100. 
For multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.
'''

for fizzbuzz in range(1, 101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    print(fizzbuzz)
	