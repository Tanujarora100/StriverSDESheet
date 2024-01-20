from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        number1, number2 = -1, -1
        count, count2 = 0, 0
        
        for num in nums:
            if number1 == num:
                count += 1
            elif number2 == num:
                count2 += 1
            elif count == 0:
                count = 1
                number1 = num
            elif count2 == 0:
                count2 = 1
                number2 = num
            else:
                count -= 1
                count2 -= 1

        ans = []
        count, count2 = 0, 0
        
        for num in nums:
            if num == number1:
                count += 1
            elif num == number2:
                count2 += 1

        if count > len(nums) // 3:
            ans.append(number1)
        if count2 > len(nums) // 3:
            ans.append(number2)

        return ans
