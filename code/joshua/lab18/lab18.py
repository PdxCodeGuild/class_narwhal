'''
Josh Novac
Lab 20
Python
PDX Code Guild
'''

'''///////////////////////////////////INSTRUCTIONS///////////////////////////////////
1. peaks - Returns the indices of peaks. 
2. valleys - Returns the indices of 'valleys'.
3 peaks_and_valleys - compiles a single list of the peaks and valleys in order
'''

'''
/////////////////////////////////// DEFINED FUNCTIONS ///////////////////////////////////'''
# a peak has a lower number on both the left and the right.
def peaks():
    peak = []
    for i in range(len(data) - 1):
        if data[i - 1] < data[i] > data[i + 1]:  # 6, 7, 6   |   8, 9, 8
            peak.append(i)
    print(peak)
    return

# a valley is a number with a higher number on both the left and the right
def valleys():
    valley = []
    for i in range(len(data) - 1):
        if data[i - 1] > data[i] < data[i + 1] and i != 0:  # 5, 4, 5   |   7, 6, 7
            valley.append(i)
    print(valley)
    return
# a single list of the peaks and valleys in order
def peaks_and_valleys():
    peaks_and_valleys = []
    for i in range(len(data) - 1):
        if data[i - 1] < data[i] > data[i + 1]:
            peaks_and_valleys.append(i)
        if data[i - 1] > data[i] < data[i + 1] and i != 0:
            peaks_and_valleys.append(i)
    print(peaks_and_valleys)
    return

'''/////////////////////////////////// DATA ///////////////////////////////////'''
# data and index w/ each peak and valley
'''                       P        V                   P           V         '''
index= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5,  6,  7,  8,  9,  8,  7,  6,  7,  8,  9]

'''/////////////////////////////////// RUN CODE ///////////////////////////////////'''
# running each defined function
peaks()
valleys()
peaks_and_valleys()