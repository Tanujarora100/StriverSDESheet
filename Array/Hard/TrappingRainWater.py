from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) <= 2:
            return 0
        ans = 0
        # using two pointers i and j on indices 1 and n-1
        i = 1
        j = len(height) - 1
        # initialising leftmax to the leftmost bar and rightmax to the rightmost bar
        lmax = height[0]
        rmax = height[-1]
        while i <= j:
            # check lmax and rmax for current i, j positions
            if height[i] > lmax:
                lmax = height[i]
            if height[j] > rmax:
                rmax = height[j]
            # fill water upto lmax level for index i and move i to the right
            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1
            # fill water upto rmax level for index j and move j to the left
            else:
                ans += rmax - height[j]
                j -= 1
        return ans

    def trap(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_max = [0]*n
        suffix_max = [0] * n

        # Calculate the Prefix Max Array
        prefix_max[0] = arr[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], arr[i])

        # Calculate the Suffix Max Array
        suffix_max[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], arr[i])

        trapped_water = 0
        for i in range(n):
            trapped_water += min(prefix_max[i], suffix_max[i])-arr[i]
        return trapped_water