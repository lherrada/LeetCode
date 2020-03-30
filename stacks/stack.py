class Stack:
    def __init__(self):
        self.StackArray = []

    def push(self,value):
        self.StackArray.append(value)

    def pop(self):
        return self.StackArray.pop()

    def __repr__(self):
        return str(self.StackArray)

    def __len__(self):
        return len(self.StackArray)


if __name__ == '__main__':
    mystack=Stack()
    mystack.push(10)
    mystack.push(20)
    mystack.push(30)

    print(mystack.pop())
    print(mystack.pop())
    print(mystack.pop())
    print(mystack)
