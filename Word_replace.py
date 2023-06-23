# Using replace funtion of strings

def word_replace():
    string = input('Enter the sentence: ')
    word_to_replace = input('Enter the word to replace: ')

    if word_to_replace not in string:
        print('Word doesn\'t exist in the given sentence!')
    else:
        new_word = input('Enter the replacement:')
        print(string.replace(word_to_replace, new_word))

word_replace()