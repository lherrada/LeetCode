#!/usr/bin/python3
# Facebook logo stickers cost $2 each from the company store. I have an idea.
# I want to cut up the stickers, and use the letters to make other words/phrases.
# A Facebook logo sticker contains only the word 'facebook', in all lower-case letters.
#
# Write a function that, given a string consisting of a word or words made up
# of letters from the word 'facebook', outputs an integer with the number of
# stickers I will need to buy.
#
# get_num_stickers('coffee kebab') -> 3
# get_num_stickers('book') -> 1
# get_num_stickers('ffacebook') -> 2
#
# You can assume the input you are passed is valid, that is, does not contain
# any non-'facebook' letters, and the only potential non-letter characters
# in the string are spaces.

word=list("facebook")

myinput="ccooffee"

#Initializing dict with one sticker
FB={}
for i in word:
    FB.setdefault(i, 0)
    FB[i] +=1

#Adding one sticker when I run out of letters
def getnewsticker():
    for key in FB.keys():
        FB[key] += 1

print(FB)
sticker_count=1
for i in myinput:
    FB[i]=FB[i]-1
    if FB[i] == -1 :
        getnewsticker()
        sticker_count+=1


print("Your word: ",myinput)
print("Number of required stickers: ",sticker_count )
