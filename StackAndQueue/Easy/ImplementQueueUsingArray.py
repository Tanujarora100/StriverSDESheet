class queue:
    def __init__(self):
        self._stack = []
        self._sizeArray = 0

    def push(self, value):
        self._stack.insert(0, value)
        self._sizeArray += 1

    def pop(self):
        if self._sizeArray <= 0:
            raise Exception('Stack underflow')
        else:
            self._sizeArray -= 1
            return self._stack.pop(0)

    def isEmpty(self):
        return self._sizeArray == 0

    def top(self):
        if not self.isEmpty:
            return self._stack[0]
        else:
            raise Exception("Empty queue")

    def length(self):
        return self._sizeArray


obj = queue()
obj.push(5)
obj.push(6)
obj.push(7)
obj.push(8)
obj.push(9)
print(obj.length())
obj.pop()
print(obj.length())