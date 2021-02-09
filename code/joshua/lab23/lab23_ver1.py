'''
Josh Novac
Lab 23
Version_1
Python
PDX Code Guild
'''


'''////////////////////////VERSION_1////////////////////////'''

with open("contacts.csv") as file:
    data = file.read().split('\n')
    
    # headers
    '''['name', 'favorite color', 'favorite fruit']'''
    headers = data[0].split(',')
    # print(headers)

    # data of each contact - prints their 'name,fav color,fav fruit'
    '''['Billy,red,apple', 'Bob,blue,orange', 'Joe,green,banana']'''
    data = data[1:4]
    # print(data)

    # lists each list of contacts and lists each element within each contact's own list
    '''[['Billy', 'red', 'apple'], ['Bob', 'blue', 'orange'], ['Joe', 'green', 'banana']]'''
    data_of_contacts = []
    for contact in data:
        data_of_contacts.append(contact.split(","))
        # print(data_of_contacts)

    # creates the list of dictionaries for each contact and adds the key headers to the contact values
    '''
        [
    {'name': 'Billy', 'favorite color': 'red', 'favorite fruit': 'apple'}, 
    {'name': 'Bob', 'favorite color': 'blue', 'favorite fruit': 'orange'}, 
    {'name': 'Joe', 'favorite color': 'green', 'favorite fruit': 'banana'}
    ]
    '''      
    contacts = []
    for contact in data_of_contacts:
        list_of_contacts = {}
        for i in range(len(headers)):
            list_of_contacts[headers[i]] = contact[i]
        contacts.append(list_of_contacts)    
    print(contacts)