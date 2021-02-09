'''
=-=-= Lab 23 08 Feb 2021 =-=-=
=-=-=-=- Contact List -=-=-=-=
=-=-=- Composer: brndn =-=-=-=
'''

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

contacts = []

keys = lines.pop(0).split(',')                            #separate header and split on ','s as keys

contact_profiles = [line.split(',') for line in lines]    #separate remaining lines as contact profiles.

for profile in contact_profiles:                          #pair keys with values for each profile
    contacts.append(dict(zip(keys,profile)))              #store each profile as a dictionary

def create_record():
    new_profile = input(f'\nEnter contact {", ".join(str(key) for key in keys)}, each separated by a comma(,) without spaces:\n>>> ').split(',')
    new_profile = [value.capitalize() for value in new_profile]
    while len(keys) != len(new_profile):
        new_profile.append('')
    contacts.append(dict(zip(keys,new_profile)))
    print(f'\nContact created:\n{dict(zip(keys,new_profile))}')
    
def retrieve_record():
    name = input(f'\n{keys[0]}: ').capitalize()
    for index, contact in enumerate(contacts):
        if name in contact[keys[0]]:
            print(f'\n{contacts[index]}')
            return index
    print('\nContact nonexistent')
    return None

def update_record():
    record_to_update = retrieve_record()
    if record_to_update == None:
        return None
    attribute = input('\nAttribute?: ').capitalize()
    new_value = input(f'\nNew {attribute}?: ').capitalize()
    contacts[record_to_update][attribute] = new_value
    print(f'\nContact updated:\n{contacts[record_to_update]}')

def delete_record():
    record_to_delete = retrieve_record()
    if record_to_delete == None:
        return None
    contacts.pop(record_to_delete)
    print('\nContact deleted.')

crud_func = {
    'c': create_record,
    'r': retrieve_record,
    'u': update_record,
    'd': delete_record,
}

while True:
    crud = input('\nManage contacts; ("Exit" to quit)\n"C" to Create\n"R" to Retrieve\n"U" to Update\n"D" to Delete\n>>> ').lower()
    try:
        if crud == 'exit':
            break
        crud_func[crud]()
    except KeyError:
        print('\nInvalid entry.')

new_lines = ''                                                     #new string to be written to file

keyline = ','.join(str(key) for key in keys)                       #turn key list into comma separated string

new_lines += f'{keyline}\n'                                        #add key line to string first, ending with \n

for contact in contacts:
    contactline = [value for key, value in contact.items()]        #turn values of each contact dict into lists
    contactline = ','.join(str(value) for value in contactline)    #turn contact lists into comma separated strings
    new_lines += f'{contactline}\n'                                #add contact lines to string, ending in \n

with open('contacts.csv', 'w') as file:
    file.write(new_lines.strip())