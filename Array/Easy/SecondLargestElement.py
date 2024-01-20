class Solution:

    # Approach 2-Sort the array first
    # Get the second largest element from the array
    def print2largest(self,arr, n):
        # code here
        arr.sort()
        for i in range(n-1,-1,-1):
            if arr[i]!=arr[n-1]:
                return arr[i]
        return -1