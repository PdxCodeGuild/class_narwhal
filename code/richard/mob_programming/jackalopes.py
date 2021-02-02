'''Mob Programming: Jackalope Simulator

Version 1
The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

Jackalopes are reproductive from ages 4-8 and die at age 10.
Gestation is instantaneous. Each gestation produces two offspring.
Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
With these conditions in mind, we can represent our population as a list of ints.
'''


jackalopes = [4]
total_jackalopes = len(jackalopes)
print(f'total jackalope pairs - {total_jackalopes}')

time = 0
offspring = 1
reproductive_age_min = 4
reproductive_age_max = 8
jackalope_age_of_death = 10
population_target = 1000 / 2

# do while total_jackalopes <= population_target:
#     time += 1

## calculate new offspring
# how many reproducing adults?
reproducing_adults = [n for n in jackalopes if (n >= 4 and n <= 8)]
# print(reproducing_adults)
reproducing_adults_count = len(reproducing_adults)
# print(reproducing_adults)
print(f'reproducing adult pairs - {reproducing_adults_count}')

## add 1 year to everyones' ages
for i in range(len(jackalopes)):
    jackalopes[i] = jackalopes[i] + 1
print(jackalopes)

## how many new kids?
new_kids = reproducing_adults_count # pairs
# add the new kids to the list of jackalopes
if reproducing_adults_count == 0:
    jackalopes = jackalopes
else:
    for kids in reproducing_adults:
        jackalopes.append(0)
print(jackalopes)


## calculate dead jackalopes
# how many jackalopes older than 10?

## count total jackalopes
# total jackalopes = original - dead jackalopes + new




















'''
Version 2
Now let's give the jackalopes distinct sexes and extend their gestation period to one year. We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries. A jackalope will have the following properties:

name
age
sex
whether they're pregnant
Jackalopes can only mate with those immediately around them. Every generation Jackalopes are randomly shuffled.
'''