class solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        balance = 0
        open_seen = 0
        for i in s:
            if i == '(':
                open_seen += 1
                balance += 1
                stack.append(i)
            elif i == ')':
                if balance > 0:
                    balance -= 1
                    stack.append(i)
                else:
                    continue
            else:
                stack.append(i)

        result = []

        keep_open = open_seen-balance
        for i in stack:
            if i == '(':
                keep_open -= 1
                if keep_open < 0:
                    continue
            result.append(i)
        return "".join(result)