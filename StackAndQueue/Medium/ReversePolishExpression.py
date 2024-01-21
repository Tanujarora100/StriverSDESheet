from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand_dict = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        for i in tokens:
            if i in operand_dict:
                num1 = stack.pop()
                num2 = stack.pop()
                op_performed = operand_dict[i]
                # Corrected order of operands
                stack.append(op_performed(num2, num1))
            else:
                stack.append(int(i))
        return stack[-1]