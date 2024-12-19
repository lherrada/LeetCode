'''
https://www.hackerrank.com/challenges/absolute-permutation/problem
We define to be a permutation of the first natural numbers in the range .
Let denote the value at position in permutation using 1-based indexing.

P is considered to be an absolute permutation if  | pos[i] - i| = k
holds true for every i E [1,n].

Given n and k,print the lexicographically smallest absolute permutation P.
If no absolute permutation exists, print -1.

Example

Create an array of elements from to , . Using based indexing, create a permutation where every . It can be rearranged to so that all of the absolute differences equal :

'''
import os

def condition(i: int, k: int, n: int, a: set) -> bool:
    return 0 < i + k <= n and (i + k) not in a


def absolutePermutation(n: int, k: int) -> int | list[int]:
    ans = [-1 for _ in range(n + 1)]
    a = set()
    for i in range(1, n + 1):
        if condition(i, -k, n, a) is True:
            ans[i] = i - k
            a.add(i - k)
        elif condition(i, k, n, a) is True:
            ans[i] = i + k
            a.add(i + k)
        else:
            return [-1]
    return ans[1:]


# if __name__ == '__main__':
#     os.environ['OUTPUT_PATH'] = 'absolutePermutation'
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     t = int(input().strip())
#
#     for t_itr in range(t):
#         first_multiple_input = input().rstrip().split()
#
#         n = int(first_multiple_input[0])
#
#         k = int(first_multiple_input[1])
#
#         result = absolutePermutation(n, k)
#
#         fptr.write(' '.join(map(str, result)))
#         fptr.write('\n')
#
#     fptr.close()



n = 10
k = 1
#  2 1 4 3 6 5 8 7 10 9 # Expected
# [2 1 2 3 4 5 6 7  8 9] #Actual


print(absolutePermutation(n, k))
