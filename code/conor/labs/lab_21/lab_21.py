# ---- Lab 21 ---- #

# - Count Words - Sherlock Holmes - #

import string

f = open('sherlock.txt', encoding ='utf-8')
sherlock = f.read()
f.close()

# taking out punctuation
translator = str.maketrans('', '', string.punctuation)
words_only = sherlock.translate(translator)

# Function to send words only text into a function with keys : values
def count_dict(x):
    count_dict = {}
    for word in x.split():
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] +=1
    return count_dict
    
# print(count_dict(words_only))

# Converting the Function incl. Sherlock to a manageable variable
word_count = count_dict(words_only)

# Printing out the Top 10 words
words = list(word_count.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
