'''
https://www.hackerrank.com/challenges/journey-to-the-moon/problem?isFullScreen=true

The member states of the UN are planning to send people to the moon.
They want them to be from different countries.
You will be given a list of pairs of astronaut ID's.
Each pair is made of astronauts from the same country.
Determine how many pairs of astronauts from different countries they can choose from.

Example
n = 4
astronaut = [1,2], [2,3]

There are 4 astronauts numbered 0 through 3.
 Astronauts grouped by country are [0] and [1,2,3].
 There are 3 pairs to choose from:
  [0,1], [0,2] and [0,3] .
  Answer is 3
'''

from collections import defaultdict


def find(x: int, parent: list[int]):
    path = []
    while parent[x] >= 0:
        path.append(x)
        x = parent[x]

    for i in path:
        parent[i] = x
    return x


def union(a: int, b: int, array: list[int]):
    repA = find(a, array)
    repB = find(b, array)
    if repA == repB: return
    sizeA = abs(array[repA])
    sizeB = abs(array[repB])

    if sizeA >= sizeB:
        array[repA] += array[repB]
        array[repB] = repA
    else:
        array[repB] += array[repA]
        array[repA] = repB


def approach_1(n: int, array: list[int]):
    nPairs = 0
    for i in range(n - 1):
        if array[i] >= 0: continue
        for j in range(i + 1, n):
            if array[j] >= 0: continue
            nPairs += abs(array[i]) * abs(array[j])
    return nPairs


def approach_2(n: int, array: list[int]):
    nPairs = 0
    H = defaultdict(int)
    for i in range(n):
        if array[i] < 0:
            H[abs(array[i])] += 1

    helper = list(H.keys())
    m = len(helper)
    for i in range(m):
        for j in range(i, m):
            if i == j:
                nPairs += pow(helper[i], 2) * (H[helper[i]] * (H[helper[i]] - 1)) // 2
            else:
                nPairs += helper[i] * H[helper[i]] * helper[j] * H[helper[j]]
    return nPairs

#n = total number of astronauts
#k = number of different group sizes
#m =  the size of astronaut array
#Time complexity: O(m + n + k^2)    
#Space complexity: O(n)
def journeyToMoon(n: int, astronaut: list[list[int]]):
    array = [-1 for _ in range(n)]
    #union-find data structure
    for a, b in astronaut:
        union(a, b, array)
    return approach_2(n, array)


n = 4
astronaut = [[1, 2], [2, 3]]  #Expected: 3

#n = 5
#astronaut = [[0, 1], [2, 3], [0, 4]]  #Expected: 6
#
# n = 10
# astronaut = [[0, 2], [1, 8], [1, 4], [2, 8], [2, 6], [3, 5], [6, 9]]  #Expected: 23

# n = 100000
# astronaut = [[1, 2], [3, 4]] #Expected: 4999949998

print(journeyToMoon(n, astronaut))


