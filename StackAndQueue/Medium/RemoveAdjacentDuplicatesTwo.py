from collections import deque

class Pair:
    def __init__(self, cnt, ch):
        self.cnt = cnt
        self.ch = ch

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        counts = deque()
        for i in range(len(s)):
            if not counts or s[i] != counts[-1].ch:
                counts.append(Pair(1, s[i]))
            else:
                counts[-1].cnt += 1
                if counts[-1].cnt == k:
                    counts.pop()

        result = []
        while counts:
            p = counts.pop()
            result.append(p.ch * p.cnt)

        return ''.join(result[::-1])

# Example usage:
sol = Solution()
s = "deeedbbcccbdaa"
k = 3
result = sol.removeDuplicates(s, k)
print(result)
