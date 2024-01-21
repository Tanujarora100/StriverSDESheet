class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for i in s:
            if stack:
                if stack[-1]==i:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return "".join(stack)