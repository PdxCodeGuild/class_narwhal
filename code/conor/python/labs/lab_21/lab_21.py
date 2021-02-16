# ---- Lab 21 ---- #

# - Count Words - Sherlock Holmes - #

# Version 1 #

import string

f = open('sherlock.txt', encoding ='utf-8')
sherlock = f.read()
f.close()

# make all lower case
sherlock = sherlock.lower()

# Take out all punctuation punctuation
translator = str.maketrans('', '', string.punctuation + "“")
words_only = sherlock.translate(translator)

# Below is another way to take out all punctuation

# sherlock = list(sherlock)

# for punc in string.punctuation + "“":
#     while punc in sherlock:
#         sherlock.remove(punc)

# words_only = ''.join(sherlock)


# Function to send words only text into a function with keys : values
def count_dict(x):
    count_dict = {}
    for word in x.split():
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] +=1
    return count_dict
    

# Converting the Function incl. Sherlock to a manageable variable
word_count = count_dict(words_only)

# List of most common words
STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

# taking out the list of most common words
for word in STOPWORDS:
    if word in word_count.keys():
        del word_count[word]

# Printing out the Top 10 words, sans stop words
words = list(word_count.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

# Version 2 (Optional) #


# Version 3 (Optional) #