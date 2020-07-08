"""
Given a maze, find a possible solution between two points
This is a non-recursive solution

matrix = [['.', 'X', '.', '.', 'G'],
          ['.', 'X', '.', 'X', '.'],
          ['.', '.', '.', 'X', '.'],
          ['.', 'X', '.', '.', 'X'],
          ['S', 'X', '.', '.', '.']
          ]

One possible solution:
0 0 1 1 1 
0 0 1 0 0 
1 1 1 0 0 
1 0 0 0 0 
1 0 0 0 0 
"""
import queue


def print_solution(solution, N):
    solution_array = [[0 for _ in range(N)] for _ in range(N)]
    for p in solution:
        solution_array[p[0]][p[1]] = 1

    for i in solution_array:
        for j in i:
            print(j, end=' ')
        print()


# Validate if point is a possible solution
# Do not retry points already visited
# because you will entered an infinite loop
def valid(i, j):
    if 0 <= i < len(matrix) and 0 <= j < len(matrix):
        if visited[i][j] is 0 and matrix[i][j] is not 'X':
            return True


# Find neighbors : up, down, left, right
# diagonal not implemented but easy to extend

def findNeighbors(current):
    count = 0
    i = current[0]
    j = current[1]
    visited[i][j] = 1
    for m in range(4):
        ni = i + rows[m]
        nj = j + columns[m]
        if valid(ni, nj):
            count += 1
            stack.put((ni, nj))
            break
    return count

#the real deal is here
def exploreMaze(startPoint):
    (i, j) = startpoint
    visited[i][j] = 1
    current = startPoint
    path = [current]

    # G stands for Goal
    while matrix[i][j] is not 'G':
        #Explore neighbors and try and 
	# validated candidate
        if findNeighbors(current) > 0:
            current = stack.get()
            path.append(current)
        else:
            # You entered a deadlock so backtrack
            path.pop()
            if path:
                current = path[-1]
        i = current[0]
        j = current[1]
    return path

#Search for start point, defaults to (0,0)
def searchStartPoint(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] is 'S':
                return (i, j)
    return (0, 0)


rows = [0, 0, 1, -1]
columns = [1, -1, 0, 0]
stack = queue.LifoQueue()
matrix = [['.', 'X', '.', '.', 'G'],
          ['.', 'X', '.', 'X', '.'],
          ['.', '.', '.', 'X', '.'],
          ['.', 'X', '.', '.', 'X'],
          ['S', 'X', '.', '.', '.']
          ]

startpoint = searchStartPoint(matrix)
visited = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
solution = exploreMaze(startpoint)
if solution:
    print_solution(solution, len(matrix))
else:
    print("There is no solution")
