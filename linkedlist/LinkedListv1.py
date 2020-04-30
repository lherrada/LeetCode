import time


# Implementation of LinkedList data structure
# I added methods to create loops

class Node:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None
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

    def prepend(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
            self.head = node

    def print_forward(self, loop=False):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
            if loop:
                time.sleep(1)
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

    def remove(self, value):
        current = self.head
        if current.data == value:
            self.head = current.next
        else:
            while current.next:
                if current.next.data is value:
                    current.next = current.next.next
                    break
                current = current.next

    def insert(self, index, value):
        count = 0
        if index < 0:
            return
        elif index == 0:
            self.prepend(value)
        else:
            current = self.head
            while current:
                if count == index - 1:
                    node = Node(value)
                    node.next = current.next
                    current.next = node
                    break
                count += 1
                current = current.next

    # Loop last node with first node
    def create_loop1(self):
        current = self.head
        while current.next:
            current = current.next
        current.next = self.head

    # Loop node in position index with previous one.
    def create_loop2(self, index):
        if index < 0 or index == 0:
            return
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                current.next.next = current
                return
            current = current.next
            count += 1

    def loopdetection(self):
        current = self.head
        while current.next:
            if not current.visit:
                current.visit = True
            elif current.visit:
                return True
            current = current.next
        return False

    def loopdetection_v2(self):
        H = {}
        current = self.head
        while current:
            if current not in H:
                H.setdefault(current, "FB")
            else:
                return True
            current = current.next
        return False

    def insert_by_value_after(self, value, value_insert):
        current = self.head
        if current is None:
            return
        while current:
            if current.data == value:
                node = Node(value_insert)
                node.next = current.next
                current.next = node
                break
            current = current.next

    #Algorithm Floyd for loop detection. 
    #Traverse the linked list with pointes at 2 different speeds.
    #If there is a loop, the 2 pointers will meet eventually.
    def loopdetection_v3(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# 6 -> 3 -> 4 -> 2

p1 = LinkedList(6)
p1.append(3)
p1.append(4)
p1.append(2)
p1.append(7)
p1.append(12)


p1.print_forward()
p1.create_loop1()

#p1.create_loop2(3)
# p1.print(True)

if p1.loopdetection_v3():
    print("Loop detected")
else:
    print("No Loop detected")
