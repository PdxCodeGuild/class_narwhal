import numpy as np

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peaks_and_valleys = []

def find_peaks(data):
    peaks = []
    for i, num in enumerate(data):
        try:
            before = data[i - 1]
            after = data[i + 1]
            if num > before and num > after:
                peaks.append(num)
        except IndexError:
            break
    return peaks

def find_valleys(data):
    valleys = []
    for i, num in enumerate(data):
        try:
            before = data[i - 1]
            after = data[i + 1]
            if num < before and num < after:
                valleys.append(num)
        except IndexError:
            break
    return valleys

def peaks_and_valleys(data):
    p = find_peaks(data)
    v = find_valleys(data)
    #combine the two lists into a single list of tuples
    lt = list((zip(p, v)))
    #use list comprehension to put each num into a list from the list of tuples.
    #num is the output in the new list. T is the tuple in the list of tuples.
    #lt is the list of tuples. Finally target the number in each individual tuple.
    output = [num for t in lt for num in t]
    

    return output

print(peaks_and_valleys(data))
print(data.shape(len(data), 1))


# for num in data:
#     y = (f"{num} {(num * 'x')}")
#     print(np.rot90(y, 0, 1))
