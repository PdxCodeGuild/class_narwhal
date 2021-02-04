'''
=-=-= Lab 21 04 Feb 2021 =-=-=
=-=-=-= Count Words V1 =-=-=-=
=-=-=- Composer: brndn =-=-=-=
'''

import string

with open('walden.txt', 'r') as filetxt:
    walden = filetxt.read().lower()

translator = str.maketrans('', '', string.punctuation)

walden = walden.translate(translator)      #strip punctuation

walden_words = walden.split()              #separate words into list

walden_words_dict = {}                     #dictionary for words

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

for word in walden_words:
    if word in stopwords:                  #ignore stopwords
        continue
    elif word not in walden_words_dict:    #add new words to dictionary
        walden_words_dict[word] = 1
    elif word in walden_words_dict:        #add value(+1) to existing words
        walden_words_dict[word] += 1

words = list(walden_words_dict.items())    #sort words by value (number of occurrences)
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):       #print 10 most frequent words
    print(words[i])
