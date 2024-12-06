# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

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
