class FreqStack:

    def __init__(self):
        self.stack = []
        self.count = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.count[val] += 1

    def pop(self) -> int:
        maxCount = max(self.count.values())
        top = len(self.stack) - 1

        while self.count[self.stack[top]] != maxCount:
            top -= 1
        self.count[self.stack[top]] -= 1
        return self.stack.pop(top)



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()