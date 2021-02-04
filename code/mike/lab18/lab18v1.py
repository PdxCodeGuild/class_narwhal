'''
Lab 18
Version 1
Peaks and Valleys
'''



data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]



for i in range(len(data)):
    bi = data[i] - 1
    ni = data(i)
    ai = data(i) + 1
    if bi < ni > ai:
        print(bi,ni,ai)

# for p in data:
#     bp = data[p] - 1
#     np = data[p]
#     ap = data[p] + 1
#     if bp < np < ap:
#         print(bp,np,ap)