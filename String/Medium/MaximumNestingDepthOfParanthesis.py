class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0  # count current depth of "()"
        max_depth = 0  # count max depth of "()"

        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            max_depth = max(count, max_depth)

        return max_depth


