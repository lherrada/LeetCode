import time


# Implementation of LinkedList data structure
# with forward and backward links

class Node:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.visit = False


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
            current.next.prev = current

    def print_forward(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current:
                print(current.data, end=' ')
                current = current.next
        print()


    def countnodes(self):
        if self.head is None:
            return 0
        else:
            count = 1
            current = self.head
            while current.next:
                count += 1
                current = current.next
            return count

    def print_backward(self):
        countnodes = self.countnodes()
        if self.head is None:
            return
        else:
            index = 0
            current = self.head
            # Reaching end node
            while current:
                if index == countnodes - 1:
                    break
                index += 1
                current = current.next

            while current:
                print(current.data, end=' ')
                current = current.prev
            print()

    def print_backward_v2(self):
        if self.head is None:
            return
        else:
            index = 0
            current = self.head
            # Reaching end node
            while current.next:
                current = current.next

            while current:
                print(current.data, end=' ')
                current = current.prev
            print()



p1 = LinkedList(6)
p1.append(3)
p1.append(4)
p1.append(12)
p1.print_forward()
p1.print_backward()
