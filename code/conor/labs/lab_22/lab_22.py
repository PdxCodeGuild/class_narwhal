# ---- Lab 22 ---- #

# - Compute Automated Readability Index - #

import math # to round up
import string # for the Characters function

# importing .txt file with encoding to eliminate weird characters
f = open('gettysburg.txt', encoding ='utf-8')
burg = f.read()
f.close()
# print(burg)

# Find the amount of Words
def words(x):
    count = 0
    x_strip = x.strip()
    for i in x_strip:
        if i == " ":
            count += 1
    return int(count)

# Find the amount of Characters, minus the spaces
def characters(x):
    count = 0
    for let in x:
        if let in string.ascii_letters:
            count += 1
    return int(count)

# Find the number of Sentences. I counted the numbers of periods for this example.
def sentences(x):
    sentences = x.split('.') # I'm aware there are other ways to do this :)
    sentences = len(sentences)
    return int(sentences)

# Changed the functions into more manageable variables
word = (words(burg))
char = (characters(burg))
sent = (sentences(burg))

# ARI equation
ari = (math.ceil((4.71 * (char/word) + 0.5 * (word/sent) - 21.43))) 

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

# saving the numberic score from ARI as a varible to call more easily
score = (ari_scale[ari])

# Print the product for the Gettysburg Address
print(f"""
The ARI for your text is '{ari}'.
This corresponds to a '{score['grade_level']}' level of difficulty
suitable for a person '{score['ages']}' years old.
""")