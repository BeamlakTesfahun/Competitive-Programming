class MyCircularDeque:

    def __init__(self, k: int):
        self.d = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.d) < self.k:
            self.d = [value] + self.d
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.d) < self.k:
            self.d.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.d) > 0:
            self.d.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if len(self.d) > 0:
            self.d.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if len(self.d) > 0:
            return self.d[0]
        else:
            return -1
    def getRear(self) -> int:
        if len(self.d) > 0:
            return self.d[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if len(self.d) == 0:
            return True
        else:
            return False
    def isFull(self) -> bool:
        if len(self.d) == self.k:
            return True
        else:
            return False
        
