'''
https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

For the purposes of this challenge, we define a binary search tree to be a binary
tree with the following properties:

The data value of every node in a node's left subtree is less than the data value of that node.
The data value of every node in a node's right subtree is greater than the data value of that node.
The data value of every node is distinct.

For example, the image on the left below is a valid BST. The one on the right fails on several counts:
- All of the numbers on the right branch from the root are not larger than the root.
- All of the numbers on the right branch from node 5 are not larger than 5.
- All of the numbers on the left branch from node 5 are not smaller than 5.
- The data value 1 is repeated.

'''
class BSTNode:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

#Recursive approach
def buildTree(array: list[int]) -> BSTNode:
    n = len(array)

    def process(array: list[int], i: int, n: int) -> BSTNode:
        root = None
        if i < n and array[i] is not None:
            root = BSTNode(array[i])
            root.left = process(array, 2 * i + 1, n)
            root.right = process(array, 2 * i + 2, n)
        return root

    return process(array, 0, n)

def checkBST(root: BSTNode):
    S = set()
    MIN_VAL = -1 * float('inf')
    MAX_VAL = float('inf')

    # [ minValue, maxValue]
    def process(root: BSTNode) -> list[float] | list[int]:
        if root is None:
            return [MAX_VAL, MIN_VAL]

        leftArray = process(root.left)
        rightArray = process(root.right)

        if root.data < leftArray[1] or root.data > rightArray[0] or root.data in S:
            return [-1, -1]
        S.add(root.data)
        return [min(leftArray[0], root.data), max(rightArray[1], root.data)]

    return False if process(root)[0] == -1 else True


input = [6, 4, 5, None, None, 4, None]
input = [6, 7, 9, 3, 9]
input = [2, 1, 3]
root = buildTree(input)
print(checkBST(root))
