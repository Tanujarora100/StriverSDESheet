class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s) - 1

        while left < len(s) and s[left].isspace():
            left += 1

        while right >= 0 and s[right].isspace():
            right -= 1

        stack = []
        while left <= right:
            word = ''
            while left <= right and not s[left].isspace():
                word += s[left]
                left += 1

            stack.append(word)

            while left <= right and s[left].isspace():
                left += 1

        result = ' '.join(reversed(stack))
        return result

