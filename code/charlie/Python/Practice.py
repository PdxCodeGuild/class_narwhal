# def is_even(a):
#     if a % 2 == 0:
#         return True 
#     return False

# def opposite(a,b):
#     if a >= 0 and b < 0:
#         return True
#     elif b >= 0 and a < 0:
#         return True
#     else:
#         return False

def near_100(num):
    if num >= 90 and num <= 110:
        return True
    return False

def main():

#    truth = is_even(26) 
#    print(truth)

    # verdict = opposite(-3457, 2342)
    # print(verdict)

    verdict = near_100(90)
    print(verdict)



main()