'''
Version 1
The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

Jackalopes are reproductive from ages 4-8 and die at age 10.
Gestation is instantaneous. Each gestation produces two offspring.
Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
With these conditions in mind, we can represent our population as a list of ints.
'''

#start
def main():
    age_of_jacks = [0, 0]
    years = 0 

    #loop until the length of age of jacks = 1000

    while len(age_of_jacks) <= 1000:

        for i in range(len(age_of_jacks)):
            #look at each age and if it is between 4 and 8 add a "baby"
            if 4 <= age_of_jacks[i] <= 8:
                age_of_jacks.append(0)
            #if age is 10 remove it from the population    
            if age_of_jacks[i] == 10:
                age_of_jacks.pop(i)
                #end loop if there is no i beyond end
                break
            #add one to the age of each jack
            age_of_jacks[i] += 1
        #count the number of loops aka "years"
        years += 1
    #print out the list of ages, the count, and the number of loops it took.
    print(age_of_jacks)
    print(len(age_of_jacks))
    print("It takes this many years = ", years)

main()
#end
