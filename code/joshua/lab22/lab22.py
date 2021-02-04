import math

'''////////////////////////DICTIONARY////////////////////////'''
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'},
    15: {'ages': '18-22', 'grade_level':      'College'},
    16: {'ages': '18-22', 'grade_level':      'College'},
    17: {'ages': '18-22', 'grade_level':      'College'},
    18: {'ages': '18-22', 'grade_level':      'College'},
    19: {'ages': '18-22', 'grade_level':      'College'},
    20: {'ages': '18-22', 'grade_level':      'College'},
}

'''///////////////////OPENING/READING TEXT///////////////////'''
with open('getty_bliss.txt', 'r') as f:
    contents = f.read()
    # print(contents)

    words = len(contents.split(' '))   ## counts and totals words in text
    # print(words)

    character_amount = 0
    characters = contents.split()     ## counts and total characters in text
    for i in range(len(contents)):
        character_amount = character_amount + 1
        # print(character_amount)

    sentences = contents.count(".")    ## counts all sentences in text
    # print(sentences)

'''/////////SOLVING FOR ARI/////////'''
solve = 4.71 * (character_amount / words) + 0.5 * (words / sentences) - 21.43
round_up = math.ceil(solve)
# print(round_up)

if round_up in ari_scale:
    grade_level = ari_scale[round_up]['grade_level']
    ages = ari_scale[round_up]['ages']

'''///////PRINTING ANSWERS///////'''
print(f'\nARI: {round_up}')
print(f'Recommended for {grade_level} students between {ages} years old.')
