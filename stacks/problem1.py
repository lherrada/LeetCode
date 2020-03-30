# Check for balanced parentheses in Python
#     Given an expression string, write a python program to find whether a given string has balanced parentheses or not.
#
# Examples:
#
# Input : {[]{()}}
# Output : Balanced
#
# Input : [{}{}(]
# Output : Unbalanced

from stack import Stack

H = {'{': '}', '[': ']', '(': ')'}


def checkifbalanced(myinput):
    stack = Stack()
    for i in myinput:
        if i in H.keys():
            stack.push(i)
        else:
            if len(stack) > 0 and H[stack.pop()] == i:
                continue
            else:
                return False

    return False if len(stack) > 0 else True

myinput = '([[[{}]]]('

if checkifbalanced(myinput):
    print("Balanced")
else:
    print("Unbalanced")
