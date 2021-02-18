# Lab 22: Compute Automated Readability Index
# Richard
# Feb 3rd, 2021

import string
import math

# 0. Define the file to read in
file = 'book.txt'


# 1. Read in the file 

with open(file, 'r') as f:
    book = f.read()
# print(book)


# 2. Count the number of characters
characters = 0
for letter in book:
    if letter in string.ascii_letters:
        characters += 1
print(f"Number of characters: {characters}")




# 3. Count the number of words
words = len(book.split()) 
print(f"Number of words: {words}")


# 4. Count the number of sentences
sentences = len(book.split(".")) 
print(f"Number of sentences: {sentences}")

# 5. Calcuate the index
'''
The score is computed by 
multiplying the number of characters 
divided by the number of words by 4.17, 
adding the number of words divided by the number of sentences multiplied by 0.5, 
and subtracting 21.43. 

**If the result is a decimal, always round up.** 
Scores greater than 14 should be presented as having the same age and grade level as scores of 14. 
'''

score = math.ceil(4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43)

print(f"The readability score is: {score}")

# 6. Use the following dictionary to look up the grad level

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

big = ari_scale[score]
# print(f"big: {big}")

ages = big.get('ages')
# print(f"ages: {ages}")

grade_level = big.get('grade_level')
# print(f"grade - level: {grade_level}")

# The output should look something like the following:
'''

    --------------------------------------------------------

    The ARI for gettysburg-address.txt is 12
    This corresponds to a 11th Grade level of difficulty
    that is suitable for an average person 16-17 years old.

    --------------------------------------------------------

'''
print(" ")
print(f"The ARI for {file} is {score}")
print(f"This corresponds to a {grade_level} level of difficulty")
print(f"that is suitable for an average person {ages} years old.")
print(" ")



'''
Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for 
computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:

![ARI Formula](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/878d1640d23781351133cad73bdf27bdf8bfe2fd)

The score is computed by multiplying the number of characters divided by the number of words by 4.17, 
adding the number of words divided by the number of sentences multiplied by 0.5, 
and subtracting 21.43. **If the result is a decimal, 
always round up.** Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

Scores correspond to the following ages and grad levels:

```
    Score  Ages     Grade Level
     1       5-6    Kindergarten
     2       6-7    First Grade
     3       7-8    Second Grade
     4       8-9    Third Grade
     5      9-10    Fourth Grade
     6     10-11    Fifth Grade
     7     11-12    Sixth Grade
     8     12-13    Seventh Grade
     9     13-14    Eighth Grade
    10     14-15    Ninth Grade
    11     15-16    Tenth Grade
    12     16-17    Eleventh grade
    13     17-18    Twelfth grade
    14     18-22    College
```
'''