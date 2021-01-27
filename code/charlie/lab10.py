def main():


    nums = []

    print("Welcome to the average calculator where you can enter as many numbers as you want!")
    choice = input("Please enter a number or \'done\': ")

    if choice != 'done':
        while choice != 'done':
            nums.append(choice)    
            choice = input("Please enter a number or \'done\': ")

        average = 0

        for num in range(len(nums)):
            average += int(nums[num])

        average = average / len(nums)
        print(f"Your average is: {average}")
    print("Have a nice day! :-)")
main()