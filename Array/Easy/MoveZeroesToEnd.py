from typing import List
def moveZeroes(self, nums: List[int]) -> None:
    # Initialize two pointers, ptr1 and ptr2, both pointing to the start of the list
    ptr1 = 0
    ptr2 = 0
    
    # Iterate through the list using ptr2
    while ptr2 < len(nums):
        # If the element at ptr2 is 0, move ptr2 to the next element
        if nums[ptr2] == 0:
            ptr2 += 1
        else:
            # If the element at ptr2 is not 0, swap the elements at ptr1 and ptr2, then move both pointers to the next element
            nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
            ptr1 += 1
            ptr2 += 1
             
        