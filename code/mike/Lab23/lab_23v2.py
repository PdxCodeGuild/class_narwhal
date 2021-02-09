with open('contacts.csv', 'r') as file: # Opens contacts.csv
    lines = file.read().split('\n') # reads lines in file and splits on line break
rows = lines # identifies lines as rows
header = rows[0].split(',') # Identifies the top row as header

contacts = [] # creates empty list

for x in range(1, len(rows)): # starts with first row after header
    row = rows[x].split(',') # identifies singular row
    contact = dict(zip(header, row)) # creates dictionary called contact zipping the header and row
    contacts.append(row) # adds the contract to the contracts list


# Create new contact
new_contact = {} # empty dictionary for contact
for info in header: 
    details = input(f'Enter contact\'s {info}: ') # user inputs the contact information based on the header value
    new_contact[info] = details
    contacts.append(new_contact) # after loop, adds the contact list to the list of dictionaries


print(contacts)

rows = [','.join(header)]
for contact in contacts:
    row = ','.join(new_contact.values())
    rows.append(row)
write_contacts = '\n'.join(rows)
with open('contacts.csv', 'w') as file:
    file.write(write_contacts)