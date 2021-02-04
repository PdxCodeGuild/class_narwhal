# Lab 21: Count Words
# Richard
# Feb 4th, 2021

# libraries
import string
from collections import Counter

'''
Let's write a python module to analyze a given text file containing a book for its vocabulary frequency 
and display the most frequent words to the user in the terminal. 
Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), 
try to find rules that work best.

Find a book on [Project Gutenberg](http://www.gutenberg.org).
Download it as a UTF-8 text file.
'''
# 1. Define the file to read in
file = 'book.txt'


# 2. Open the file.
with open(file, 'r') as f:
    book = f.read()
#print(book)


#3 . Clean it up

# Make everything lowercase
book = book.lower()
#print(book)

# strip punctuation
translator = str.maketrans('', '', string.punctuation)
book = book.translate(translator) # I am a string with punctuation
# print(book)

# split book into a list of words
book = book.split()
# print(book)

# 4. Turn the list of words into a dictionary
'''
Your dictionary will have words as `keys` and counts as `values`. If a word isn't in your dictionary yet, 
add it with a count of 1. If it is, increment its count.
'''
# word_dict is a dictionary where the key is the word and the value is the count
word_dict = Counter(book)
# print(word_dict)


# 5. Print the most frequent 10 words and their counts. 
'''
for word, count in word_dict.most_common(10):
    print(f"{word}: {count}")
'''

# 6. Remove the stop words

STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", 
"you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 
'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 
'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 
'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 
'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 
'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 
'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 
'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 
'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 
'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', 
"doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 
'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', 
"weren't", 'won', "won't", 'wouldn', "wouldn't"]

for word in STOPWORDS:
    if word in word_dict.keys():
        del word_dict[word]
#print(word_dict)



# 7. Print the most frequent 10 words and their counts again (without the stopwords in)
print("Ten most frequent words with stop words removed")
for word, count in word_dict.most_common(10):
    print(f"{word}: {count}")




## Version 2 (optional)

# Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.













## Version 3 (optional)

#Let the user enter a word, then show the words which most frequently follow it.
