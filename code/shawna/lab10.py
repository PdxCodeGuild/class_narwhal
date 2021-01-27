while True:
    user_input = input('Enter the numbers to calculate the average seperated by a comma (i.e. 1, 2, 3) or "done" to exit.\n')
    if user_input.lower() == "done":
            break
    try: 
        sub_total = 0
        #split input on the comma and remove leading whitespace
        # list comprehension example found here https://stackoverflow.com/questions/4071396/split-by-comma-and-strip-whitespace-in-python
        nums = [num.strip() for num in user_input.split(',')]

        #add numbers
        for num in nums:
            sub_total += float(num)
        
        #divide for total
        total = (sub_total / len(nums))
        print(total)

        #ask user if they would like to repeat  
        repeat = input('Would you like to caluate again? Y/N: ')
        if repeat.lower() == 'n':
            break

    except ValueError:
            print('All values must be numbers. Please try again or enter "done" to exit.')

  
   