'''
nci programme: BSHDS 
program: count and display words
author: Renato Gusani
studentID: x19411076
date: 06/05/2020

'''
from collections import Counter, defaultdict # Counter is a subclass of Dictionary and used to keep track of elements and their count

# creating word list to input into a file
wordslist = ['There is a theory that our world is simulated, Elon Musk is Ironman and Ironman is a fictional character, Therefore nothing is real']

# inserting the word list onto a text file
with open('freqwords.txt', 'w') as filehandle:
    for listitem in wordslist:
        filehandle.write('%s\n' % listitem)


# Opening the file in read mode 
text = open("freqwords.txt", "r") 
  
# Creats empty dict
wordfreqdictionary = dict() 
  
# Loops through every line in file 
for line in text: 
    # Removes spaces and newlines 
    line = line.strip() 
  
    # Converts characters to lowercase
    line = line.lower() 
  
    # Split the line into words 
    words = line.split(" ") 
  
    # Iterates each word in line 
    for word in words: 
        # Check if the word is already in dict 
        if word in wordfreqdictionary: 
            # Increments count of word by 1 
            wordfreqdictionary[word] = wordfreqdictionary[word] + 1
        else: 
            # Adds word to dictionary with a count 1 
            wordfreqdictionary[word] = 1

order = Counter(wordfreqdictionary)

# Finding 10 highest values 
top = order.most_common(10)  
  
# prints entire dictionory 
print(wordfreqdictionary, "\n") 
  
# print top 10 words in dictionary with their frequency
print("Top 10 words with frequency") 
  
for i in top: 
    print(i[0]," :",i[1]," ") 