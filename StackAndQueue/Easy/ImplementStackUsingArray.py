class Stack:
    def __init__(self, size):
        self._stack = []
        self._size = size

    def is_empty(self):
        return len(self._stack) <= 0

    def push(self, data):
        if len(self._stack) >= self._size:
            raise Exception('Stack overflow')
        else:
            self._stack.append(data)

    def pop(self):
        if len(self._stack) <= 0:
            raise Exception('Stack underflow')
        else:
            return self._stack.pop()

    def peek(self):
        if len(self._stack) <= 0:
            raise Exception('Stack underflow')
        else:
            return self._stack[-1]

    def length(self):
        return len(self._stack)

    def print(self):
        return print(self._stack)


stack = Stack(5)
stack.push(5)
stack.push(2)
stack.push(3)
stack.push(9)
stack.push(6)
print(stack.peek(), end=" ")
print(stack.pop(), end=" ")
print(stack.length(), end=" ")
print(stack.peek(), end=" ")
print()
print(stack.print())
'''
Space complexity (for n push)->O(n)
Time complexity of push()->O(1)
Time complexity of pop()->O(1)
Time complexity of length()->O(1)
Time complexity of is_empty()->O(1)
'''