from queue import Queue

"""
Implementation of BFS (Breadth First Search)
Optimal Solution for the given Maze:

0 0 0 0 0 1 0 0 0 
0 0 0 0 1 1 0 0 0 
0 0 0 0 1 0 0 0 0 
0 0 0 1 1 0 0 0 0 
0 0 0 1 0 0 0 0 0 
0 0 0 1 0 0 0 0 0 
0 0 0 1 0 0 0 0 0 
0 1 1 1 0 0 0 0 0 
1 1 0 0 0 0 0 0 0 
"""
def createMaze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "S", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["G", " ", "#", "#", "#", "#", "#", "#", "#"])
    return maze

# Add neighbors of the current point.
# We consider 4 directions: up,down, left,right
# Also make sure neighbors are valid points
def addNeighbors(current, parent):
    cr = current[0]
    cc = current[1]
    for i in range(4):
        nrow = cr + rows[i]
        ncolumn = cc + columns[i]
        if nrow < 0 or nrow >= len(maze): continue
        if ncolumn < 0 or ncolumn >= len(maze): continue
        if maze[nrow][ncolumn] is '#': continue
        #
        if visited[nrow][ncolumn] is 1: continue
        parent[(nrow, ncolumn)] = current
        q.put((nrow, ncolumn))
        visited[nrow][ncolumn] = 1

#The real deal just below
#Value returned is a hash with the path
def solveMaze(current, end):
    parent = {}
    parent.setdefault(current, None)
    q.put(current)
    visited[current[0]][current[1]] = 1
    while current != end and not q.empty():
        current = q.get()
        addNeighbors(current, parent)
    return parent

#Print solution with  path in yellow
def print_solution(target, solDict):
    yellow = '\033[93m'
    endcolor = '\33[0m'
    solution = [[0 for _ in range(len(maze))] for _ in range(len(maze))]
    while target:
        row = target[0]
        column = target[1]
        solution[row][column] = yellow + str(1) + endcolor
        target = solDict[target]

    for i in solution:
        for j in i:
            print(j, end=' ')
        print()

# Find coordinates of points marked as 'S': Start
# and 'G': Goal
def find_start_end(maze):
    p = {}
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] is 'S' or maze[i][j] is 'G':
                p.setdefault(maze[i][j], (i, j))
                if len(p.keys()) is 2:
                    return p


columns = [0, 0, -1, 1]
rows = [-1, 1, 0, 0]
q = Queue()
maze = createMaze()
visited = [[0 for _ in range(len(maze))] for _ in range(len(maze))]

location = find_start_end(maze)
start = location['S']
end = location['G']

solution = solveMaze(start, end)
if end in solution:
    print_solution(end, solution)
else:
    print("There is no solution")
