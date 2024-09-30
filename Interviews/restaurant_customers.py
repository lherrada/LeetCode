'''
https://www.youtube.com/watch?v=n0jwLjMvS_0
https://cses.fi/problemset/task/1619/
You are given the arrival and leaving times of n customers in a restaurant.
What was the maximum number of customers in the restaurant at any time?
Input
The first input line has an integer n: the number of customers.
After this, there are n lines that describe the customers.
 Each line has two integers a and b: the arrival and leaving times of a customer.
You may assume that all arrival and leaving times are distinct.
Output
Print one integer: the maximum number of customers.
Constraints

1 <= n <= 2*10^5
1 <= a < b <=10^9

Example
Input:
3
5 8
2 4
3 9

Output:
2
'''
import sys
from collections import defaultdict


class Solution:

    def myRange(self, hour: int, arrive: int, leave: int) -> bool:
        return True if arrive <= hour <= leave else False

    #Time Exceeded (Brute Force)
    def restaurantCustomer(self, n: int, customerTimes: list[list[int]]) -> int:
        minTime = float('inf')
        maxTime = -1 * float('inf')
        ans = float()
        for i in range(n):
            minTime = min(minTime, customerTimes[i][0])
            maxTime = max(maxTime, customerTimes[i][1])
        H = defaultdict(int)
        for i in range(minTime, maxTime + 1):  # O(q)
            for j in customerTimes:  #O(n)
                if self.myRange(i, j[0], j[1]):
                    H[i] += 1
        return max(H.values())

    #Not passing one test (out of 10) in cses web site
    def restaurantCustomer_v2(self, n: int, customerTimes: list[list[int]]) -> int:
        p = []
        for i in range(n):
            p.append([customerTimes[i][0], 1])
            p.append([customerTimes[i][1], -1])
        p.sort()
        ans = 0
        s = 0
        for i in p:
            s += i[1]
            ans = max(ans, s)
        return ans

    #Passed all test in cses.fi web site
    def restaurantCustomer_v3(self, n: int, customerTimes: list[list[int]]) -> int:
        H = defaultdict(int)
        for i in range(n):
            arrival = customerTimes[i][0]
            leave = customerTimes[i][1]
            H[arrival] += 1
            H[leave] -= 1

        ans = 0
        s = 0
        for i in sorted(H.keys()):
            s += H[i]
            ans = max(ans, s)
        return ans




sol = Solution()
# n = 3
# t = [[5, 8], [2, 4], [3, 9]]
# #
# n = 5
# t = [[1, 3], [2, 9], [4, 6], [5, 7], [9, 10]]

# print(sol.restaurantCustomer_v2(n, t))

if __name__ == '__main__':
    myInput = []
    for line in sys.stdin:
        line = line.rstrip()
        myInput.append(line)

    n = int(myInput[0])
    customerTimes = []
    for i in myInput[1:]:
        x = i.split(' ')
        x = [int(j) for j in x]
        customerTimes.append(x)

    print(sol.restaurantCustomer_v3(n, customerTimes))
