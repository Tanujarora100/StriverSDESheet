from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans_list = []
        potions.sort()
        if len(potions) == 0 or len(spells) == 0:
            return []
        for i in range(len(spells)):
            ans = self.binary_search(spells[i], potions, success)
            ans_list.append(ans)
        return ans_list

    def binary_search(self, number, potions, success):
        count_pairs = 0
        start = 0
        end = len(potions) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if potions[mid] * number >= success:
                count_pairs += end - mid + 1
                end = mid - 1
            else:
                start = mid + 1
        return count_pairs
    # Time Complexity-O(N)* LOG(M) + O(MLOGM) For Sorting


# Brute Force- O(N)+O(N)
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans_list = []

        def helper(number, potions, success):
            nonlocal ans_list
            count_pairs = 0
            for i in range(len(potions)):
                if potions[i] * number >= success:
                    count_pairs += 1
            ans_list.append(count_pairs)

        for i in range(len(spells)):
            helper(spells[i], potions, success)
        return ans_list