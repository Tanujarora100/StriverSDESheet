from typing import List


class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        curr_cost= nums[0]
        max_profit=0
        for i in range(1,len(nums)):
            curr_profit= nums[i]-curr_cost
            max_profit= max(max_profit, curr_profit)
            curr_cost= min(curr_cost, nums[i])
        return max_profit