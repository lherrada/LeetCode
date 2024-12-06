'''
Level = Hard
https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Given an array of integers heights representing
the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:

    1 <= heights.length <= 10^5
    0 <= heights[i] <= 10^4

'''
# Brute Force solution :
# Time complexity: O(n^2)
def largestRectangle(h: list[int]) -> int:
    area = 0
    n = len(h)
    #Brute Force
    for i in range(n):
        hmin = float('inf')
        for j in range(i, n):
            base = j - i + 1
            hmin = min(hmin, h[j])
            area = max(area, hmin * base)
    return area


# Optimal Solution:
# Time complexity: O(n)
# Space complexity: O(n)
#Approach is to find the area that can be formed to the left of the bar
# and to the right of the bar. To do so, we need to figure out the index in both
# directions (left and right). Once calculated the index, calculating the area for
# the given bar is straightforward.

def largestRectangle_v2(h: list[int]) -> int:
    #Building left limit
    stack = []
    leftLimit = []
    n = len(h)
    rightLimit = [-1 for _ in range(n)]
    for current in range(n):
        while len(stack) > 0 and h[stack[-1]] >= h[current]:
            stack.pop()
        leftLimit_index = stack[-1] + 1 if len(stack) > 0 else 0
        leftLimit.append(leftLimit_index)
        stack.append(current)

    #Building right limit
    stack = []
    for current in range(n - 1,-1, -1):
        while len(stack) > 0 and h[stack[-1]] >= h[current]:
            stack.pop()
        rightLimit_index = stack[-1] - 1 if len(stack) > 0 else n - 1
        rightLimit[current] = rightLimit_index
        stack.append(current)

    #Calculating area
    area = 0
    for i in range(n):
        base = rightLimit[i] - leftLimit[i] + 1
        height = h[i]
        area = max(area, base*height)
    return area

a = 5
h = [4, 1, 2, 5, 1]
h = [3, 2, 3]
h = [1, 2, 3, 4, 5]
h = [5, 2, 6, 6, 7, 0, 2]

h = [2, 4, 6, 7, 1]
h = [1, 2, 3, 4, 5, 0]
h = [5, 2, 6, 6, 7, 0, 2]
h = [5, 4, 3, 2, 1]
h = [2, 4, 6, 7, 3, 3, 5]

h = [2,1,5,6,2,3]

print(largestRectangle_v2(h))
