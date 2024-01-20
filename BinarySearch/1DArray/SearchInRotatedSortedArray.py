from typing import List


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        start=0
        end=len(arr)-1
        while start<=end:
            mid= start+(end-start)//2
            if arr[mid]==target:
                return mid
            # Checking if the left part is sorted
            if arr[start]<=arr[mid]:
                if arr[start]<=target and target<=arr[mid]:
                    end=mid-1
                else:
                    start=mid+1
            if arr[mid]<=arr[end]:
                if arr[mid]<=target and target<=arr[end]:
                    start=mid+1
                else:
                    end=mid-1
        return -1
            