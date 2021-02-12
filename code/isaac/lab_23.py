
with open('contacts.csv','r') as file:
    lines = file.read().split('\n')
    #print(lines)

#dummy_list = ["Name","Fav Fru","

#def Convert(dummy_list):
    #res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    #return res_dct


contacts_list = []

for line in lines:
    line = line.split (',')
    contacts_list.append(line)




#for rows in rows:
    #row = row.split 


#contact_dict = {}

#print(contacts_list)

for i, line in enumerate(contacts_list):
    print(f"Index: {i} of contacts_list is: ", line)


keys_1 = contacts_list[0]

values_1 = contacts_list[1:]

#for i in range of len(contacts_list)


#print(keys_1)

print(values_1)