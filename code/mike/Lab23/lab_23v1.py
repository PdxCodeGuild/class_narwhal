with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

contacts = []

for line in lines:
    line = line.split(',')
    contacts.append(line)



print(lines)

print(contacts)
