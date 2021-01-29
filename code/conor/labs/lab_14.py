# ---- Lab 14 ---- #

# - Pick 6 - #

import random

def pick_6():
    rand_list = [random.randint(1, 99) for _ in range(6)]
    return rand_list

print(pick_6())
