from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        dicts = {}
        for i in range(len(nums)):
            if nums[i] not in dicts:
                dicts[nums[i]] =1
            else:
                dicts[nums[i]]+=1
        print(dicts)
        for keys, values in dicts.items():
            if values == 2:
                answer.append(keys)
        return answer