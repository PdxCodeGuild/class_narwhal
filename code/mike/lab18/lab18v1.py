'''
Lab 18
Version 1
Peaks and Valleys
'''


# Dictionary of test data
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# Generate list of peak indices
peaks = []
for p in range(1,len(data()-1):
    before = data[p-1]
    current = data[p]
    after = data[p+1]
    if before < current > after:
        peaks.append(p)
print(peaks)

# Generate list of valley indices
valleys = []
for v in range(len(data[0:-1])):
    before = data[v-1]
    current = data[v]
    after = data[v+1]
    if before > current < after:
        valleys.append(v)
print(valleys)

# Combine the two lists into one
peaks_and_valleys = peaks + valleys

print(peaks_and_valleys)