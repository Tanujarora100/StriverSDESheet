'''
Time Complexity:
O(1) for push operation, as it only takes constant time to push an element into the stack.
O(1) for pop operation, as it only takes constant time to pop out an element out of the stack.
Space Complexity:
O(N), where N is the size of the array used for two stack's implementation.
'''
# One Stack-Left to Right
# Two Stack-Right to Left


class stack:
    def __init__(self, size) -> None:
        self.size = size
        self.arr = [0]*self.size
        self.top1 = -1
        # At the Beginning of the Array
        self.top2 = self.size
        # At the end

    def push1(self, value):
        # Check for Overflow of stack
        if self.top1+1 == self.top2:
            return -1
        self.top1 += 1
        # Increment the index
        self.arr[self.top1] = value

    def push2(self, value):
        # Check for Overflow of stack
        if self.top2-1 == self.top1:
            return -1
        self.top2 -= 1
        self.arr[self.top2] = value

    def pop1(self) -> int:
        if self.top1 == -1:
            return -1
        # No element in the stack to pop
        temp = self.arr[self.top1]
        self.top1 -= 1
        return temp

    def pop2(self) -> int:
        # If the stack is empty
        if self.top2 == self.size:
            return -1
        temp = self.arr[self.top2]
        self.top2 += 1
        return temp

    def print(self):
        for i in range(len(self.arr)):
            print(self.arr[i], end="  ")


ob = stack(10)
ob.push1(100)
ob.push2(200)
ob.push1(200)
ob.push1(10000)
ob.push2(56)
ob.print()