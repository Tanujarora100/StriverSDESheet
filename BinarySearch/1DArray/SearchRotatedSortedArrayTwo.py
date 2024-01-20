class Solution:
    def search(self, arr, target):
        # Set the start and end pointers for the array
        start = 0
        end = len(arr) - 1

        # Loop until the start pointer is less than or equal to the end pointer
        while start <= end:
            # Calculate the middle index
            mid = start + (end - start) // 2

            # If the middle value is equal to the target, return True
            if arr[mid] == target:
                return True

            # If the start, middle, and end values are all the same, move the start and end pointers
            if arr[start] == arr[mid] and arr[mid] == arr[end]:
                start += 1
                end -= 1
            # If the left half of the array is in increasing order
            elif arr[start] <= arr[mid]:
                # If the target is within the left half, update the end pointer
                if arr[start] <= target <= arr[mid]:
                    end = mid - 1
                # Otherwise, update the start pointer
                else:
                    start = mid + 1
            # If the right half of the array is in increasing order
            else:
                # If the target is within the right half, update the start pointer
                if arr[mid] <= target <= arr[end]:
                    start = mid + 1
                # Otherwise, update the end pointer
                else:
                    end = mid - 1

        # If the target is not found, return False
        return False
