'''
Level: Easy
https://cses.fi/problemset/task/1629
In a movie festival n movies will be shown. You know the starting and ending time of each movie. What is the maximum number of movies you can watch entirely?
Input
The first input line has an integer n: the number of movies.
After this, there are n lines that describe the movies. Each line has two integers a and b: the starting and ending times of a movie.
Output
Print one integer: the maximum number of movies.
Constraints

1 <= n <= 2*10^5
1 <= a < b <= 10^9

Example
Input:
3
3 5
4 9
5 8

Output:
2
'''

import sys

class Solution:
    def festival(self, n: int, movieTime: list[list[int]]):
        movieTime = sorted(movieTime, key=lambda k: k[1])
        movies_seen = 0
        upperLimit = 0
        for i in range(n):
            interval = movieTime[i]
            if interval[0] >= upperLimit:
                movies_seen += 1
                upperLimit = interval[1]
        return movies_seen


sol = Solution()

# t = [[4, 5], [1, 4], [7, 8], [1, 3]]
#t = [[3, 5], [4, 9], [5, 8]]
# print(sol.festival(len(t), t))

if __name__ == '__main__':
    input = []
    for line in sys.stdin:
        line = line.rstrip()
        input.append(line)

    n, = [int(i) for i in input[0].split(' ')]

    p = []
    for i in range(1, n + 1):
        movieTimes = input[i].split(' ')
        movieTimes = [int(i) for i in movieTimes]
        p.append(movieTimes)

    #print(n, p)
    print(sol.festival(n, p))
