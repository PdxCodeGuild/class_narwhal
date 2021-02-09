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

## Retrieve

# 1. Ask the user what contact to retrieve
retrieve_name = input("What person would you like the info on? ")



# 2. Spit out that output (if it exists)
retrieved_contact = None
for contact in contacts:
    if contact["name"] == retrieve_name:
        retrieved_contact = contact
        print(contact)
if retrieved_contact == None:
    print("Nobody by that name")



## Update

update_question = input("Would you like to update any field on the contact we just recieved? (Y/N) ")
update_question = update_question.lower()

if update_question == "y" or update_question == "yes":
    print("OK, lets update the record")
    update_field = input("What field would you like to update? (name, favorite_fruit, favorite_color, favorite_state) ")
    update_field = update_field.lower()
    update_value = input("What would you like to update it to? ")
    print(f"OK, lets update {update_field} to {update_value}")
    contact.update({update_field: update_value})
    print("heres the new contact info")
    print(contact)
    # if update_field == name:
        #retrieved_contact.update({"name": update_value })
print(f"New information is: ")
print(contacts)


## Delete
delete_question = input("Would you like to delete a record? (Y/N) ")
delete_question = delete_question.lower()

if delete_question == "y" or update_question == "yes":
    print("OK, lets delete a record")
    delete_item = int(input("Whats the position of the record you would like to delete? "))
    del contacts[delete_item]
    print("Here are the contacts after we deleted that one: ")
    print(contacts)


    

    
# print(f"New information is: {contact}")






# Version 3 - Save everything back to the contacts.csv file


# The Easy way - use a python module
import csv

with open("contacts_updated.csv", "w", newline="") as csv_file:
  cols = ["name", "favorite_fruit", "favorite_color", "favorite_state"] 
  writer = csv.DictWriter(csv_file, fieldnames=cols)
  writer.writeheader()
  writer.writerows(contacts)







