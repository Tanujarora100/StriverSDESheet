class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if stack:
                if i == '*':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                # If Stack is empty and a star comes then just continue
                if i == '*':
                    continue
                else:
                    # If any Other character then just append it to the stack
                    stack.append(i)
        return "".join(stack)