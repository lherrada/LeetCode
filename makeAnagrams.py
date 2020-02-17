#!/usr/local/bin/python3
#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

#Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

#Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

#Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

#For example, if  and , we can delete  from string  and  from string  so that both remaining strings are  and  which are anagrams.

#Level: Easy

word1 =  input("Word1: ")
word2 = input("Word2: ")

print(word1,word2)

H={}
for i in word1:
    H.setdefault(i,0)
    H[i]+=1


for i in word2:
    H.setdefault(i,0)
    H[i] -= 1

sum=0
for i in H.values():
    sum+=abs(i)

print("Result: ", sum)
