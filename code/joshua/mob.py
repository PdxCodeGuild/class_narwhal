# Feb 2nd, 2021
# Richard
# Josh

'''Mob Programming: Jackalope Simulator
Version 1
The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.
Jackalopes are reproductive from ages 4-8 and die at age 10.
Gestation is instantaneous. Each gestation produces two offspring.
Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
With these conditions in mind, we can represent our population as a list of ints.
'''


jackalopes = [0]
total_jackalopes = len(jackalopes)
# print(f'total jackalope pairs - {total_jackalopes}')

time = 0
offspring = 1
reproductive_age_min = 4
reproductive_age_max = 8
jackalope_age_of_death = 10
population_target = 500 # 1000 / 2  => counted in pairs => 1000 translates into 500 pairs

while total_jackalopes <= population_target:
    time += 1

    ## calculate new offspring
    # how many reproducing adults?
    reproducing_adults = [n for n in jackalopes if (n >= 4 and n <= 8)]
    # print(reproducing_adults)
    reproducing_adults_count = len(reproducing_adults)
    # print(reproducing_adults)
    # print(f'reproducing adult pairs - {reproducing_adults_count}')



    ## add 1 year to everyones' ages
    for i in range(len(jackalopes)):
        jackalopes[i] = jackalopes[i] + 1
    # print(jackalopes)



    ## how many new kids?
    new_kids = reproducing_adults_count # pairs
    # add the new kids to the list of jackalopes
    if reproducing_adults_count == 0:
        jackalopes = jackalopes
    else:
        for kids in reproducing_adults:
            jackalopes.append(0) # add new kids to the list
    # print(jackalopes)



    # remove the 10 year old jackalopes from the list
    jackalopes = [n for n in jackalopes if (n < 10)]
    # print(jackalopes2)

    total_jackalopes = len(jackalopes)

'''
    ## calculate dead jackalopes
    # how many jackalopes age 10 or older?
    dying_adults = [n for n in jackalopes if (n == 10)]
    # print(reproducing_adults)
    dying_adults_count = len(dying_adults)
    # print(reproducing_adults)
    print(f'dying adult pairs - {dying_adults_count}')
'''

'''
    for items in jackalopes: # range(len(jackalopes)):
        if jackalopes[items] == 10:
            jackalopes.remove(10)   # .remove() ?
'''
    

print(f"jackalopes - {jackalopes}")
print(f"total jackalope pairs - {total_jackalopes}")
print(f"total jackalopes - {total_jackalopes * 2}")
print(f"time - {time}")