class Solution:
    def merge(self, arr, l, m, r):
        # Initialize pointers for the left and right subarrays
        i = l
        j = m + 1
        # Create an empty list to store the merged subarray
        merged = []

        # Merge the subarrays by comparing elements and appending them to the merged list
        while i <= m and j <= r:
            if arr[i] <= arr[j]:
                merged.append(arr[i])
                i += 1
            else:
                merged.append(arr[j])
                j += 1

        # Append any remaining elements from the left subarray
        while i <= m:
            merged.append(arr[i])
            i += 1

        # Append any remaining elements from the right subarray
        while j <= r:
            merged.append(arr[j])
            j += 1

        # Copy the merged list back to the original array
        for k in range(len(merged)):
            arr[l + k] = merged[k]

        def mergeSort(self, arr, l, r):
            if l >= r:
                return arr
            
            m = (l + r) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)

            return arr
            
