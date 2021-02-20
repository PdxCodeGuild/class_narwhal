'''
=-=-=- Lab22 03 Feb 2021 -=-=-=
= Automated Readability Index =
=-=-=-= Composer: brndn =-=-=-=
'''

import string

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
    14: {'ages': '18-22', 'grade_level':      'College'}
}

dot_txt = 'walden.txt'

with open(dot_txt, 'r') as filetxt:
    text_to_ari = filetxt.read()

number_of_characters = len(''.join(character for character in text_to_ari if character.isalnum()))

number_of_words = len(text_to_ari.split())

number_of_sentences = len(text_to_ari.split('.'))

ari = round(((number_of_characters / number_of_words) * 4.71) + ((number_of_words / number_of_sentences) * .5) - 21.43)

age = ari_scale[ari]['ages']

grade_level = ari_scale[ari]['grade_level']

print(f'\nThe ARI for {dot_txt} is {ari}.\nDifficulty Level: {grade_level}\nRecommended for ages {age}.\n')