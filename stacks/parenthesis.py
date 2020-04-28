"""
Given a balanced expression that can contain opening and closing parenthesis, check
if the expression contains any duplicate parenthesis or not.
For example,
 Input: ((x+y)) + z
 Output: The expression have duplicate parenthesis

Input: ((x+y) + ((z)))
 Output: The expression have duplicate parenthesis

Input: (x+y)
Output: The expression does not have duplicate parenthesis
Level: Easy
"""

from LeetCode.stacks.stack import Stack 

stack=Stack()

def parenthesis(input):
    for c in input:
        if c is not ')':
            stack.push(c)
        else:
            if stack.pop() is '(':
                return True
            else:
                while stack.pop() is not '(':
                    pass
    return False

input="(x+((y+z))+p)"

if parenthesis(input):
    print("The expression have duplicate parenthesis")
else:
    print("The expression does not have duplicate parenthesis")
