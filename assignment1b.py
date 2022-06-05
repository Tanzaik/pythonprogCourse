#
# assignment1b.py
#
# Tanzim Amin
# 06/04/22
# The program takes a sentence as contribution from the client and
# afterward parts it into a rundown of words utilizing the split() work.
# The len() work is then used to compute the length of the rundown, which relates to the quantity of words in the sentence.
# Lastly, the program prints the quantity of words as result.

def countWords(sentence):
# To take multiple inputs from user
# split() splits the string into substrings
# and returns it in the form of a list 

    sentenceList = sentence.split()
    return len(sentenceList)
# Driver code
    sentence = 'hello  how  are  you.'
    print(countWords(sentence))