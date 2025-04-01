class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            if val <= self.minStack[len(self.minStack)-1]:
                self.minStack.append(val)
        return None

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        else:
            top = self.stack.pop()
            if top == self.minStack[-1]:
                self.minStack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
    
# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
# Output: [null,null,null,null,0,null,2,1]

minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()