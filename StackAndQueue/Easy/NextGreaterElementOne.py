from collections import deque

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = deque()
        stack.append(-1)
        hashMap = {}
        
        # Traverse nums2 in reverse order
        for i in range(len(nums2) - 1, -1, -1):
            # Pop elements from stack until we find a greater element
            while len(stack) > 1 and stack[-1] <= nums2[i]:
                stack.pop()
            # Store the next greater element in the hash map
            hashMap[nums2[i]] = stack[-1]
            # Push the current element onto the stack
            stack.append(nums2[i])

        finalAns = []
        # Find the next greater element for each element in nums1 using the hash map
        for num in nums1:
            finalAns.append(hashMap.get(num, -1))
        return finalAns

# Example usage:
sol = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
result = sol.nextGreaterElement(nums1, nums2)
print(result)
