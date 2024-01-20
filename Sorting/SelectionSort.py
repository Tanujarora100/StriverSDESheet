class Solution: 
    def select(self, arr, i):
        # Initialize the minimum position as the current index
        minpos = i
        # Iterate through the array starting from the current index
        for j in range(i, len(arr)):
            # If the element at the current index is less than the element at the minimum position
            if arr[j] < arr[minpos]:
                # Update the minimum position to the current index
                minpos = j
        # Return the index of the minimum element
        return minpos
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            minpos = self.select(arr,i)
            arr[minpos], arr[i] = arr[i], arr[minpos]