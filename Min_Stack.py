class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack= []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # compare val and top value of minStack if minStack is not empty
        # if minStack is empty compare val and val
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
# only called when stack is non-empty
    def top(self) -> int:
        return self.stack[-1]
# only called when stack is non-empty
    def getMin(self) -> int:
        return self.minStack[-1]
        
