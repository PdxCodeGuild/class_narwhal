# Contact List
# Lab 23
# Richard Farr
# Feb 8th, 2021

# Version 1 - Open the contacts.csv file and turn into a dictionary
'''
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
'''

contacts = []

with open("contacts.csv", 'r') as myfile:
    firstline = True
    for line in myfile:
        if firstline:
            mykeys = "".join(line.split()).split(',')
            firstline = False
        else:
            values = "".join(line.split()).split(',')
            contacts.append({mykeys[n]:values[n] for n in range(0,len(mykeys))})
print(" ")
print(contacts)





# Version 2 - Create, Retieve, Update, & Delete (CRUD)

## Create
'''
# 1. Get input from user
name = input("Whats your name? ")
favorite_fruit = input("Whats your favorite fruit? ")
favorite_color = input("Whats your favorite color? ")
favorite_state = input("Whats your favorite state? ")
# print([name, favorite_fruit, favorite_color, favorite_state])

# 2. Turn the input into a dictionary
user_input = {'name': name, 'favorite_fruit': favorite_fruit, 'favorite_color': favorite_color, 'favorite_state': favorite_state}
print(user_input)

# 3. Add the dictionary to the list called contacts
contacts.append(user_input)
print(contacts)
'''

## Retieve

# 1. Ask the user what contact to retrieve
retieve_name = input("What person would you like the info on? ")



# 2. Spit out that output (if it exists)
for item in range(len(contacts)):
    # print(contacts[item].values())
    print(contacts[item].get(retieve_name)) # issues here
    '''
    if retieve_name in contacts[item].keys(): #[name].keys()
        print(contacts[item].get(item))
    else:
        print("nobody by that name")
        break
'''


## Update

## Delete


# Version 3 - Save everything back to the contacts.csv file
import csv

with open("contacts_updated.csv", "w", newline="") as csv_file:
  cols = ["name", "favorite_fruit", "favorite_color", "favorite_state"] 
  writer = csv.DictWriter(csv_file, fieldnames=cols)
  writer.writeheader()
  writer.writerows(contacts)







