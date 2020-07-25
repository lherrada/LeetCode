from queue import LifoQueue
"""
Implementation of BFS (Breadth First Search)
Optimal Solution for the given Maze:

Solution:

# # # # # # # # #
# 1 1 1 1       #
#   # # 1 # #   #
#   #   1 1 #   #
#   #   # 1 #   #
#   #   # 1 #   #
#   #   # 1 # # #
#         1 1 1 #
# # # # # # # # #
"""

def createMaze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "#", "#"])
    return maze


def createMaze2():
    maze = []
    maze.append([".", ".", "."])
    maze.append([".", "#", "."])
    maze.append([".", "#", "."])
    maze.append([".", "#", "."])
    return maze


class DFS:
    def __init__(self, maze):
        self.maze = maze
        self.q = LifoQueue()
        self.parent = {}
        self.visited = {}

    def findNeighbors(self, current):
        i = current[0]
        j = current[1]
        rows = [-1, 1, 0, 0]
        columns = [0, 0, -1, 1]

        for k in range(4):
            ni = i + rows[k]
            nj = j + columns[k]
            if ni < 0 or ni >= len(self.maze): continue
            if nj < 0 or nj >= len(self.maze[ni]): continue
            if (ni, nj) in self.visited: continue
            if self.maze[ni][nj] is "#": continue
            self.visited[(ni, nj)] = 1
            self.parent[(ni, nj)] = current
            self.q.put((ni, nj))

    def DFS(self, current, target):
        self.visited[current] = 1
        self.parent[current] = None
        self.q.put(current)

        while current is not target and not self.q.empty():
            current = self.q.get()
            self.findNeighbors(current)
        return self

    def print_solution(self, target):
        yellow = '\033[93m'
        endcolor = '\33[0m'
        if target not in self.parent:
            print("There is no solution")
            return

        while target:
            row = target[0]
            column = target[1]
            self.maze[row][column] = yellow + str(1) + endcolor
            target = self.parent[target]

        for i in self.maze:
          for j in i:
            print(j, end=' ')
          print()


x = DFS(createMaze())
start = (1, 1)
target = (7, 7)
x.DFS(start, target).print_solution(target)
