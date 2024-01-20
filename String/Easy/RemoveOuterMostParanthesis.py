class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans, cnt = [], 0
        for ch in s:
            if ch == '(' and cnt > 0: ans.append(ch)
            if ch == ')' and cnt > 1: ans.append(ch)
            cnt += 1 if ch == '(' else -1
        return "".join(ans)