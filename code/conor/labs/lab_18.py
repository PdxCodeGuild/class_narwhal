# ---- Lab 18 ---- #

# - Peaks and Valleys - #

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(num):
    the_peaks = []
    for i in len(data[1:-1]):
        if data[i - 1] < data[i] > data[i + 1]:
            the_peaks.append(i)
    return the_peaks

print(peaks(data))

#def valleys(num):
#    the_valleys = []
#    for i, num in enumerate(data):
#        if data[i - 1] > data[i] < data[i + 1]:
#            the_valleys.append(i)
#    return the_valleys  

#print(valleys(data))

#def peaks_and_valleys(data):
    
#print(peaks_and_valleys(data))