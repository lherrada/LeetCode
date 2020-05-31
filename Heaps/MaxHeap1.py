class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, number):
        self.heapList.append(number)
        index = len(self.heapList) - 1

        while index // 2 > 0:
            if self.heapList[index] > self.heapList[index // 2]:
                self.swap(index, index // 2)
            else:
                break
            index = index // 2

        self.currentSize = len(self.heapList) - 1

    def swap(self, i, j):
        if self.heapList[i] is not self.heapList[j]:
            self.heapList[i] = self.heapList[i] ^ self.heapList[j]
            self.heapList[j] = self.heapList[i] ^ self.heapList[j]
            self.heapList[i] = self.heapList[i] ^ self.heapList[j]

    def minChild(self, i):
        if 2 * i + 1 > self.currentSize:
            return 2 * i
        elif self.heapList[2 * i] > self.heapList[2 * i + 1]:
            return 2 * i
        else:
            return 2 * i + 1

    def remove(self):
        self.swap(1, self.currentSize)
        self.currentSize -= 1
        index = 1
        while 2 * index <= self.currentSize:
            indexMin = self.minChild(index)
            if self.heapList[index] > self.heapList[indexMin]:
                break
            else:
                self.swap(index, indexMin)
                index = indexMin

    def __repr__(self):
        return str(self.heapList[1:])


x = BinaryHeap()
a = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
#a = [9, 6, 5, 2, 3]
for i in a:
    x.insert(i)

print("Max Heap:", x)

for _ in range(len(a) - 1):
    x.remove();

print("Sorted array:", x)
