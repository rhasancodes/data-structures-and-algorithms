class MinBinaryHeap:
    def __init__(self):
        self.heapList = []
        
    def percUp(self):
        """
        percUp last element to it's right place
        """
        childIndex = len(self.heapList)-1  # last index
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            if self.heapList[childIndex] < self.heapList[parentIndex]:
                temp = self.heapList[childIndex]
                self.heapList[childIndex] = self.heapList[parentIndex]
                self.heapList[parentIndex] = temp
            childIndex = parentIndex
            
    def insert(self, data):
        self.heapList.append(data)
        self.percUp()
    
    def minChild(self, parentIndex):
        """
        min child of a parent node which must have child
        """
        lastIndex = len(self.heapList) - 1
        leftChildIndex = parentIndex * 2 + 1
        rightChildIndex = leftChildIndex + 1
        
        if lastIndex == leftChildIndex:
            return leftChildIndex
        
        if self.heapList[leftChildIndex] < self.heapList[rightChildIndex]:
            return leftChildIndex
        
        return rightChildIndex
    
    def percDown(self, parentIndex = 0):
        """
        percDown a root or any parent element to it's right place
        """
        lastIndex = len(self.heapList)-1
        leftChildIndex = parentIndex * 2 + 1
        while leftChildIndex <= lastIndex:
            minChildIndex = self.minChild(parentIndex)
            if self.heapList[parentIndex] > self.heapList[minChildIndex]:
                temp = self.heapList[parentIndex]
                self.heapList[parentIndex] = self.heapList[minChildIndex]
                self.heapList[minChildIndex] = temp
                
            parentIndex = minChildIndex
            leftChildIndex = parentIndex * 2 + 1
      
    def delMin(self):
        """
        delete minimum element of heap
        """
        data = self.heapList[0]
        lastIndex = len(self.heapList)-1
        self.heapList[0]=self.heapList[lastIndex]
        self.heapList.pop()
        self.percDown()
        return data
        
    def buildHeap(self, alist):
        """
        converting a list into min binary heap
        """
        self.heapList = alist
        lastIndex = len(self.heapList)-1
        parentIndex = (lastIndex-1)//2
        
        while(parentIndex>=0):
            self.percDown(parentIndex)
            parentIndex -= 1