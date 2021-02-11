
# The Peak and the Valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peaks = []
    print(data)
    #return data
    
    for x in range(len(data)):
        #print(data[x])
        if data[x] == 1:
            pass
           #print(True)

            if range(data[x])== 0:
                print(data[x])
    


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]



for i, in range(1, len(data) -1):
  # note i forgot about this little trick when we were on the call, if you use range you can tell it where to start and where to end. they syntax is (from where in what to where) so here it is from 1 because we dont want index 0 and for the whole lenght of data but dont use the last num and that is -1
  if data[i] > data[i-1] and data[i]>[i+1]:
    # in this we are checking the data value to see if it is greater than the thing to the left i-1 and greater than the thing on the right i+1
    print("peak")



peaks(data)







#def valleys(data):
     





#print(data)