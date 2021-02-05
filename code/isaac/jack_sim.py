'''
=-=-= MOB PROG. Jackalope Simulator =-=-=
=-=-=-=-=-=-= 02 Jan 2021 =-=-=-=-=-=-=-=
=-=- Composed by: Isaac, Conor, brndn =-=
'''

jackalopes = [0,0]

#jackalopes = [j+1 for j in jackalopes]

year = 0
while len(jackalopes) <= 1000: 

    for i, jack in enumerate(jackalopes):
        jackalopes[i] = jackalopes[i] + 1  
        if jack >= 4 and jack <= 8:
            jackalopes.append(0)
    for i in range(len(jackalopes)-1,0,-1):
        if jackalopes[i] == 10:
            jackalopes.pop(i)
    year += 1

print(f'\n\N{RABBIT}\N{DEER}{year}\N{THUMBS UP SIGN}\n')