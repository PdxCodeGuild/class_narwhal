'''
Lab 18
Version 1
Peaks and Valleys
'''


# Dictionary of test data
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# Generate list of peak indices
def peaks(data):
    peaks = []
    for p in range(1,len(data)-1):
        before = data[p-1]
        current = data[p]
        after = data[p+1]
        if before < current > after:
            peaks.append(p)
    return peaks


# Generate list of valley indices
def valleys(data):
    valleys = []
    for v in range(1,len(data)-1):
        before = data[v-1]
        current = data[v]
        after = data[v+1]
        if before > current < after:
            valleys.append(v)
    return valleys


# Combine the two lists into one
def peaks_and_valleys(peaks, valleys):
    return sorted(peaks(data) + valleys(data))

print(data)
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(peaks, valleys))
