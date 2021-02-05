import re
import math
import os

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

#parse data from file
f = open("gettysburg_address.txt")
text = f.read()
f.close


#split text into sentences. Imported "re" above for regex. Passed in regular expression for splitting
#at a sentence and passed in the thing to split. Docs found here 
#https://note.nkmk.me/en/python-split-rsplit-splitlines-re/
# and here https://stackoverflow.com/questions/25735644/python-regex-for-splitting-text-into-sentences-sentence-tokenizing

sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
sentence_count = len(sentences)

#break into words
words = text.split()
word_count = len(words)

#remove line breaks
no_linebreak = text.strip()

#remove spaces
no_space = no_linebreak.replace(" ", "")

#break into chars
chars = list(no_space.strip())
char_count = len(chars)

#math (s) sentence count, (w) word count, (c) char count
def ari(s, w, c):
    #do math
   score = (4.17 * (c / w)) + (0.5 * (w / s)) - 21.43
   #round
   score = math.ceil(score)
   return score

#get the numeric score using the function and save in a variable 
numeric_score = (ari(sentence_count, word_count, char_count))

#round it
values=(ari_scale[numeric_score])

#print it usine multiline f string
print(f"""
--------------------------------------------------------

The ARI for {f.name} is {numeric_score}
This corresponds to a {values['grade_level']} level of difficulty
that is suitable for an average person {values['ages']} years old.

--------------------------------------------------------
""")
