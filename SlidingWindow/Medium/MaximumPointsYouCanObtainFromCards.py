from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        if k==len(cardPoints):
            return sum(cardPoints)
        left=0
        n=len(cardPoints)
        right= n-k
        total_sum= sum(cardPoints[right:])
        max_sum=total_sum
        # Current Window starting from left
        while right< len(cardPoints):
            total_sum+= (cardPoints[left]- cardPoints[right])
            max_sum= max(max_sum,total_sum)
            left=left+1
            right=right+1
        return max_sum


        