'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of integers in the stack
'''


def deleteMid(self, s, sizeOfStack):
    if sizeOfStack == 0:
        return
    stack = []
    count = 0

    while count < sizeOfStack//2:
        stack.append(s[-1])
        s.pop()
        count = count+1

    s.pop()

    while stack:
        s.append(stack[-1])
        stack.pop()