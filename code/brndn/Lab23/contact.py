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
        
print(f'\n {contacts}\n')