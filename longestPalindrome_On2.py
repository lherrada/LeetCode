#!/usr/local/bin/python3
#Given a string s, find the longest palindromic subsequence's length in s.
#https://leetcode.com/problems/longest-palindromic-substring/
# You may assume that the maximum length of s is 1000.

#Level: intermediate
# Complexity: O(n^2)

#The script build a moving window from index 0 to index len(word) - 1
#For each iteration, the moving window tries to expand to the left and to the right.
#There are two types of moving window, one that consider a palindrome with a center character
#which does not repeat. And another palindrome that is perfectly simmetrical. The one with the longest
# length is saved (actually just the indexes are saved).



def expandFromMiddle(word,left,right):
   if len(word) == 0 or left > right:
       return 0

   while left >= 0 and right < len(word) and word[left] == word[right]:
     left-=1
     right+=1

   return right -left - 1


def longestPalindrome(word):
    wordlen=len(word)

    if len(word) < 1 or word is None:
        return ""

    start=0
    end=0
    for i in range(0,wordlen):
        len1 = expandFromMiddle(word,i,i)
        len2 = expandFromMiddle(word,i,i+1)
        lenf = max(len1,len2)
        if lenf > end - start:
           start = int(i - (lenf -1)/2)
           end = int(i + (lenf)/2)

    return word[start:end+1]

#Complexity: O(n^2)
word="abbappbacccpccc"

print(longestPalindrome(word))

