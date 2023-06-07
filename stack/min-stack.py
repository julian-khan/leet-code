# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        currMin = self.getMin()

        if (not currMin and currMin != 0) or currMin > val:
            currMin = val
        self.stack.append((val, currMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None