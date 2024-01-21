class MinStack:

    def __init__(self):
        self.stack = []
        self.minSt = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minSt:
            # If Not empty
            self.minSt.append(min(self.minSt[-1], val))
        else:
            self.minSt.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minSt.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minSt[-1]