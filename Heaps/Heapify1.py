#Learning Reference:
#https://www.youtube.com/watch?v=HqPJF2L5h9U

class Heapify:
    def __init__(self, mylist):
        self.heaplist = [0] + mylist
        self.currentsize = len(self.heaplist) - 1

    def maxChild(self, i):
        if 2 * i + 1 > self.currentsize:
            return 2 * i
        elif self.heaplist[2 * i] > self.heaplist[2 * i + 1]:
            return 2 * i
        else:
            return 2 * i + 1

    def swap(self, i, j):
        if i is not j:
            self.heaplist[i] = self.heaplist[i] ^ self.heaplist[j]
            self.heaplist[j] = self.heaplist[i] ^ self.heaplist[j]
            self.heaplist[i] = self.heaplist[i] ^ self.heaplist[j]
 
    #Using recursion to heapify subtrees
    def heapifySubTree(self, i):
        if 2 * i > self.currentsize:
            return
        maxindex = self.maxChild(i)
        if self.heaplist[i] > self.heaplist[maxindex]:
            return
        else:
            self.swap(i, maxindex)
            self.heapifySubTree(maxindex)

    def heapify(self):
        init = len(self.heaplist) // 2
        while init > 0:
            self.heapifySubTree(init)
            init -= 1

    def priorityQueue(self):
         x=self.heaplist.pop(1)
         self.currentsize = len(self.heaplist) - 1
         self.heapify()
         return x

    def __repr__(self):
        return str(self.heaplist[1:])

    def getCurrentSize(self):
        return self.currentsize


mylist = [11, 6, 8, 19, 4, 10, 5, 17, 43, 31, 49]
p = Heapify(mylist)

#Heapify array
p.heapify()
print(p)

#Printing element with highest priority
while p.getCurrentSize() > 0:
    print(p.priorityQueue())






