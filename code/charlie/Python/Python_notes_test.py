# s = "You ain't gotta lie to kick it"
# l = s.split(" ")
# l2 = ["C", "A", "P"]
# s2 = ", ".join(l2)

# print(f"This is the split string: {l}")
# print(f"This is the conjoined string: {s2}")
# print(sorted(l2))
# print("This is what a delta looks like: \u0394")

#######******* Recursion and binary search algorithm *********#########
# import random

# nums = [num for num in range(random.randint(0, 10000)) if num % 2 != 0]
# print(nums)
# random.shuffle(nums)
# print(nums)


# def binary_search_recurse(num, nums, low, high):
#     if low >= high:
#         return None
#     mid = (low + high) // 2
#     if nums[mid] == num:
#         return mid
#     elif nums[mid] < num: # search in the upper half
#         return binary_search_recurse(num, nums, mid+1, high)
#     else: # search in the lower half
#         return binary_search_recurse(num, nums, low, mid+1)

        
# def binary_search(num, nums):
#     return binary_search_recurse(num, nums, 0, len(nums)-1)

# num = input("Please enter a number from 0 to 10,000 and we'll see if it's in the Chamber of Recursion!")

# catch = 0
# catch = binary_search(num, nums)


# print(f"")

###### List Comprehensions #######
# Stardust = [x**3 for x in range(100)]
# print("Here is the list:"), print(Stardust)

# fruits =["Pineapple", "Lychee", "Clementines", "Durian"]

# best_fruits = ["Like " + fruit.upper() + " but better!!" for fruit in fruits]
# print(best_fruits)

# years = [1995, 2000, 2004, 2024, 2022]
# leap_years = [year for year in years if year % 4 == 0]
# print(leap_years)

##### Try/Except blocks for "error handling" #############
# def my_func(num1, num2):
#     try:
#         return num1 - num2
#     except TypeError:
#         print("Those are not numbers!")

# print(my_func("5", "three"))

# try:
#     f = open("gettys.txt")
#     contents = f.read()
#     sentences = contents.split('.')
#     chars = ' '.join(sentences)
#     words = chars.split()
    
#     print("The number of words in the Gettysburg Address = ", len(words)-1)
    
#     print("The number of characters in the Gettysburg Address = ", len(chars)-1)
#     print("The number of sentences in the Gettysburg Address = ", len(sentences)-1)
#     #print(contents)
# except (IOError, OSError) as e:
#     print(e)
# finally:
#     f.close()




# ##################### Classes/OOP ########################
# # Version1
# # class Point:
# #     def __init__(self, x, y): # this is the initializer
# #         self.x = x # these are member variables
# #         self.y = y
    
# # p = Point(5,2) # call the initializer, instantiate the class
# # print(p.x) # 5
# # print(p.y) # 2

# # print(type(p)) # Point

# # Version2
# import math

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
    
#     def distance(self, p): # method, or 'member function'
#         dx = self.x - p.x
#         dy = self.y - p.y
#         return math.sqrt(dx*dx + dy*dy)
    
#     def scale(self, v):
#         self.x *= v
#         self.y *= v
# ############## Static Method #######################
#     @staticmethod
#     def from_polar(r, theta): # static methods belong to the type, not the instance
#         px = r * math.cos(theta)
#         py = r * math.sin(theta)
#         return Point(px, py) 
    
# p3 = Point()
# p1 = Point(5,2)
# p2 = Point(8,4)
# dist = p1.distance(p2) # or p2.distance(p1), either works
# print(dist)
# print(p1.x, p1.y)
# p1.scale(19)
# print("Scaled = ", p1.x, p1.y)
# # similar to how we can call methods of the str class
# s = 'hello world'
# print(s.split(' '))

# ################### Private Variables ###################
# class PointPriv:
#     def __init__(self, x, y):
#         self.__x = x  # use two underscores to denote a private variable
#         self.__y = y
    
#     def distance(self, p):
#         dx = self.__x - p.__x # still accessible from inside methods
#         dy = self.__y - p.__y # still accessible to other members of the same class
#         return math.sqrt(dx*dx + dy*dy)

# p1 = PointPriv(5,2)
# p2 = PointPriv(7,8)
# print(p1.distance(p2))
# print(p1.__x) # AttributeError: 'PointPriv' object has no attribute '__x'

# ####################### Inheritance ##############################
# '''Inheritance lets us extend the functionality of a class by adding additional methods and fields. 
# You can visualize it like an onion, with the super-class in the center, and a sub-class representing a new shell. 
# The child class has all the attributes of its parent, but additional attributes all its own.'''

# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Squirrel(Animal): # inherit from Animal
#     def __init__(self, name):
#         super().__init__(name) # invoke the parent's initializer

# s = Squirrel('Clarence')
# print(s.name)

################## Multiple Inheritance ###########################

# class ParentA:
#     def __init__(self):
#         print('start parent a initializer')
#         super().__init__()                  ### using the "super" keyword in all classes uses multiple inheritance resolution protocol
#         print('end parent a initializer')

# class ParentB:
#     def __init__(self):
#         print('start parent b initializer')
#         super().__init__()
#         print('end parent b initializer')

# class Child(ParentA, ParentB):
#     def __init__(self):
#         print('start child initializer')
#         super().__init__()
#         print('end child initializer')

# c = Child()
# x = 24
# y = 5
# print(x.__add__(y))

####### Dunder Methods in Classes ##############
# import math
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
    
#     def distance(self, p): # method, or 'member function'
#         dx = self.x - p.x
#         dy = self.y - p.y
#         return math.sqrt(dx*dx + dy*dy)
    
#     def scale(self, v):
#         self.x *= v
#         self.y *= v
#     def __str__(self): # specify a str conversion
#             return '['+str(self.x)+','+str(self.y)+']'
    
# p3 = Point(7, 10)
# p1 = Point(5,2)
# p2 = Point(8,4)
# print(p1, p2, p3)


# board = [[ '' for column in range(0,3)] for row in range(0,3)]
# print(board)
# board[1][1] = 'X'
# print(board)

# from passlib.hash import pbkdf2_sha256
# #import passlib.hash

# my_hash = pbkdf2_sha256.hash("let'sseethisworkshallwee?")
# print("The hash of my  32-bit PASS == ", my_hash)
# #thrtytwo_byte = pbkdf2_sha256.using(salt_size = 8).hash("let'sseethisworkshallwee?")
# #print("The hash of my 32-byte PASS == ", thrtytwo_byte, type(thrtytwo_byte))
# symbols = []
# for i in range(10000, 100000):
#     symbols.append(chr(i))
# print(",".join(symbols))

for i in range(1,101):
    # if i % 3 == 0 and i % 5 == 0:
    #     print("fizz buzz")
    if i % 3 == 0:
        print("fizz")
    if i % 5 == 0:
        print("buzz")
    else:
        print(i)
    