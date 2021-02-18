import string

def main():
    
    #contact_list = []
    with open('contact.csv') as file:
        contents_csv = file.read()

    keys = contents_csv[0]
    data = [dict(zip(keys, row)) for row in contents_csv[1::]]
    print(data)
    # lines = contents_csv.split('\n')
    # contacts_list = []
    # keys = lines[0].split(',')
    # for i in range(1, len(lines)):
    #     row = lines[i].split(',')
    #     contact = dict(zip(keys, row))
    #     contacts_list.append(contact)
    # print(contacts_list)
    
    # dat_csv = [line.split('\n') for line in contents_csv.split('\n')]
    # print(contents_csv)
    # #contacts = []
    # #contacts = contacts.split(",")
    # #contacts.pop(0)
    # #contacts = [word for word in contacts if word not in keys]

    # for row in contents_csv[1::]:
    #     entry = {}
    #     for j, cell in enumerate(contents_csv[1::]):
    #         entry[j] = cell
    #     contacts.append(entry)
    # for values in contents_csv[1::]:
    #     contacts.append(dict(zip(keys, values)))
    #print(contacts)

main()