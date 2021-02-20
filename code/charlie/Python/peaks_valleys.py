import random

def peaks(data, LOL):
    temp = []
    for i in range(1, LOL-1): # or range(1, len(data)-1)
        Previous = data[i-1]
        Current = data[i]
        Next = data[i+1]
        if Previous < Current > Next: 
            temp.append(i)
    return temp       

def valleys(data, LOL):
    temp = []
    for i in range(1, LOL-1): # or range(1, len(data)-1)
        Previous = data[i-1]
        Current = data[i]
        Next = data[i+1]
        if Previous > Current < Next: 
            temp.append(i)
    return temp       



def main():
    data = []
    for i in range(0, 200):
        data.append(random.randint(0, 100))

    LOL = len(data)
    The_peaks = peaks(data, LOL)
    The_Valleys = valleys(data, LOL)
    print("\nThe valleys are at indices: \n", The_Valleys)
    print("\nThe peaks are at indices: \n", The_peaks)
    print("\nHere is the set of data these stats. were derived from: \n\n", data)
main()