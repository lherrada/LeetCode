'''
Amazon games have introduced a new mathematical game for kids.
You will be given n sticks and the player is required to form rectangles from those sticks.
Formally, given an array of n integers representing the lengths of the sticks,
you are required to create rectangles using those sticks.
Note that a particular stick can be used in at most one rectangle and
in order to create a rectangle we must have exactly two pairs of sticks with the same lengths.
For example, you can create a rectangle using sticks of lengths (2, 2, 5, 5) and [4, 4, 4, 4)
but not with (3, 3, 5, 8).
The goal of the game is to maximize the total sum of areas of all the rectangles formed.

In order to make the game more interesting, we are allowed to reduce any integer by at most 1.
Given the array sideLengths, representing the length of the sticks,
find the maximum sum of areas of rectangles that can be formed such that each
element of the array can be used as length or breadth of at most one rectangle and
you are allowed to decrease any integer by at most 1. Since this number can be quite large,
return the answer modulo 1000

Example 1:
      The side lengths are given as sideLengths = [2,6,6,2,3,5]
      The lengths 2,2,6 and 6 can be used to form a rectangle of area 2*6 = 12
      No other rectangles can be formed with the remaining lenghts. The answer is
      12 modulo 1000.

Example 2:
    sideLengths = [2,3,3,4,6,8,8,6] ; size n = 8
    Two rectangles can be formed. One has sides of 6 and 6, and the other by reducing 4 and one of
    the 3's by 1 has sides of 2 and 3.
    The total area of these rectangles is (6*8 + 2*3) mod 1000 = 54

Example 3:
    sideLengths = [3,4,5,5,6]; size n = 5
    Explanation
    The rectangle can have either sides of 5 and 3 (reduce 4 by 1), or sides of 5 and 4
    (reduce 6 and one 5 by 1). The second option has a greater area, 5*4 > 3*5
'''

from collections import defaultdict
from collections import Counter


class Solution:
    #My solution. 
    def findArea_Me(self, arr: list[int]):
        MOD = 1000
        freq = defaultdict(int)
        #Counting the number of sticks and storing on a dict (map)
        for key in arr:
            freq[key] += 1

        #For an even number of sticks, do not modify the frequency map.
        #For an odd number of sticks, reduce that frequency in 1, to make it even.
        #That extra stick is useless.
        #Considering reducing in one the length of the stick. If there is another stick with
        #same length add it to such frequency

        keysSorted = sorted(freq.keys(), reverse=True)
        for key in keysSorted:
            if freq[key] % 2 == 0: continue
            freq[key] -= 1
            keyTemp = key - 1
            if keyTemp in freq:
                freq[keyTemp] += 1

        #Sticks with frequency less than 2 are removed
        freq = {i: freq[i] for i in freq.keys() if freq[i] > 1}
        pairs = []

        for key in sorted(freq.keys(), reverse=True):
            while freq[key] > 0:
                freq[key] -= 2
                pairs.append(key)

        area = 0
        #Calculate maximum area from the pairs array.
        if len(pairs) % 2 == 1: pairs.pop()
        for i in range(0, len(pairs), 2):
            area += pairs[i] * pairs[i + 1]
        return area % MOD

    #CHat GPT version: it does not work for all test cases
    def findArea_ChatGPT(self, sideLengths: list[int]):
        MOD = 1000

        # Count the frequency of each stick length
        count = Counter(sideLengths)

        # Store pairs that can form rectangles
        pairs = []

        # First, add pairs of sticks that can form rectangles without reduction
        for length in sorted(count.keys(), reverse=True):
            # Make as many pairs as possible with the original length
            while count[length] >= 2:
                count[length] -= 2
                pairs.append(length)

        # Next, try reducing sticks by 1 to form more pairs
        for length in sorted(count.keys(), reverse=True):
            if length > 1 and count[length] > 0 and count[length - 1] > 0:
                # Form a pair with one stick reduced by 1
                pairs.append(length - 1)
                count[length] -= 1
                count[length - 1] -= 1

        # Calculate the maximum area
        #print(pairs)
        area_sum = 0
        for i in range(0, len(pairs) - 1, 2):
            area_sum += pairs[i] * pairs[i + 1]
            area_sum %= MOD

        return area_sum


sol = Solution()

# Example usage:
arr = [2, 2, 5, 5, 4, 4, 4, 4]  #Expected: 28
#arr = [6, 6, 5, 7, 7, 7, 1]   #Expected: 42
arr = [3, 4, 5, 5, 6]  # Expected = 20 ; ChatGPT version fails, outputs 15.
arr = [2, 3, 3, 4, 6, 8, 8, 6] # Expected 54

print(sol.findArea_Me(arr))
print(sol.findArea_ChatGPT(arr))

