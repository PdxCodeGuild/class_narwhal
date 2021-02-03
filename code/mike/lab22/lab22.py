'''
Lab 22
Version 1
Compute Automated Readability Index
'''



# Open text file
file_name = '1984.txt'
f = open(file_name)
contents = f.read()


# ARI Scale to determine recommended reading level
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

# Remove all spaces and white space to count characters
content_split = ''.join(contents.split())
characters = len(content_split)


# Removes all white space to count words
words = len(contents.split())


# Count sentence ending punctuation
period = 0
exclamation_point = 0
question_mark = 0 
for punct in contents:
    if punct == '.':
        period += 1
    elif punct == '!':
        exclamation_point += 1
    elif punct == '?':
        question_mark += 1

# Add sentence endings to get sentence count
sentences = period + exclamation_point + question_mark

# Calculate ARI
ARI = int(4.71 * (characters/words) + .5 * (words/sentences) - 21.43)

# Get grade level
grade = ari_scale[ARI]


print('Characters: ', characters)
print('Words: ', words)
print('Periods: ', period)
print('Exclamation Points: ', exclamation_point)
print('Question Marks: ', question_mark)
print('Sentences: ', sentences)
print('Automated Readability Index: ', ARI)

print(f'''
The ARI for "{file_name}" is {ARI}.
This corresponds to a {grade['grade_level']} of difficulty
that is suitable for an average person {grade['ages']} years old.
'''
)