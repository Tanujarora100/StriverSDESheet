from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans_list=[]
        temp_list=[]
        def backTrack(openCount, closedCount):
            if openCount==closedCount==n:
                ans_list.append("".join(temp_list))
                return
            
            # Call for open parentheses
            if openCount<n:
                temp_list.append("(")
                backTrack(openCount+1,closedCount)
                temp_list.pop()
            # Call for Closed Parentheses
            if closedCount<openCount:
                temp_list.append(")")
                backTrack(openCount, closedCount+1)
                temp_list.pop()
        backTrack(0,0)
        return ans_list