"""
https://leetcode.com/problems/range-sum-query-2d-immutable/
Given a 2D matrix matrix, find the sum of the elements inside
 the rectangle defined by its upper left corner (row1, col1)
 and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by
(row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""
from typing import List

sum2d_array = []

A = []
A.append([3, 0, 1, 4, 2])
A.append([5, 6, 3, 2, 1])
A.append([1, 2, 0, 1, 5])
A.append([4, 1, 0, 1, 7])
A.append([1, 0, 3, 0, 5])


def PartialSum2d(A: List[List[int]]):
    for rowArray in A:
        sumArray = [0]
        for i in range(len(rowArray)):
            sumArray.append(rowArray[i] + sumArray[i])
        sum2d_array.append(sumArray)


def sum_region(k, l, m, n):
    mysum = 0
    for i in range(k, m + 1):
        mysum += sum2d_array[i][n + 1] - sum2d_array[i][l]
    return mysum


PartialSum2d(A)
print(sum_region(2, 1, 4, 3))
print(sum_region(1, 1, 2, 2))
print(sum_region(1, 2, 2, 4))
