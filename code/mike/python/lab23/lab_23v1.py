'''
Lab 23
Version 1
Contacts List
'''

with open('contacts.csv', 'r') as file: # Opens contacts.csv
    rows = file.read() # reads file as rows

contacts = [] # creates empty list

rows = rows.split('\n') # separates rows with line break
header = rows[0].split(',') # Identifies the top row as header

# starts list of contacts on the first row after header
for x in range(1, len(rows)):
    row = rows[x].split(',')
    contact = dict(zip(header, row))
    contacts.append(contact)

print(contacts)
