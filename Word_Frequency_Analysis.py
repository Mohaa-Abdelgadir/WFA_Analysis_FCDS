# # Word Frequency Analysis

## 1- Importing necessary libraries & reading the file


import re # for splitting the string
import nltk # for stopwords removal
from nltk.corpus import stopwords
nltk.download('stopwords')

# Saving the text as a string variable

# 'with' keyword handles external resources management
# 'open' opens the file for reading
# '.read()' reads the contents of a file
with open("random_paragraphs.txt") as file:
    text = file.read()


## 2- Splitting the string into a list of words, and removing the stop words (i.e. the, as, are..etc.)

# using re.split() to split the words seperated by spaces, new lines, and punctuation marks
words_list = re.split(r'[ \n.,;!?\(\)\[\]\{\}\'\"]+', text)
words_list = words_list[:-1] # Last element is a whitespace
print('Number of words Including stop words): ', len(words_list))
print('First 20 words:')
print(words_list[:20])
print('Last 20 words:')
print(words_list[-20:])


# Removing the stop words
stop_words = stopwords.words('english')
print('Number of stop words: ', len(stop_words))
print('List of the current stop words: ')
print(stop_words)

filtered_words_list = [word for word in words_list if word.lower() not in stop_words]
print('Number of words after removing stop words: ', len(filtered_words_list))
print('First 20 words:')
print(filtered_words_list[0:20])
print('Last 20 words:')
print(filtered_words_list[-20:])


## 3- Counting each word's frequency

# We start with an empty dictionary. Looping through the words list, if the word has not been added to the dictionary, we add it
# and set its value (frequency) to 1. If the word exists, we increment its value (frequency) by 1.
words_freqs = {}
for word in filtered_words_list:
    if word in words_freqs.keys():
        words_freqs[word]+=1
    else:
        words_freqs[word]=1
        
print('Number of unique words: ', len(words_freqs))


## 4- Displaying the word frequencies
top_words = [word for word in words_freqs.keys() if words_freqs[word]>500]
print('Number of words occuring more than 500 times: ', len(top_words))
print('List of words occuring more than 500 times:')
print(top_words)


# Allowing the user to see the frequency of their chosen word
choice = input("Enter a word to check its frequency (type: 'let me go' to exit): ")

while choice != 'let me go':
    found = False
    for word in words_freqs.keys():
        if word == choice:
            print(f'Frequency of "{word}" is:', words_freqs[word])
            found = True

    if not found:
        print(f"The word {choice} was not found")
        
    choice = input("Enter a word to check its frequency (type: 'let me go' to exit): ")