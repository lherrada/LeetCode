# Question 1: In a map which is contoured with various heights of land, what's the minimum water height that
# disconnects a path between two corners of this map. You can only move orthogonally (in right angles)
#
# Example:
# Land of heights:
# S  5  4  5  5
# 4  2  5  1  1
# 5  5  2  1  5         [S & E are of infinite heights]
# 2  3  2  4  4
# 5  4  5  5  E
#
#
# Water level: 3  <== Answer
# S  5  4  5  5
# 4  X  5  X  X
# 5  5  X  X  5         [S & E are of infinite heights]
# X  X  X  4  4
# 5  4  5  5  E

from queue import LifoQueue
from typing import Dict
from multiprocessing import Pool


class DFSProblem:
    def __init__(self, mymaze, height):
        self.maze = list(map(list, mymaze))
        self.convertMaze(height)
        self.visited = {}
        self.parent = {}
        self.q = LifoQueue()
        self.rows = [-1, 1, 0, 0]
        self.columns = [0, 0, -1, 1]
        self.target = ()

    def print_solution(self):
        yellow = '\033[93m'
        endcolor = '\33[0m'
        target = self.target
        if target not in self.parent:
            print("There is no solution")
            return

        while target:
            row = target[0]
            column = target[1]
            self.maze[row][column] = yellow + str(0) + endcolor
            target = self.parent[target]

        for i in self.maze:
            for j in i:
                print(j, end=' ')
            print()

    def findSandE(self) -> Dict:
        p = {}
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] is 'S' or self.maze[i][j] is 'E':
                    p.setdefault(self.maze[i][j], (i, j))
                if len(p.keys()) is 2:
                    return p

    def find_neighbors(self, current):
        row = current[0]
        column = current[1]
        for k in range(4):
            new_row = row + self.rows[k]
            new_column = column + self.columns[k]
            tuple1 = (new_row, new_column)
            if new_row < 0 or new_row >= len(self.maze): continue
            if new_column < 0 or new_column >= len(self.maze[new_row]): continue
            if self.maze[new_row][new_column] is 'X': continue
            if tuple1 in self.visited: continue
            self.q.put(tuple1)
            self.visited[tuple1] = 1
            self.parent[tuple1] = current

    def DFS(self):
        sAndE = self.findSandE()
        start = sAndE['S']
        self.target = sAndE['E']
        self.parent[start] = None
        self.visited[start] = 1
        self.q.put(start)

        current = start
        while current is not self.target and not self.q.empty():
            current = self.q.get()
            self.find_neighbors(current)

        return self

        # return self.isThereSolution(end)

    def isThereSolution(self):
        if self.target in self.parent:
            return True
        else:
            return False

    def convertMaze(self, n):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if isinstance(self.maze[i][j], int) and self.maze[i][j] <= n:
                    self.maze[i][j] = 'X'
        # print(self.maze)


def results(n: int):
    return DFSProblem(maze2, n).DFS().isThereSolution()


maze = []
maze.append(['S', 5, 4, 5, 5])
maze.append([4, 2, 5, 4, 4])
maze.append([5, 5, 2, 1, 5])
maze.append([2, 3, 2, 4, 4])
maze.append([5, 4, 5, 3, 'E'])

maze2 = []
maze2.append([1, 9, 6, 4, 1, 2])
maze2.append([9, 6, 7, 9, 7, 'E'])
maze2.append([1, 3, 1, 8, 8, 2])
maze2.append(['S', 7, 4, 9, 9, 1])
maze2.append([1, 9, 2, 7, 7, 1])

# p = DFSProblem(maze, 2)
# p.DFS().print_solution()
# print("end")

numbers = set()
for i in maze2:
    for j in i:
        if isinstance(j, int):
            numbers.add(j)

numbers = sorted(list(numbers))
# print(DFSProblem(maze,3).DFS().isThereSolution())


with Pool(10) as mp:
    solution = mp.map(results, numbers)

# print(solution.index(False))
print(numbers[solution.index(False)])

# concurrence =2
# i=1
# while True:
#     x = range(i,i+2)

# print(DFSProblem(maze,2).DFS().isThereSolution())

