#coding=utf-8

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # small element float up
    # 'i' means the head's total size
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i // 2

    # insert element to Heap
    # 'k' means the element
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    # big element sink down
    # i means the element serial number
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    # find the min child serial number in heap
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    # delete min child
    def delMin(self):
        retval = self.heapList[1]   # heap serial number begins with "1"
        self.heapList[1] = self.heapList[self.currentSize]  # swap with the last child in the heap
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval   # retval means the min child element

    # build a heap based on list
    def buildHeap(self, alist):
        i = len(alist) // 2 # i means the total set of heap's child
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)    # build heap in O(n)
            i = i - 1

if __name__ == "__main__":
    binaryHeap = BinHeap()
    binaryHeap.buildHeap([1, 2, 3, 4, 4, 5, 2, 3, 4, 1, 2, 5, 6, 34, 6, 23523, 3])

    # time complexity is O(n)
    for i in range(5):
        print str(i+1) + '. ' + str(binaryHeap.delMin())
