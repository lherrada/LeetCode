'''
A LuisStore is a warehouse run by Luis's company that houses items found in convenience stores,
grocery stores, and restaurants. We have a city with open roads, blocked-off roads, and LuisStores.

City planners want you to identify how far a location is from its closest LuisStore
You can only travel over open roads (up, down, left, right)

#Locations are given in [row, col] format
' ' represents an open road that you can travel over in any direction (up, down, left, or right)
'X' represents a blocked  road that you cannot travel through
'D' represents a LuisStore

[                 0    1    2    3    4    5    6    7    8
             0  ['X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X'],
             1  ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
             2  [' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', 'D'],
             3  [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' '],
             4  [' ', ' ', ' ', ' ', 'X', 'X', 'X', ' ', 'X'],
             5  [' ', ' ', ' ', ' ', 'X', ' ', 'D', ' ', 'X']
]

list of pairs [row, col]
locations = [
    [50, 50],
    [1,4],
    [5,0],
    [5,8],
    [3,8],
    [5,5]

#Number of steps to reach a LuisStore
answer = [-1,7,15,-1,1,1]
'''

from queue import PriorityQueue
from collections import deque

class Solution:
    #Implementation of Dijkstra algorithm to solve this problem
    #Space complexity = O(m.n) + O(m.n) = O(m.n)
    #Time complexity: O(m.n.log(m.n))
    def dijkstra_algo(self, array2d: list[list[str]], start: list[int]) -> int:
        nrows = len(array2d)
        ncols = len(array2d[0])
        if start[0] >= nrows or start[1] >= ncols or array2d[start[0]][start[1]] == 'X':
            return -1
        costArray = [[float('inf') for _ in range(ncols)] for _ in range(nrows)]
        costArray[start[0]][start[1]] = 0
        visited = set()
        pq = PriorityQueue()
        pq.put((0, start))
        # up, down, left, right
        dirRows = [-1, 1, 0, 0]
        dirCols = [0, 0, -1, 1]

        while not pq.empty():
            cost, node = pq.get()  # O(1)
            if array2d[node[0]][node[1]] == 'D':
                return int(costArray[node[0]][node[1]])
            if tuple(node) in visited:
                continue
            visited.add(tuple(node))
            for i in range(4):
                neighbor_row = node[0] + dirRows[i]
                neighbor_col = node[1] + dirCols[i]
                if neighbor_row < 0 or neighbor_row >= nrows: continue
                if neighbor_col < 0 or neighbor_col >= ncols: continue
                if array2d[neighbor_row][neighbor_col] == 'X': continue
                neighbor_cost = cost + 1
                if neighbor_cost < costArray[neighbor_row][neighbor_col]:
                    costArray[neighbor_row][neighbor_col] = neighbor_cost
                    pq.put((neighbor_cost, [neighbor_row, neighbor_col]))  #O(log(m.n))
        return -1

    #Breadth First Search
    #Time complexity: O(m.n)
    #Space complexity: O(m.n)
    def BFS(self, array2d: list[list[str]], start: list[int]) -> int:
        nrows = len(array2d)
        ncols = len(array2d[0])
        if start[0] >= nrows or start[1] >= ncols or array2d[start[0]][start[1]] == 'X':
            return -1
        distance = [[0 for _ in range(ncols)] for _ in range(nrows)]
        visited = set()
        rowDir = [-1, 1, 0, 0]
        colDir = [0, 0, -1, 1]
        q = deque()
        q.append(start)
        while q:
            current_node = q.popleft()
            if array2d[current_node[0]][current_node[1]] == 'D':
                return distance[current_node[0]][current_node[1]]
            if tuple(current_node) in visited:
                continue
            visited.add(tuple(current_node))
            for i in range(4):
                neighbor_row = current_node[0] + rowDir[i]
                neighbor_col = current_node[1] + colDir[i]
                if neighbor_row < 0 or neighbor_row >= nrows: continue
                if neighbor_col < 0 or neighbor_col >= ncols: continue
                if array2d[neighbor_row][neighbor_col] == 'X': continue
                if (neighbor_row, neighbor_col) in visited: continue
                distance[neighbor_row][neighbor_col] = distance[current_node[0]][current_node[1]] + 1
                q.append([neighbor_row, neighbor_col])
        return -1

    #Depth First Search (recursive)
    #Time complexity: O(m.n)
    #Space complexity: O(m.n)
    def DFS(self, array2d: list[list[str]], start: list[int]) -> int:
        nrows = len(array2d)
        ncols = len(array2d[0])
        if (start[0] >= nrows or start[1] >= ncols or
                array2d[start[0]][start[1]] == 'X'):
            return -1
        distance = [[float('inf')] * ncols for _ in range(nrows)]
        distance[start[0]][start[1]] = 0

        def store_locations(array2d: list[list[str]]) -> list[list[int]]:
            location = []
            for i in range(nrows):
                for j in range(ncols):
                    if array2d[i][j] == 'D':
                        location.append([i, j])
            return location

        def dfs(start):
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dir in directions: # O(n.m)
                neighbor_row = start[0] + dir[0]
                neighbor_col = start[1] + dir[1]
                if neighbor_row < 0 or neighbor_row >= nrows: continue
                if neighbor_col < 0 or neighbor_col >= ncols: continue
                if array2d[neighbor_row][neighbor_col] == 'X': continue
                distance_neighbor = distance[start[0]][start[1]] + 1
                if distance_neighbor < distance[neighbor_row][neighbor_col]:
                    distance[neighbor_row][neighbor_col] = distance_neighbor
                    dfs([neighbor_row, neighbor_col])


        dfs(start)
        stores = store_locations(array2d) # O(n.m)
        min_distance = min([distance[i[0]][i[1]] for i in stores])
        return min_distance if min_distance != float('inf') else -1


#input = 2d array, start point
#Extra space: 2d

# array2d = [
#     ['.', 'X', 'D'],
#     ['.', '.', '.'],
#     ['.', 'X', 'D'],
# ]

# array2d = [
#     ['.', '.', '.', '.'],
#     ['.', 'X', '.', '.'],
#     ['.', '.', '.', 'X'],
#     ['.', 'X', '.', 'D']
# ]

array2d = [
    ['X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
    [' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', 'D'],
    [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', 'X', 'X', 'X', ' ', 'X'],
    [' ', ' ', ' ', ' ', 'X', ' ', 'D', ' ', 'X']
]

start = [200, 200]
start = [5, 5]
sol = Solution()
print(sol.dijkstra_algo(array2d, start))
print(sol.BFS(array2d, start))
print(sol.DFS(array2d, start))

