# Word dictionary using python dictionary library
# Make sure to install nltk and download wordnet before running this file
    # import nltk
    # nltk.download('wordnet')

from nltk.corpus import wordnet

def define(word):
    if wordnet.synsets(word):
        definition = wordnet.synsets(word)[0].definition()
        print("Definition of", word,'is:', definition)
    else:    
        print('Word unavailable!')

word_to_define = input('Enter a word to define: ')
define(word_to_define)