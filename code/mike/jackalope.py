'''
Version 1
The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

Jackalopes are reproductive from ages 4-8 and die at age 10.
Gestation is instantaneous. Each gestation produces two offspring.
Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
With these conditions in mind, we can represent our population as a list of ints.
'''
population = 2
years = 0
# Life of a jackalope

max_age = 10
current_age = 0

while population <= 1000:
    while current_age < max_age:
        if  4 <= current_age <= 8:
            population += 2
            current_age += 1
            years += 1
        elif current_age == 10:
            population -= 2
            current_age += 1
            years += 1
        else:
            current_age += 1
            years += 1

print(population)
print(years)

 #if age is between 4 and 8 add 2 offspring per year

 #if age is 10 remove 1 from the total population
 #if age is 0-3 or 9 nothing 

# Total population count
    



# def main():

#     age_of_jacks = [0, 0]
#     num_of_jacks = 2
    
#     while num_of_jacks <= 1000:

#         for i in range(len(age_of_jacks)):
            
#         if 4 =< age_of_jacks[] <= 8:
#             num_of_jacks += 2


#    # for n in range(1000):


# main()