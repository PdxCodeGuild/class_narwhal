def main():

    contact_list = []
    with open('contact.csv', 'r') as file:
        lines = file.read().split('\n')
        keys_header = lines[0]
        for line in keys_header:
            field = line.split(",")
            entry = {'name': , 'favorite color': , 'favorite band': }
            for i, value in enumerate(field):
                entry[field] = value.strip()
            contact_list.append(entry)

    print(contact_list)

main()