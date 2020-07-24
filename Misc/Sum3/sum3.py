"""
https://leetcode.com/problems/3sum/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0
 Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

solution:
Time complexity: O(n^2)
No sort required.
We split the sum3 problem into several sum2 problems
For solving the sum2 problem , I used the complement logic.
Code below is self explanatory
For avoiding duplicates, I am sorting each triplet for a solution and 
adding it to a set.
"""


def sum2(array, mysum):
    H = {}
    solution = {}
    for num in array:
        if num in H:
            solution[num] = mysum - num
        else:
            H[mysum - num] = num

    return [(i, j) for (i, j) in solution.items()]


def sum3(array, mysum):
    result = set()
    size = len(array) - 2
    track = []
    for i in range(size):
        num = array.pop(0)
        if num in track:
            continue
        track.append(num)
        solution = sum2(array, mysum - num)
        solution = [tuple(sorted((num,) + j)) for j in solution]
        for k in solution:
            result.add(k)
    return result


a = [-1, 0, 1, 2, -1, -4]
suma = 0
print(sum3(a, suma))
