#!/usr/bin/python

#Part 1
# Generate a string of 100 character (randomly using lowercase english alphabet,
# #with spaces 7/33 probability, all other 26 alphabet characters 26/33 probability)
# Print generated string to standard output.

#Part 2
# Find words where all characters are unique (no duplicate characters).
# Print words to standard output. Hint: “aa” and “aba” are not unique, “abc” is.

#Part 3
# Find the word(s) which contains the most of the other words as a substring.
# Print those word(s) to standard output. Hint: If the input string is
# “pear appear appear ear hear bear pea” then the output should be [“appear”,“appear”].

#Level: Easy

import string
import random
import re


#Part 1

alphabet = string.ascii_lowercase
alphabet = f'{alphabet}' + ' ' * 7
pool = [random.choice(alphabet) for i in range(100)]
pool = ''.join(pool)
#pool = "pear appear appear ear hear bear pea"
print(pool)
print("====================")

#Part 2

words = re.split(r'\W+',pool)

for i in words:
    unique =[i for i in words if len(i) == len(set(i)) and len(i) > 0]

print("Word with unique characters: ", unique)

print("====================")
#Part3
X = [ (word, len([substring for substring in words if substring in word])) for word in words if len(word) > 0]
mymax = sorted(X, key=lambda i: i[1], reverse=True)[0][1]
print([ i[0] for i in X if i[1] == mymax])
