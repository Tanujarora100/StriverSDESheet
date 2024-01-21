from collections import deque
class MyStack:

    def __init__(self):
        self._stack=deque()
        self._size_stack=0

    def push(self, x: int) -> None:
        self._stack.append(x)
        self._size_stack+=1

    def pop(self) -> int:
        if self._size_stack<=0:
            return -1
        else:
            popped_ele=self._stack.pop()
            self._size_stack-=1
            return popped_ele

    def top(self) -> int:
        return self._stack[-1]  
        

    def empty(self) -> bool:
        if self._size_stack<=0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()