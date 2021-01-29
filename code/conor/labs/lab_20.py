# ---- Lab 13 ---- #

# - Credit Card Validation - #

card_num = '4556737586899855'

card_list = [(x) for x in card_num]
card_list = list(map(int, card_list))
print(card_list)

check = card_list[-1]
print(check)

card_list = card_list[:-1]
print(card_list)