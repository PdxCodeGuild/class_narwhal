# Lab 18: Peaks and Valleys
# Richard 
# Feb 2nd, 2021

'''
Define the following functions:

1. `peaks` - Returns the indices of peaks. A peak has a lower number on both the left and the right.

1. `valleys` - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

1. `peaks_and_valleys` - uses the above two functions to compile a single list of the peaks and 
valleys in order of appearance in the original data.

Visualization of test data:

| Data    |  1 | 2 | 3 | 4 | 5 | 6 | 7 | 6 | 5 | 4 | 5 | 6 | 7 | 8 | 9 | 8 | 7 | 6 | 7 | 8 | 9 |
|---------|----|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Index   |  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20|
| POI     |    |   |   |   |   |   | P |   |   | V |   |   |   |   | P |   |   | V |   |   |   |


Example I/O:
```python
                                                      X                 X
                                                   X  X  X           X  X
                              X                 X  X  X  X  X     X  X  X
                           X  X  X           X  X  X  X  X  X  X  X  X  X
                        X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
                     X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
                  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
               X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
            X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
>>> peaks(data)
[6, 14]
>>> valleys(data)
[9, 17]
>>> peaks_and_valleys(data)
[6, 9, 14, 17]
```
'''
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(f"Data: {data}")
# print(range(len(data)))

length_of_data = len(data)
# indices = range(length_of_data)
#print(f"Indicies: {indices}")

# data2 = dict(zip(indices, data))
# print(f"Index and Data: {data2}")



# Problems in the function below
def peaks(x):
   peaks = []
   for a, b in enumerate(x):
      print(a, b)
      if a == 0 or a == len(x):
         pass
      
      elif b > x[a - 1] and b > x[a + 1]:
         peaks.append(a)
   return(peaks)

 


peaks(data)





# valleys
def valleys(input):
   print("1")

# valleys(data)


# peaks and valleys
def peaks_and_valleys(input):
   print("1")

# peaks_and_valleys(data)






'''
# peaks
def peaks(input):
   length = len(input)
   points_to_check = range(1,length-1)
   print(f"points_to_check - {points_to_check}")

   # is the number bigger than the one that came before it and after it?
   for points_to_check in input:
      if ((input[points_to_check] > input[points_to_check -1]) and (input[points_to_check] > input[points_to_check +1])):
         print(points_to_check, "peak")
      else:
         print("not a peak")

   # output something
   # print(points_to_check)



   print(f"length of data {length}")
'''







'''
## Version 2 (optional)

Using the `data` list above, draw the image of `X`'s above.

## Version 3 (optional)

Imagine pouring water into onto these hills. 
The water would wash off the left and right sides, but would accumulate in the valleys. 
Below the water is represented by `O`'s. Given `data`, calculate the amount of water that would be collected.

```
                                                  X  O  O  O  O  O  X
                                               X  X  X  O  O  O  X  X
                          X  O  O  O  O  O  X  X  X  X  X  O  X  X  X
                       X  X  X  O  O  O  X  X  X  X  X  X  X  X  X  X
                    X  X  X  X  X  O  X  X  X  X  X  X  X  X  X  X  X
                 X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
              X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
           X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
        X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

```
'''