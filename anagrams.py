#!/usr/local/bin/python3
"""
https://leetcode.com/problems/group-anagrams/
Given an array of strings, group anagrams together.

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Level: Easy

"""
myinput = ["eat", "tea", "tan", "ate", "nat", "bat"]

#First version
H={}
for word in myinput:
    bucket=''.join(sorted(word))
    H.setdefault(bucket,[]).append(word)

print(H)

#Second version: using dictionary comprehension  

J={''.join(sorted(i)) : [j for j in myinput if ''.join(sorted(j)) == ''.join(sorted(i)) ]  for i in myinput}
print(J)

