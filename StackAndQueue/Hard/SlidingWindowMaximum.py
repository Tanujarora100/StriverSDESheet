from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        res = []

        # Process the first k elements
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])

        # Process the rest of the elements
        for i in range(k, len(nums)):
            if dq[0] == i - k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            res.append(nums[dq[0]])

        # Return the result as a list
        return res