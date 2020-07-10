"""
Recursive implementation of backtrack algorithm
to resolve maze problem
S = Start
G = Goal
Complexity = O(n!)
maze = [
        ['.', '.', '.', 'X', 'G'],
        ['.', 'X', '.', 'X', '.'],
        ['.', 'X', '.', 'X', '.'],
        ['.', 'X', '.', 'X', '.'],
        ['S', 'X', '.', '.', '.']
       ]

Solution for this maze:
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1

"""

def valid(i, j, visit):
    if 0 <= i < len(visit) and 0 <= j < len(visit):
        if visit[i][j] is not 1 and maze[i][j] is not 'X':
            return True
    return False

def print_solution(solution, N):
    if not solution:
        print("There is no solution")
        return

    solution_array = [[0 for _ in range(N)] for _ in range(N)]
    for p in solution:
        solution_array[p[0]][p[1]] = 1

    for i in solution_array:
        for j in i:
            print(j, end=' ')
        print()

def findpath(i, j, maze, path, visit, flag=[]):
    if valid(i, j, visit):
        visit[i][j] = 1
        path.append((i, j))

	#Once the goal has been reached
	#turn on the flag so all recursive calls
	#do not pop the result saved in "path"
        if maze[i][j] is 'G':
            flag.append(1)
            return

	#Looking a path from any of the 4 directions:
	#up,down,right,left
        for pos in range(4):
            if flag:
                break
            ni = i + rows[pos]
            nj = j + columns[pos]
            findpath(ni, nj, maze, path, visit)

        #Backtracing
        if not flag:
          path.pop()

def solveMazeProblem(maze):
    visit = [[0 for _ in range(len(maze))] for _ in range(len(maze))]
    (i, j) = searchStartPoint(maze)
    path = []
    findpath(i, j, maze, path, visit)
    return path

def searchStartPoint(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] is 'S':
                return i, j
    return 0, 0

# Right,Left,Down,Up
rows = [0, 0, 1, -1]
columns = [1, -1, 0, 0]

maze = [
	['.', '.', '.', 'X', 'G'],
        ['.', 'X', '.', 'X', '.'],
        ['.', 'X', '.', 'X', '.'],
        ['.', 'X', '.', 'X', '.'],
        ['S', 'X', '.', '.', '.']
       ]

print_solution(solveMazeProblem(maze), len(maze))
