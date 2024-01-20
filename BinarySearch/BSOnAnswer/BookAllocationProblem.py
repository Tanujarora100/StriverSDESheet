class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, A, N, M):
        # Helper function to check if it's possible to allocate pages with given constraints
        def isPossible(arr, n, m, mid):
            if m > n:  # If the number of students is greater than the number of books, it's impossible
                return False
            curr_student = 1  # Initialize current student to 1
            curr_pages = 0  # Initialize current pages read to 0
            for i in range(n):  # Iterate through the array of pages
                if curr_pages + arr[i] <= mid and arr[i] < mid:  # If adding the current page doesn't exceed the limit and the page is less than the limit
                    curr_pages += arr[i]  # Add the current page to the current pages read
                elif curr_pages + arr[i] > mid:  # If adding the current page would exceed the limit
                    curr_student += 1  # Increment the student count
                    curr_pages = arr[i]  # Reset the current pages read to the current page
                    if curr_student > m:  # If the current student count exceeds the allowed students
                        return False  # It's impossible to allocate pages
                else:  # If the page is exactly the limit, it's not possible
                    return False
            return True  # It's possible to allocate pages

        start = max(A)  # Set the start as the maximum number of pages
        end = sum(A)  # Set the end as the total sum of pages
        ans = -1  # Initialize the answer as -1
        while start <= end:  # Binary search loop
            mid = start + (end - start) // 2  # Calculate the mid value
            if isPossible(A, N, M, mid):  # If it's possible to allocate pages with the current mid value
                ans = mid  # Update the answer
                end = mid - 1  # Move the end to mid - 1
            else:  # If it's not possible to allocate pages with the current mid value
                start = mid + 1  # Move the start to mid + 1
        return ans  # Return the answer



