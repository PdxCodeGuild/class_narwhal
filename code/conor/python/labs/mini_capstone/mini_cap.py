# ---- Mini Capstone ---- #

# -- Golf Tournament Scores -- #
# -- With Plotted Print out -- #

import matplotlib.pyplot as plt
import pandas as pd

scoring_list = []

with open('scores.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(scores)
    header = lines[0].split(',') # turn the first line into headers
    for i in range(1, len(lines)): # skip the headers
        row = lines[i].split(',')  # give the rows value
        row = [int(item) if item.isdigit() else item for item in row]
        print(row)
        players = dict(zip(header, row)) # zip 'em up into a dicitonary
        scoring_list.append(players) # toss it into the contact_list list

print(scoring_list)

df = pd.DataFrame(scoring_list)
print(df)
df.plot(x = "rounds", y = ['conor', 'billy', 'mike'])
plt.show()
# # plt.plot(df)