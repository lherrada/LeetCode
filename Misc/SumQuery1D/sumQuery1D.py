"""
https://leetcode.com/problems/range-sum-query-immutable/
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Constraints:

You may assume that the array does not change.
There are many calls to sumRange function.
0 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
0 <= i <= j < nums.length
"""

from typing import List

# F(i,j) = Sum(j) - Sum(i-1)
sum_array = []


def PartialSum(A: List[int]) -> List[int]:
    sum_array.append(0)
    for i in range(len(A)):
        sum_array.append(A[i] + sum_array[i])
    return sum_array


def Query_1d(i, j):
    return sum_array[j + 1] - sum_array[i]


A = [1, 2, 4, 5]  # -> Sum=[0,1,3,7,12]

print(PartialSum(A))
print(Query_1d(0, 2))
