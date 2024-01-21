def calculateSpan(self, arr, n):
        stack = [[arr[0], 0]]
        ans = [1]
        for i in range(1, n):
            if stack[-1][0] > arr[i]:
                stack.append([arr[i], i])
                ans.append(1)
            else:
                while stack and stack[-1][0] <= arr[i]:
                    stack.pop()
                if(len(stack))==0:
                    ans.append(i+1)
                else:
                    ans.append(i-stack[-1][1])
                stack.append([arr[i],i])

        return ans