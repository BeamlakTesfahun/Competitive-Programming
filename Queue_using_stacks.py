class MyQueue:

    def __init__(self):
        self.stack1= []
        self.stack2= []

    def push(self, x: int) -> None:
        #Push element to the back of queue

        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
    def pop(self) -> int:
        #Removes the element from in front of queue and returns the element
        return self.stack1.pop()

    def peek(self) -> int:
        #Get the front element
        return self.stack1[-1]
    def empty(self) -> bool:
        #Retruns wheteher the queue is empty
        return not self.stack1
