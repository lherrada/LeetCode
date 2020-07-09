# Python3 program to solve Rat in a Maze
# problem using backtracking
""" First version authored by Shiv Shankar.
    I extended to the 4 directions: up,down,left,right
    This function solves the Maze problem using Backtracking.
    It mainly uses solveMazeUtil() to solve the problem. It
    returns false if no path is possible, otherwise return
    true and prints the path in the form of 1s. Please note
    that there may be more than one solutions, this function
    prints one of the feasable solutions.
"""

# A utility function to print solution matrix sol
def printSolution(sol):
    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")

    # A utility function to check if x, y is valid


# Check if point is valid.
# Valid point is a point that is within the maze
# and have not been visited.
def isSafe(maze, x, y, visited):
    N = len(maze)
    if 0 <= x < N and 0 <= y < N and maze[x][y] is not 'X':
        if visited[x][y] is not 1:
            visited[x][y] = 1
            return True
    return False


# Search for start point, defaults to (0,0)
def searchStartPoint(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] is 'S':
                return i, j
    return 0, 0


def solveMaze(maze):
    N = len(maze)
    sol = [[0 for j in range(N)] for i in range(N)]
    visited = [[0 for j in range(N)] for i in range(N)]
    (i, j) = searchStartPoint(maze)
    if not solveMazeUtil(maze, i, j, sol, visited):
        print("Solution doesn't exist");
        return False

    printSolution(sol)
    return True


# The real deal is here
# A recursive utility function to solve Maze problem
def solveMazeUtil(maze, x, y, sol, visited):
    # if (x, y is goal) return True

    # Check if maze[x][y] is valid
    if isSafe(maze, x, y, visited):
        if maze[x][y] is 'G':
            sol[x][y] = 1
            return True
        # mark x, y as part of solution path
        sol[x][y] = 1

        # Move forward in x direction
        if solveMazeUtil(maze, x + 1, y, sol, visited) is True:
            return True

        # If moving in x direction doesn't give solution
        # then Move down in y direction
        if solveMazeUtil(maze, x, y + 1, sol, visited) is True:
            return True

        if solveMazeUtil(maze, x - 1, y, sol, visited) is True:
            return True

        if solveMazeUtil(maze, x, y - 1, sol, visited) is True:
            return True

        # If none of the above movements work then
        # BACKTRACK: unmark x, y as part of solution path
        sol[x][y] = 0
        return False


# Driver program to test above function
if __name__ == "__main__":

    # Initialising the maze
    maze = [['S', '.', 'X', 'G'],
            ['X', '.', '.', '.'],
            ['.', '.', 'X', '.'],
            ['.', '.', 'X', '.']]

    solveMaze(maze)

