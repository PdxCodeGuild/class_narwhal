# ---- Lab 18 ---- #

# - Peaks and Valleys - #

# Data to be run through
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# Function to find peaks
def peaks(x):
    peaks = [] # output list of the function
    for i in range(1, len(x) -1): # to keep the range between the indices of 1 and -1 of the input list
        if data[i] == 0 and data[i] == len(x):
             pass # if the indices are on the end, pass by them
        if x[i - 1] < x[i] > x[i + 1]: # if there is a number with lower numbers on either side, that is a peak
             peaks.append(x[i]) # append that number to the functions output list
    return peaks # return the output function

print(f'The Peaks are: {peaks(data)}')

# Function to find Valleys: Inverse of Peaks function
def valleys(x):
    valleys = []
    for i in range(1, len(x) -1):
        if data[i] == 0 and data[i] == len(x):
             pass
        if x[i - 1] > x[i] < x[i + 1]: # if there is a number with lower numbers on either side, that is a peak
             valleys.append(x[i])
    return valleys 

print(f'The Valleys are: {valleys(data)}')

# Function to combine Peaks and Valleys into one list
def peaks_and_valleys(x):
    for num in valleys(x), peaks(x): # for the numbers in the function output lists
        return (valleys(x) + peaks(x)) # taking the lists and putting them into on list

print(f'The Peaks and Valleys are: {peaks_and_valleys(data)}')