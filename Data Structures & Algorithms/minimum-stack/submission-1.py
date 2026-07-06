class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
    def pop(self) -> None:
        stack = self.stack
        stack.pop(-1)
        
    def top(self) -> int:
        stack = self.stack
        return stack[-1]
        
    def getMin(self) -> int:
        stack = self.stack
        return min(stack)
