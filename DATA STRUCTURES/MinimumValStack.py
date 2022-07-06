class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, item):
        self.stack.append(item)
        value = min(item, self.minstack[-1] if self.minstack else item)
        self.minstack.append(value)
    def pop(self):
        self.stack.pop()
        self.minstack.pop()
    def getmin(self):
        return self.minstack[-1]
    def top(self):
        return self.stack[-1]
M = MinStack()
M.push(8)
M.push(4)
M.push(99)
M.push(3)
M.push(9)
print(M.getmin())
print(M.top())
