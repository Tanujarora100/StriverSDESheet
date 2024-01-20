from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        
        def first_occurence(nums, target, first_occurence):
            start=0
            end=len(nums)-1
            while start<=end:
                mid=start+(end-start)//2
                if nums[mid]>target:
                    end=mid-1
                elif nums[mid]<target:
                    start=mid+1
                else:
                    first_occurence=mid
                    end=mid-1
            return first_occurence
        
        
        def last_occurence(nums, target, last_occurence):
            start=0
            end=len(nums)-1
            while start<=end:
                mid=start+(end-start)//2
                if nums[mid]<target:
                    start=mid+1
                elif nums[mid]>target:
                    end=mid-1
                else:
                    last_occurence=mid
                    start=mid+1
            return last_occurence
        
        
        first_occur=first_occurence(nums,target,-1)
        last_occur=last_occurence(nums,target,-1)
        return [first_occur,last_occur]