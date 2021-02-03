def peaks(data, LOL):
    temp = []
    for i in range(LOL):
        if LOL > i > 0 and data[i-1] < data[i] and data[i] > data[i+1]:
            temp.append(i)
    return temp       

def valleys(data, LOL):
    temp = []
    for i in range(LOL):
        if i > 0 and data[i-1] > data[i]: 
            if data[i] < data[i+1] and i < LOL:
                temp.append(i)
    return temp       



def main():

    data = [0, 1, 2, 3, 5, 6, 7, 8, 7, 6, 4, 3, 4, 6, 7, 10, 7,]
    LOL = len(data)
    print(LOL)
    The_peaks = peaks(data, LOL)
    The_Valleys = valleys(data, LOL)
    print("The valleys are at indices: ", The_Valleys)
    print("The peaks are at indices: ", The_peaks)

main()