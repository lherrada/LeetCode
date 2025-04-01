"""
At Audible, a subscriber can gift an audiobook from his/her
library to any other non-subscriber to kick start their audiobook journey.

The first time subscriber can receive up to a maximum of N audiobooks from
their friends/relatives.
When a non-subscriber receives an audiobook, we can infer that the two
may be related. Similarly, if the non-subscriber receives gifted books from two
other subscribers, we can infer that all of them are related and the three of
them form a group. More formally, a group is composed of all of the people who know
one another, whether directly or transitively. Audible would like your help
finding out the number of such distinct groups from the input data.

Example
Consider the following input matrix M:

 1 1 0
 1 1 0
 0 0 1

Every row corresponds to a subscriber and the value M[i][j]
determines if j was gifted a book by i. In the above example,
user 0 has gifted a book to user 1 and so they are connected
[0][1], while person 2 has not received a book from anyone
or gifted book to anyone. Therefore, there are 2 groups.

M[i][j] = 1 if i == j (Each of the people is known to self)


"""

#Implementation of Union-Find data structure aka Disjoint sets
class UnionFindDS:
    def __init__(self, array: list[int]):
        self.array = array

    def find(self, a: int):
        while self.array[a] >= 0:
            a = self.array[a]
        return a

    def union(self, a: int, b: int):
        if a == b:
            return
        repA = self.find(a)
        repB = self.find(b)

        sizeA = abs(self.array[repA])
        sizeB = abs(self.array[repB])

        if sizeA >= sizeB:
            self.array[repA] += self.array[repB]
            self.array[repB] = repA
        else:
            self.array[repB] += self.array[repA]
            self.array[repA] = repB




from collections import deque
class Solution:
    #Using Union-Find data structure to count
    # number of groups .
    #Time Complexity : O(n^2)
    #Space Complexity : O(n) -> members array

    def giftingGroup_v1(self, array: list[list[int]]) -> int:
        n = len(array)
        members = [-1] * n
        uf = UnionFindDS(members)

        for i in range(n):
            for j in range(i, n):
                if i == j:
                    continue
                elif array[i][j] == 1:
                    uf.union(i, j)
        set1 = set()
        for i in range(n):  # O(n)
            set1.add(uf.find(i))
        return len(set1)

    #Traversing the bidimensional array
    # using Breadth First Search
    #Time Complexity : O(n^2)
    #Space Complexity : O(n) -> visited array

    def bfs(self, node, visited, array):
        q = deque()
        q.append(node)
        n = len(array)
        while q:
            current = q.popleft()
            for i in range(n):
                if i not in visited and array[current][i] == 1:
                    visited.add(i)
                    q.append(i)

    def giftingGroup_v2(self, array: list[list[int]]) -> int:
        n = len(array)
        visited = set()
        number_of_groups = 0
        for node in range(n):  # n times
            if node not in visited:
                number_of_groups += 1
                visited.add(node)
                self.bfs(node, visited, array)

        return number_of_groups

    #Traversing the bidimensional array
    # using Depth First Search
    #Time Complexity : O(n^2)
    #Space Complexity : O(n) -> visited array

    def dfs(self, node, visited: set, array: list[list[int]]):
        stack = []
        n = len(array)
        stack.append(node)

        while stack:
            current = stack.pop()
            #The array is symmetrical.
            #just need to traverse half the array
            # excluding the diagonal
            for i in range(node + 1, n):
                if i not in visited and array[current][i] == 1:
                    visited.add(i)
                    stack.append(i)

    def giftingGroup_v3(self, array: list[list[int]]) -> int:
        n = len(array)
        visited = set()
        number_of_groups = 0
        for node in range(n):
            if node not in visited:
                number_of_groups += 1
                visited.add(node)
                self.dfs(node, visited, array)
        return number_of_groups


sol = Solution()
input2 = [[1, 1, 0],
          [1, 1, 0],
          [0, 0, 1]]

input1 = [[1, 0, 0, 1],
          [0, 1, 1, 0],
          [0, 1, 1, 1],
          [1, 0, 1, 1]]

print(sol.giftingGroup_v1(input1))
print(sol.giftingGroup_v2(input1))
print(sol.giftingGroup_v3(input1))
