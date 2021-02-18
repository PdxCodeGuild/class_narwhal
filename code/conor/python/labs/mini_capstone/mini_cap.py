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
            # below opens digits as ints and not str
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
        if p.get("name") == read: # gets the name from the user input
             print(f'''
             {p}''')

# separate read function for the Update and Delete fuctions
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
    scoring_list = start()[0] #uses the start function to re-open the saved CSV document
    rounds = ['Round 1', 'Round 2', 'Round 3', 'Round 4']
    new_list = []
    tourny = input("""
    What tournament is this for? 
    """)
    for round in rounds: # the following flips the csv document
        round_dict = {'Rounds': round} # take the rounds and coverts them from columns to rows
        for player in scoring_list:
            name = player['name'] # takes names and puts them as the headers
            round_dict[name] = player[round]
        new_list.append(round_dict) # appends new list[dict] with above changes
    names = [name for name in new_list[0].keys() if name != 'Rounds'] # separates out the names to be used in the chart
    df = pd.DataFrame(new_list) # using Pandas to create a DataFrame
    print(df)
    while True:
        show_me = input("""
        Individual' or 'All' Together? """).lower()
        if show_me == 'individual': 
            df.plot(kind = 'line', x = "Rounds", y = names, ylim = (60, 100), title = tourny, subplots = True, layout = (4,3)) # plots the points as a line chart
            plt.show() # plots individual subplots for each player
            break
        elif show_me == 'all':
            df.plot(kind = 'line', marker = '.', x = "Rounds", y = names, ylim = (60, 100), title = tourny) # plots the points as a line chart
            plt.show() # combines all players into one single chart
            break
        else:
            print('Invalid selection.')
        

while True:
    print('''
    Welcome to the Scores Manager!''')
    while True:
        print("""
        Enter 'Done' if you are finished.
        """)
        task = input("'Create' a player \n'Read' a players scores \n'Update' a player \n'Delete' a player \n'Print' a chart? ").lower()
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
        else:
            print('Invalid selection.')
    break
