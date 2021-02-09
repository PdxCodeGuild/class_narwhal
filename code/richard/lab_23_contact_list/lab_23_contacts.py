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
# print(contacts)





# Version 2 - Create, Retieve, Update, & Delete (CRUD)

## Create
def record_create():
    # 1. Get input from user
    name = input("Whats your name? ")
    favorite_fruit = input("Whats your favorite fruit? ")
    favorite_color = input("Whats your favorite color? ")
    favorite_state = input("Whats your favorite state? ")
    # print([name, favorite_fruit, favorite_color, favorite_state])

    # 2. Turn the input into a dictionary
    user_input = {'name': name, 'favorite_fruit': favorite_fruit, 'favorite_color': favorite_color, 'favorite_state': favorite_state}
    # print(user_input)

    # 3. Add the dictionary to the list called contacts
    contacts.append(user_input)
    print("The updated list of contacts is: ")
    print(contacts)


## Retrieve
def record_retrieve():
    # 0. Print out the list of possible names
    print("The people in the database are:")
    print(contacts)                             # this could be better and just list the names

    # 1. Ask the user what contact to retrieve
    retrieve_name = input("What person would you like? ")

    # 2. Spit out that output (if it exists)
    retrieved_contact = None
    for contact in contacts:
        if contact["name"] == retrieve_name:
            retrieved_contact = contact
            print("heres the contact you asked for: ")
            print(contact)
    if retrieved_contact == None:
        print("Nobody by that name")
    return retrieved_contact



## Update
def record_update():
    print("OK, lets update a record")
    contact = record_retrieve()
    update_question = input("Are you sure you want to update this contact? (Y/N) ")
    update_question = update_question.lower()

    if update_question == "y" or update_question == "yes":
        print("OK, lets update the record")
        update_field = input("What field would you like to update? (name, favorite_fruit, favorite_color, favorite_state) ")
        update_field = update_field.lower()
        update_value = input("What would you like to update it to? ")
        print(f"OK, lets update {update_field} to {update_value}")
        contact.update({update_field: update_value})
        print("heres the new contact info")
        print(contacts)
        print("changes made")
    else:
        print("OK, good. That saves me some work")


# print("New information is: ")
# print(contacts)


## Delete
def record_delete():
    # delete_question = input("Would you like to delete a record? (Y/N) ")
    # delete_question = delete_question.lower()

    # if delete_question == "y" or update_question == "yes":
        print("OK, lets delete a record")
        print("The contacts are: ")
        print(contacts)
        print(f"There are {len(contacts)} in the list. ")
        print("Remember the first item is item 0")
        item_num = int(input("What item number do you want to delete? "))
        contacts.pop(item_num)
        
        # delete_name = record_retrieve()
        # print(delete_name)



        print("Here are the contacts after we deleted that one: ")
        print(contacts)



# Run the program using the functions above.
while True:
    start = input("What do you want to do next? (Create, Retrieve, Update, Delete, or Exit) ").lower()
    if start == "exit":
        print("OK, exiting the program")
        break
    elif start == "create":
        record_create()
    elif start == "retrieve":
        record_retrieve()
    elif start == "update":
        record_update()
    elif start == "delete":
        record_delete()   
 


# Version 3 - Save everything back to the contacts.csv file
print(" ")
print("Heres what need to be saved as a csv: ")
print(f"{contacts}")



# The Hard way - code it using base Python






# The Easy way - use a python module
'''
import csv

with open("contacts_updated.csv", "w", newline="") as csv_file:
  cols = ["name", "favorite_fruit", "favorite_color", "favorite_state"] 
  writer = csv.DictWriter(csv_file, fieldnames=cols)
  writer.writeheader()
  writer.writerows(contacts)
'''






