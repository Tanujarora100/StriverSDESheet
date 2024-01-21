class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        k = 0

        for c in s:
            if c.isdigit():
                k = (k * 10) + (int(c))
                continue
            if c == '[':
                num_stack.append(k)
                k = 0
                str_stack.append(str(c))
                continue
            if c != ']':
                str_stack.append(str(c))
                continue
            temp = "" 
            while str_stack[-1] != '[':
                temp = str_stack.pop() + temp
            # Remove the "[" from stack
            str_stack.pop()
            # Get the new string
            replacement = ""
            count = num_stack.pop()
            for i in range(count):
                replacement += temp
            # Add it to the stack
            str_stack.append(replacement)
        result = ""
        while str_stack:
            result = str_stack.pop() + result

        return result