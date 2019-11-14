#Norma
#count_sentences.py
import re
FILENAME = 'alice.txt'
fvar = open (FILENAME, 'r') # open file for reading
with open('alice.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
allwords = [] # accumulate the words in this list

for aline in fvar:
    aline = aline.lower()
    if aline is '?':
        words = aline.split('?')
        # if words.count("'") %2==0:
        #     allwords.extend(words) # add all words in this line to allwords
        #     print(allwords)
        # else:
        #     words.join()
        allwords.extend(words)
    elif aline is '!':
        words = aline.split('!')
        # if words.count("'") %2==0:
        #     allwords.extend(words) # add all words in this line to allwords
        #     print(allwords)
        # else:
        #     words.join()
        allwords.extend(words)
    elif aline is '.':

        words = aline.split('.')
        # if words.count("'") %2==0:
        #     allwords.extend(words) # add all words in this line to allwords
        #     print(allwords)
        # else:
        #     words.join()
        allwords.extend(words)
# new_allwords = [] # accumulate the words in this list
# for aline in allwords:
#     aline = aline.lower()
#
#     if len(aline) ==1:
#         aline = aline.replace("'", " ")
#     elif aline[:1] is "'" or aline[-1:] is "'":
#             aline = aline.replace("'", ' ')
#             aline = aline.replace("tis", "'tis")
#     words = aline.split() # splits the line on whitespace (blanks, '\n', '\t')
#     new_allwords.extend(words)


allwords.sort()

print(allwords)


fvar.close()


