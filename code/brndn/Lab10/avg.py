'''
=-=-= Lab10  27 Jan 2021 =-=-=
=-=-=- Number Averagator =-=-=
=-=-=- Composer: brndn =-=-=-=
'''

#Version One
'''
nums = [5, 0, 8, 3, 4, 1, 6]
total = 0

for n in nums:
    total = total + n

print(total / len(nums))
'''

#Version Two

nums = []     #empty list for storing numbers entered
n = 0         #input placeholder
total = 0     #starting total

print("\nGet Averagated!\n")

while str(n) != 'done':    #loop until input is "done"
    n = input('\n Enter a number\n      -OR-\n"done" to average\n\n  >>> ')
    
    if n != "done":   #if "done", skip. if not "done"... 
        try:
            nums.append(float(n))        #if input is a number (can be converted to a float) add it to the nums list

        except ValueError:
            print("\n\N{SKULL}ILLEGAL ENTRY!\N{SKULL}")    #if input is not a number or "done", tell user and repeat loop


for n in nums:
    total = total + n      #iterate nums list and create a total

try:
    avg = total / len(nums)    #divide total by nums list length to create average

    print(f"\n\N{THUMBS UP SIGN}{avg}\N{THUMBS UP SIGN}\n")

except ZeroDivisionError:
    print("\nThanks! \N{WAVING HAND SIGN}\n")
