# ---- Mini Capstone ---- #

# -- Golf Tournament Scores -- #
# -- With Plotted Print out -- #

import matplotlib.pyplot as plt
import pandas as pd


def start():
    scoring = []
    with open('scores.csv', 'r') as file:
        lines = file.read().split('\n')
        header = lines[0].split(',') # turn the first line into headers
        for i in range(1, len(lines)): # skip the headers
            row = lines[i].split(',')  # give the rows value
            row = [int(item) if item.isdigit() else item for item in row]
            player = dict(zip(header, row)) # zip 'em up into a dicitonary
            scoring.append(player) # toss it into the contact_list list
        return scoring, header

scoring_list, header = start()

def save(scoring_list):
    topline = [','.join(header)]
    for player in scoring_list:
        strings = [str(value) for value in player.values()]
        rows = ','.join((strings)) # turn the contacts into strings separated by commas
        topline.append(rows) # add to the lines list of headers
    new_list = '\n'.join(topline) # turn lines into a string
    with open('scores.csv', 'w') as file:
        file.write(new_list) # write over the scores.csv file

def create(scoring_list, header):
    new = {}
    for key in header:
        new[key] = input(f"What is the new players's '{key}'? ")
    scoring_list.append(new)
    save(scoring_list)
    # print(scoring_list)

def cont_read(scoring_list):
    read = input('Please enter the name of the player ')
    for player in scoring_list:
        p = player
        if p.get("name") == read:
             print(f'''
             {p}''')

def read(scoring_list):
    read = input('Please enter the name of the contact? ')
    for player in scoring_list:
        p = player
        if p.get("name") == read:
            return p

def update(scoring_list):
    player = read(scoring_list)
    category_to_update = input("Please enter the category you would like to update: ")
    new_value = input(f"What would you like to change it to?  ")
    player[category_to_update] = new_value
    save(scoring_list)
    return player

def delete(scoring_list):
    delete = read(scoring_list)
    for i, player in enumerate(scoring_list):
        if player == delete:
            del scoring_list[i]
    save(scoring_list)

def plotting(scoring_list):
    scoring_list = start()[0] 
    rounds = ['round 1', 'round 2', 'round 3', 'round 4']
    new_list = []
    for round in rounds:
        round_dict = {'rounds': round}
        for player in scoring_list:
            name = player['name']
            round_dict[name] = player[round]
        new_list.append(round_dict)
    names = [name for name in new_list[0].keys() if name != 'rounds']
    df = pd.DataFrame(new_list)
    # names = [name for name in new_list[0].keys() if name != 'rounds']
    df.plot(x = "rounds", y = names, ylim = (25, 55))
    plt.show()

while True:
    print('''
    Welcome to the Scores Manager!''')
    while True:
        print("""
        Enter 'Done' if you are finished.""")
        task = input("Would you like to 'Create', 'Read', 'Update', 'Delete' or 'Print' a chart? ").lower()
        if task == 'done':
            print('''
            Have a good day!''')
            break
        elif task == 'create':
            create(scoring_list, header)
        elif task == 'read':
            cont_read(scoring_list)
        elif task == 'update':
            update(scoring_list)
        elif task == 'delete':
            delete(scoring_list)
        elif task == 'print':
            plotting(scoring_list)
    break
    # topline = [','.join(header)]
    # for player in scoring_list:
    #     strings = [str(value) for value in player.values()]
    #     rows = ','.join((strings)) # turn the contacts into strings separated by commas
    #     topline.append(rows) # add to the lines list of headers
    # new_list = '\n'.join(topline) # turn lines into a string
    # with open('scores.csv', 'w') as file:
    #     file.write(new_list) # write over the scores.csv file
    # break

# strings = [str(value) for value in players.values()]
