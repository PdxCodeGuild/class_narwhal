import math

def main():
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

    try:
        f = open("gettys.txt")
        contents = f.read()
        words = contents.split()
        sentences = contents.split('.')
        chars = "".join(words)
        
        print("The number of words in the Gettysburg Address = ", len(words)-1)    
        print("The number of characters in the Gettysburg Address = ", len(chars)-1)
        print("The number of sentences in the Gettysburg Address = ", len(sentences)-1)
    except (IOError, OSError) as e:
        print(e)
    finally:
        f.close()
    
    num_words = len(words)-1
    num_chars = len(chars)-1
    num_sent = len(sentences)-1

    ARI = (4.71*(num_chars/num_words) + 0.5*(num_words/num_sent))-21.43
    ARI = math.ceil(ARI)

    if ARI <= 14:
        AG_level = ari_scale.get(ARI)
        ages = AG_level['ages']
        grade_lev = AG_level['grade_level']

        print(f'''\n\tThis text has Automated Readability Index rating of: {ARI}\n 
        This corresponds to a {grade_lev} level of reading difficulty.\n
        That is suitable for a person ages {ages} years old.
            ''')
    else:
        print(f'''\n\tThis text has Automated Readability Index rating of: {ARI}\n 
        This corresponds to a College level of reading difficulty.\n
        That is suitable for a person ages 18-22 years old.
        ''')

main()