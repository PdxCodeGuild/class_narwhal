'''
=-=-= Lab18 02 Feb 2021 =-=-=
=-=- Peaks & Valleys V.1 -=-=
=-=-=- Composer: brndn -=-=-=
'''

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(x):
    peakis = []
    for i, d in enumerate(x):
        try:
            if d > x[i-1] and d > x[i+1]:
                peakis.append(i)
        except IndexError:
            pass
    return peakis

def valleys(x):
    valleyis = []
    for i, d in enumerate(x):
        try:
            if d < x[i-1] and d < x[i+1] and i != 0:
                valleyis.append(i)
        except IndexError:
            pass
    return valleyis
       
def peaks_and_valleys(x):
    return sorted(peaks(x) + valleys(x))
        
print(peaks(data), valleys(data), peaks_and_valleys(data))        